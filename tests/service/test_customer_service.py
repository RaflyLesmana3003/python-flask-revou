from app.models.customer import Customer
from app.service.customer_service import Customer_service
from app.repositories.customer_repo import Customer_repo


def test_get_list_customer(test_app, mocker):
   mock_customer_data = [
      Customer(id=1, name='John', phone=12, gender='laki laki'),
   ]
   mocker.patch.object(Customer_repo, 'get_list_customer',
                     return_value=mock_customer_data)
   
   with test_app.test_request_context():
      customer_service = Customer_service().get_customers()

   print(customer_service)