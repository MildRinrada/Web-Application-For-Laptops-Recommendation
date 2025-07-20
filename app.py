from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder='pages', static_url_path='/static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:ppgdmild@localhost/laptopdb'
db = SQLAlchemy(app)
