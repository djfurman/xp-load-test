from locust import HttpLocust, TaskSet, task

class UserBehavior(TaskSet):
    pass

class ApiUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 30
    max_wait = 1000
