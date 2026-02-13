import requests


class APIClient:
    def __init__(self, base_url: str):
        self.base_url = base_url

    def get_post(self, post_id: int):
        return requests.get(f"{self.base_url}/posts/{post_id}")