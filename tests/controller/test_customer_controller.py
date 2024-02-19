def test_get_customers(test_app):
   response =test_app.get("v1/customers/")
   print(response.json['data'])
   assert len(response.json['data']) == 6

def test_post_customers(test_app):
   data = {
         "name": "raly", 
         "phone": 23,
   }
   response = test_app.post("v1/customers/", json=data)

   assert response.json == 201
   assert response.status_code == 200

def test_put_customers_400(test_app):
   data = {}
   response = test_app.put("v1/customers/1", json=data)
   
   assert response.status_code == 400
