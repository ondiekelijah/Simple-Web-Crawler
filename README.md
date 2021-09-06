## Requirements ,Packages used and Installation
Download and install Python. Make sure you install Python v3.6.+
 
## Installation
          
Navigate to your directory of choice the proceed as follows;<br>
          
### 1 .Clone the git repo and create a virtual environment 
          
Depending on your operating system,make a virtual environment to avoid messing with your machine's primary dependencies
          
**Windows**
          
```
git clone https://github.com/Dev-Elie/Simple-Web-Crawler.git
cd Simple-Web-Crawler
py -3 -m venv venv
```
          
**macOS/Linux**
          
```
git clone https://github.com/Dev-Elie/Simple-Web-Crawler.git
cd Simple-Web-Crawler
python3 -m venv venv
```

### 2 .Activate the virtual environment (venv)
          
**Windows** 

```venv\Scripts\activate```
          
**macOS/Linux**

```. venv/bin/activate```
or
```source venv/bin/activate```

### 3 .Install the requirements

Applies for windows/macOS/Linux

```pip install -r requirements.txt```

### 4. Run the application 

**For linux and macOS**
Make the run file executable by running the code

```chmod 777 run```

Then start the application by executing the run file

```./run```

**On windows**
```
set FLASK_APP=main
flask run
```
Then on your browser open `localhost:5000` or `http://127.0.0.1:5000/` <br>
You should receive a response — a page similar to the one seen in the screenshot.
