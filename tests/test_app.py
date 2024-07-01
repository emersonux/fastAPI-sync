from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app

client = TestClient(app)


def test_read_root_deve_retornar_ok_e_ola_mundo():
    client = TestClient(app)

    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Here we go again'}


def test_create_user():
    client = TestClient(app)
    response = client.post(  # Envio do user no schema
        '/users/',
        json={
            'username': 'emerson',
            'password': 'secret',
            'email': 'emerson@example.com',
        },
    )

    # Voltou o status code correto?
    assert response.status_code == HTTPStatus.CREATED

    # Validar UserPublic
    assert response.json() == {
        'username': 'emerson',
        'id': 1,
        'email': 'emerson@example.com',
    }
