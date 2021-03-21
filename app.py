from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.secret_key = '67eadccda3bc198f2b9712c77912bd55'
app.config['SQLALCHEMY_DATABASE_URI']='mysql+mysqlconnector://elie:dev123@localhost/scrappy'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db =SQLAlchemy(app)
migrate = Migrate(app, db)