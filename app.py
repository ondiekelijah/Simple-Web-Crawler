from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, redirect, flash, url_for
from forms import *
import json 
import urllib.request 
from urllib.parse import urlparse,urljoin
from bs4 import BeautifulSoup
import requests
import validators

app = Flask(__name__)
app.secret_key = '67eadccda3bc198f2b9712c77912bd55'
app.config['SQLALCHEMY_DATABASE_URI']='mysql+mysqlconnector://elie:dev123@localhost/scrappy'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db =SQLAlchemy(app)
migrate = Migrate(app, db)

@app.route("/",methods=("GET", "POST"), strict_slashes=False)
def index():
    form = Url()
    if request.method == "POST":
        requested_url = form.urltext.data
        tag = form.specificElement.data
        valid=validators.url(requested_url)

        if valid==True:
            requested_url = requested_url
            source = requests.get(requested_url).text
            soup = BeautifulSoup(source, 'lxml') # alternatively >> soup = BeautifulSoup(source, "html.parser")
            
            specific_element = soup.find_all(tag)

            counter = len(specific_element)

            if tag == 'img':
                images = [img['src'] for img in specific_element]
                image_paths = []
                for i in specific_element:
                    image_path = i.attrs['src']
                    valid_imgpath = validators.url(image_path)
                    if valid_imgpath == True:
                        full_path = image_path
                    else:
                        full_path = urljoin(requested_url, image_path)
                        image_paths.append(full_path)

                return render_template("index.html",form=form,title="Scrap The Web",url = requested_url,counter=counter,image_paths=image_paths,results = specific_element)
            return render_template("index.html",form=form,title="Scrap The Web",url = requested_url,counter=counter,results = specific_element)
        else:
            flash(f"Invalid or Malformed URL", "danger")
    return render_template("index.html",form=form,title="Scrap The Web")

    if __name__ == "__main__":
        app.run(debug=True)