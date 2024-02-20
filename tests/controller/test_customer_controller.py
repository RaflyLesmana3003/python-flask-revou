def test_get_customers(test_app):
   response =test_app.get("v1/customers/")
   print(response.json['data'])
   assert len(response.json['data']) == 7

def test_post_customers(test_app):
   data = {
         "name": "raly", 
         "phone": 23,
         "gender": "laki laki"
   }
   expected_response = {
      'id': 21, 
      'name': 'raly', 
      'phone': 23
   }

   response = test_app.post("v1/customers/", json=data)

   assert response.json['data'] == expected_response
   assert response.status_code == 201

def test_put_customers(test_app):
   data =  {
         "name": "rafly", 
         "phone": 23,
   }
   response = test_app.put("v1/customers/22", json=data)
   
   assert response.status_code == 200


def test_put_customers(test_app):
   response = test_app.delete("v1/customers/22")
   
   assert response.status_code == 200
