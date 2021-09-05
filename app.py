from flask import Flask, render_template, request, flash,url_for,redirect,current_app
from forms import *
import urllib.request 
from urllib.parse import urlparse,urljoin
from bs4 import BeautifulSoup
import requests,validators,json ,uuid,pathlib,os


app = Flask(__name__)
app.secret_key = 'my-super-secret-key'



def image_handler(tag,specific_element,requested_url):
    image_paths = []

    if tag == 'img':
        images = [img['src'] for img in specific_element]
        for i in specific_element:
            image_path = i.attrs['src']
            valid_imgpath = validators.url(image_path)
            if valid_imgpath == True:
                full_path = image_path
            else:
                full_path = urljoin(requested_url, image_path)
                image_paths.append(full_path)

    return image_paths



@app.route("/",methods=("GET", "POST"), strict_slashes=False)
def index():
    form = Url()
    if request.method == "POST":

        global requested_url,specific_element,tag

        requested_url = form.urltext.data
        tag = form.specificElement.data
        valid = validators.url(requested_url)

        if valid==True:
            requested_url = requested_url
            source = requests.get(requested_url).text
            # parser library?
            soup = BeautifulSoup(source, "html.parser")
            
            specific_element = soup.find_all(tag)
            
            counter = len(specific_element)

            image_paths = image_handler(tag,specific_element,requested_url)

            return render_template("index.html",
                form=form,title="Scrap The Web",
                url = requested_url,
                counter=counter,
                image_paths=image_paths,
                results = specific_element
                )
        else:
            flash(f"Invalid or Malformed URL", "danger")
    return render_template("index.html",form=form)


@app.route("/download",methods=("GET", "POST"), strict_slashes=False)
def downloader():
    try:
        for img in image_handler(tag,specific_element,requested_url):
            image_url = img

            filename = str(uuid.uuid4())
            file_ext = pathlib.Path(image_url).suffix

            picture_filename = filename + file_ext

            picture_path  = os.path.join(
            current_app.root_path, "static/images/downloads", picture_filename
            )

            urllib.request.urlretrieve(image_url, picture_path)

        flash("Images saved in your static/downloads directory", "success")

    except Exception as e:
        flash(e, "danger")

    return redirect(url_for('index'))

    if __name__ == "__main__":
        app.run(debug=True)