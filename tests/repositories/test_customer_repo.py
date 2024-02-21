from unittest import mock

import pytest

from app import app
from app.models.customer import Customer
from app.repositories.customer_repo import Customer_repo


def test_get_list_customer(mocker):
    mock_customers = [Customer(id=1, name='Alice'), Customer(id=2, name='Bob')]
    mocker.patch('app.models.customer.Customer.query.all', return_value=mock_customers)
    repo = Customer_repo()
    result = repo.get_list_customer()
    assert result == mock_customers

def test_create_customer(mocker):
    mock_customer = Customer(id=1, name='Alice')
    mocker.patch('app.utils.database.db.session.add')
    mocker.patch('app.utils.database.db.session.commit')
    repo = Customer_repo()
    result = repo.create_customer(mock_customer)
    assert result == mock_customer
    app.utils.database.db.session.add.assert_called_with(mock_customer)
    app.utils.database.db.session.commit.assert_called_once()

def test_update_customer(mocker):
    mock_customer = mock.Mock(spec=Customer)
    mocker.patch('app.models.customer.Customer.query.get', return_value=mock_customer)
    mocker.patch('app.utils.database.db.session.commit')
    repo = Customer_repo()
    updated_customer = repo.update_customer(1, {'name': 'Alice Updated', 'phone': '12345'})
    assert updated_customer.name == 'Alice Updated'
    assert updated_customer.phone == '12345'
    app.utils.database.db.session.commit.assert_called_once()

def test_delete_customer(mocker):
    mock_customer = mock.Mock(spec=Customer)
    mocker.patch('app.models.customer.Customer.query.get', return_value=mock_customer)
    mocker.patch('app.utils.database.db.session.delete')
    mocker.patch('app.utils.database.db.session.commit')
    repo = Customer_repo()
    result = repo.delete_customer(1)
    assert result == mock_customer
    app.utils.database.db.session.delete.assert_called_with(mock_customer)
    app.utils.database.db.session.commit.assert_called_once()

def test_search_customer(mocker):
    mock_customers = [Customer(id=1, name='Alice'), Customer(id=2, name='Bob')]
    mocker.patch('app.models.customer.Customer.query.filter', return_value=mock_customers)
    repo = Customer_repo()
    result = repo.search_customer('Al')
    assert result == mock_customers
