from locust import HttpUser, task

class checkTraffic(HttpUser):
    @task
    def hello_world(self):
        self.client.get("/v1/customers/")