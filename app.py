from flask import Flask
from config import Configuration
from posts.blueprint import posts
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy as sa


app = Flask(__name__)
app.config.from_object(Configuration)
app.register_blueprint(posts, url_prefix='/blog')
db = SQLAlchemy(app)

sa.Column(sa.Integer)

