from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from os import environ
from models import db
from apps.controller.app_controller import app_router


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DB_URL')
app.register_blueprint(app_router)
db.init_app(app)


with app.app_context():
    db.create_all()
app.run(host='0.0.0.0', port=5000)