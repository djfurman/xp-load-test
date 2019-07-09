from locust import HttpLocust, TaskSet, task


class UserBehavior(TaskSet):
    @task(1)
    def fetch_api_root(self):
        self.client.get("/api")

    @task(2)
    def fetch_api_v1(self):
        self.client.get("/api/v1")

    @task(5)
    def fetch_api_v1_articles(self):
        self.client.get("/api/v1/articles")


class ApiUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 30  # thirty milliseconds
    max_wait = 1000  # one second
