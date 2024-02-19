from app import app
import pytest
import os


@pytest.fixture
def test_app():
      app.config['TESTING'] = True

      # Get database configuration from environment variables
      DATABASE_TYPE = os.getenv('DATABASE_TYPE')
      DATABASE_USER = os.getenv('DATABASE_USER')
      DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')
      DATABASE_HOST = os.getenv('DATABASE_HOST')
      DATABASE_NAME = os.getenv('DATABASE_NAME')
      DATABASE_PORT = os.getenv('DATABASE_PORT')
      
      # Configure the database URI
      app.config['SQLALCHEMY_DATABASE_URI'] = f"{DATABASE_TYPE}://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"


      with app.test_client() as client:
            yield client