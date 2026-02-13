import requests


class APIClient:
    def __init__(self, base_url: str):
        self.base_url = base_url
        

    def get_post(self, post_id: int):
        return requests.get(f"{self.base_url}/posts/{post_id}")

    def create_post(self, title: str, body: str, userId: int):
        payload = {
            "title": title,
            "body": body,
            "userId": userId
        }
        return requests.post(f"{self.base_url}/posts", json=payload)