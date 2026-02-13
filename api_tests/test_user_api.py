import pytest
import logging

logging.basicConfig(level=logging.INFO)
def test_get_post_status_code(client):
    response = client.get_post(1)

    assert response.status_code == 200


def test_get_post_id(client):
    response = client.get_post(1)
    data = response.json()

    assert data["id"] == 1

def test_post_field_types(client):
    response = client.get_post(1)
    data = response.json()

    assert isinstance(data["userId"], int)
    assert isinstance(data["id"], int)
    assert isinstance(data["title"], str)
    assert isinstance(data["body"], str)

def test_post_fields(client):
    response = client.get_post(1)
    data = response.json()

    assert "userId" in data
    assert "id" in data
    assert "title" in data
    assert "body" in data

def test_non_existing_post(client):
    response = client.get_post(999999)
    assert response.status_code == 404
    data = response.json()
    # перевірка статус-коду
    assert data == {} or data is None

@pytest.mark.parametrize(
    "post_id,expected_status_code",
    [
        (999999, 404), 
        (1, 200),
        (4,200)
    ]
)
def test_post_status_codes(client, post_id, expected_status_code):
    logging.info(f"Testing post {post_id} expecting {expected_status_code}")
    response = client.get_post(post_id)
    assert response.status_code == expected_status_code
    logging.info(f"Tested post {post_id} with status code {response.status_code}")

def test_create_post(client):
    title = "My test post"
    body = "This is a post created by automation test"
    user_id = 1

    response = client.create_post(title, body, user_id)

    # Перевірка статусу
    assert response.status_code == 201  # POST повинен повернути 201 Created

    # Перевірка полів у відповіді
    data = response.json()
    assert data["title"] == title
    assert data["body"] == body
    assert data["userId"] == user_id
    assert "id" in data
    logging.info(f"Post ID {data["id"]}")