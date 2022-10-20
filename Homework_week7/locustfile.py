import numpy as np
from locust import task, between, HttpUser

sample = [[6.4,3.5,4.5,1.2]]
 
class TestUserTraffic(HttpUser):
    """
    Usage:
        Start locust load testing client with:
            locust -H http://localhost:3000
        Open browser at http://0.0.0.0:8089, adjust desired number of users and spawn
        rate for the load test from the Web UI and start swarming.
    """
    
    @task
    def main(self):
        self.client.post('/main', json = sample)
        
    wait_time = between(0.01, 2)