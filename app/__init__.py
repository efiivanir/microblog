from flask import Flask
from config import Config
from flask_bootstrap import Bootstrap
app = Flask(__name__)
app.config.from_object(Config)

bootstrap = Bootstrap()
bootstrap.init_app(app)

from app import routes