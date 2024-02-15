from flask import Blueprint, jsonify, request
from app.utils.database import db
from app.models.customer import Customer 
from app.utils.api_response import api_response
from app.service.customer_service import Customer_service
from app.controller.customers.schema.update_customer_request import Update_customer_request
from pydantic import ValidationError

customer_blueprint = Blueprint('customer_endpoint', __name__)

@customer_blueprint.route("/", methods=["GET"])
def get_list_customer():
   try: 
      customer_service = Customer_service()

      customers = customer_service.get_customers()

      return api_response(
          status_code=200,
          message="",
          data=customers
      )
   
   except Exception as e:
      return str(e), 500
   
   
@customer_blueprint.route("/search", methods=["GET"])
def search_customer():
   try: 
      request_data = request.args
      customer_service = Customer_service()

      customers = customer_service.search_customer(request_data["name"])

      return api_response(
          status_code=200,
          message="",
          data=customers
      )
   
   except Exception as e:
      return str(e), 500
   
@customer_blueprint.route("/<int:customer_id>", methods=["GET"])
def get_customer(customer_id):
      try:
         customer = Customer.query.get(customer_id)

         if not customer:
               return "Customer not found", 404

         return customer.as_dict(), 200
      except Exception as e:
         return str(e), 500

@customer_blueprint.route("/", methods=["POST"])
def create_customer():
   try: 
      data = request.json

      customer = Customer()
      customer.name = data["name"]
      customer.phone = data["phone"]
      customer.gender = data["gender"]
      db.session.add(customer)
      db.session.commit()

      return "Customer created", 201
   except Exception as e:
      return str(e), 500

@customer_blueprint.route("/<int:customer_id>", methods=["PUT"])
def update_customer(customer_id):
      try:
      
         data = request.json
         update_customer_request = Update_customer_request(**data)


         customer_service = Customer_service()

         customers = customer_service.update_customer(customer_id,update_customer_request)

         return api_response(
          status_code=200,
          message="updated",
          data=customers
      )
      except ValidationError as e:
         return  api_response(
          status_code=400,
          message=e.errors(),
          data={}
      )
      except Exception as e:
         return str(e), 500


@customer_blueprint.route("/<int:customer_id>", methods=["DELETE"])
def delete_customer(customer_id):
      try:
         customer = Customer.query.get(customer_id)

         if not customer:
               return "Customer not found", 404

         db.session.delete(customer)
         db.session.commit()

         return 'Delete successful', 200
      except Exception as e:
         return str(e), 500
