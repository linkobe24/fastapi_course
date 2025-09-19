from fastapi import status
from .utils import *
from ..main import app
from ..routers.users import get_db, get_current_user
from ..models import Users


app.dependency_overrides[get_db] = override_get_db
app.dependency_overrides[get_current_user] = override_get_current_user


def test_return_user(test_user):
    response = client.get("/user")
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["username"] == "manueltest"
    assert response.json()["email"] == "manuel@email.com"
    assert response.json()["first_name"] == "Manuel"
    assert response.json()["last_name"] == "Beltran"
    assert response.json()["role"] == "admin"
    assert response.json()["phone_number"] == "(111)-111-111"


def test_change_password_success(test_user):
    response = client.put(
        "/user/password/",
        json={"password": "testpassword", "new_password": "newpassword"},
    )

    assert response.status_code == status.HTTP_204_NO_CONTENT


def test_change_password_invalid_current_password(test_user):
    response = client.put(
        "/user/password/",
        json={"password": "incorrectpassword", "new_password": "newpassword"},
    )

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.json() == {"detail": "Password does not match"}


def test_change_phone_number_success(test_user):
    response = client.put("/user/phonenumber/12341234")

    assert response.status_code == status.HTTP_204_NO_CONTENT
