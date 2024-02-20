from app import app
import pytest
import os


@pytest.fixture
def app():
      test_app
      with app.test_client() as client:
            yield client