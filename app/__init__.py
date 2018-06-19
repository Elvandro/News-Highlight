from flask import Flask

#nitializing application
app = Flask(__name__)

from app import views
