import pytest
from fastapi.testclient import TestClient
from app import app
import PIL


client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Сервис для определения породы собакена."}


def test_predict_german_shepherd():
    files = {'photo': open('server/test files/German_shepherd.jpg', 'rb')}
    response = client.post("/predict/", files=files)
    json_data = response.json()

    assert response.status_code == 200
    assert json_data['label'] == 'German_shepherd'


def test_predict_siberian_husky():
    files = {'photo': open('server/test files/Siberian_husky.jpg', 'rb')}
    response = client.post("/predict/", files=files)
    json_data = response.json()

    assert response.status_code == 200
    assert json_data['label'] == 'Siberian_husky'


def test_predict_great_dane():
    files = {'photo': open('server/test files/Great_Dane.jpg', 'rb')}
    response = client.post("/predict/", files=files)
    json_data = response.json()

    assert response.status_code == 200
    assert json_data['label'] == 'Great_Dane'


def test_predict_empty_file():
    with pytest.raises(PIL.UnidentifiedImageError):
        files = {'photo': open('server/test files/empty_file', 'rb')}
        response = client.post("/predict/", files=files)
        assert response.status_code == 500
