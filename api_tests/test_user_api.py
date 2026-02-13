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
