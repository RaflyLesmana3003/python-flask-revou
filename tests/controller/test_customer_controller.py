
from app import db
from app.service.customer_service import Customer_service


def test_get_customers(test_app, mocker):
   # Arrange
   mock_customer_data = [
      {
         "id": 22,
         "name": "rafly",
         "phone": 23
      },
   ]
   mocker.patch.object(Customer_service, 'get_customers',
                     return_value=mock_customer_data)

   # Act
   with test_app.test_client() as client:
      response = client.get("/v1/customers/")

   # Assert
   assert response.status_code == 200
   assert len(response.json['data']) == len(mock_customer_data)
   assert response.json['data'] == mock_customer_data


def test_post_customers(test_app, mocker):
   # Arrange
   data = {
      "name": "raly",
      "phone": 23,
      "gender": "laki laki"
   }
   mocker.patch.object(Customer_service, 'create_customer', return_value=data)

   # Act
   with test_app.test_client() as client:
      response = client.post("/v1/customers/", json=data)

   # Assert
   expected_response = {
      "name": "raly",
      "phone": 23,
      "gender": "laki laki"
   }
   assert response.json['data'] == expected_response
   assert response.status_code == 201


def test_put_customer_update(test_app, mocker):
   # Arrange
   data = {
      "name": "rafly",
      "phone": 23,
   }

   mocker.patch.object(Customer_service, 'update_customer', return_value=data)

   # Act
   with test_app.test_client() as client:
         response = client.put("/v1/customers/22", json=data)

   # Assert
   assert response.status_code == 200


def test_delete_customer(test_app, mocker):
   # Arrange
   expected_response = {
      "name": "raly",
      "phone": 23,
      "gender": "laki laki"
   }

   mocker.patch.object(Customer_service, 'delete_customer', return_value=expected_response)
   with test_app.test_client() as client:
      # Act
      response = client.delete("/v1/customers/23")

   # Assert
   assert response.status_code == 200
