from flask import Flask
from app.controller.customers import customer_route
import os
from app.utils.database import db, migrate

app = Flask(__name__)

DATABASE_TYPE = os.getenv('DATABASE_TYPE', 'postgresql')
DATABASE_USER = os.getenv('DATABASE_USER', 'default_user')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD', 'default_password')
DATABASE_HOST = os.getenv('DATABASE_HOST', 'default_host')
DATABASE_NAME = os.getenv('DATABASE_NAME', 'default_database_name')
DATABASE_PORT = os.getenv('DATABASE_PORT', 0)
app.config["SQLALCHEMY_DATABASE_URI"] = f"{DATABASE_TYPE}://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"

db.init_app(app)
migrate.init_app(app, db)

app.register_blueprint(customer_route.customer_blueprint, url_prefix="/v1/customers")