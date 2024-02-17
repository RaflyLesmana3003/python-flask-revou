from app.repositories.customer_repo import Customer_repo
from app.models.customer import Customer

class Customer_service:
   def __init__(self):
      self.customer_repo = Customer_repo()

   def get_customers(self):
      customers = self.customer_repo.get_list_customer()
      return [customer.as_dict() for customer in customers]

   def search_customer(self, name):
      customers = self.customer_repo.search_customer(name)
      return [customer.as_dict() for customer in customers]
   
   def create_customer(self, customer_data_dto):
      customer = Customer()
      
      customer.name = customer_data_dto.name
      customer.phone = customer_data_dto.phone
      customer.gender = customer_data_dto.gender
      
      created_customer = self.customer_repo.create_customer(customer)
      return created_customer.as_dict()
   
   def update_customer(self, id, customer_data_dto):
      updated_customer = self.customer_repo.update_customer(id, customer_data_dto)
      return updated_customer.as_dict()