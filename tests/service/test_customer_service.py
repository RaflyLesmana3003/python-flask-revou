from app.controller.customers.schema.create_customer_request import Create_customer_request
from app.models.customer import Customer
from app.service.customer_service import Customer_service
from app.repositories.customer_repo import Customer_repo


def test_get_list_customer_success(test_app, mocker):
   """service get customer success"""

   # Arrange
   mock_customer_data = [
      Customer(id=1, name='John', phone=12, gender='laki laki'),
      Customer(id=2, name='John', phone=13, gender='laki laki'),
   ]
   mocker.patch.object(Customer_repo, 'get_list_customer',
                     return_value=mock_customer_data)
   
   # Act
   with test_app.test_request_context():
      customer_service = Customer_service().get_customers()

   # Assert
   assert len(customer_service) == 2
   assert customer_service[0]['name'] == 'John'
   assert customer_service[1]['gender'] == 'laki laki'


def test_create_customer_success(test_app, mocker):
   """service get customer success"""
   # Arrange
   mock_customer_data = Customer(id=2, name='John', phone=12, gender='perempuan')
   mocker.patch.object(Customer_repo, 'create_customer', return_value=mock_customer_data)
   
   create_dto = Create_customer_request(name="John", phone=12, gender='perempuan')

   # Act
   with test_app.test_request_context():
      customer_service_create = Customer_service().create_customer(create_dto)
      
   # Assert
   assert customer_service_create['id'] == 2
   assert customer_service_create['name'] == 'John'
   assert customer_service_create['gender'] == 'perempuan'