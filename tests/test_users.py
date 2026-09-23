import app.schemas as schemas
import pytest
import jwt
from app.config import settings

def test_root(client):
    res = client.get("/")
    print(res.json())
    assert res.json()=="appp withhh faaassst aaapppiiii"


def test_create_user(client):
    user_data = {
                "email": "testify@example.com",
                "password": "password1234"
            }    

    res = client.post("/users/newuser", json=user_data)

    assert res.status_code == 201

    newuser=schemas.UserOut(**res.json())

    assert newuser.email == "testify@example.com"

def test_login_user(client,test_user):

    user_data={
        "username" : test_user["email"],
        "password" : test_user["password"]
    }
  
    res=client.post("/login", data=user_data)
    login_res=schemas.Token(**res.json())
    payload= jwt.decode(login_res.access_token,settings.secret_key, algorithms=[settings.algorithim])
    id=payload.get("user_id")
    assert id==test_user["id"]
    assert login_res.token_type=="bearer"
    assert res.status_code==200

@pytest.mark.parametrize("email,password,status_code",[
   ('wrongmail@gmail.com','password1234',403),
   ('testify@example.com','wrongpassword',403),
   (None,'password1234',422),
   ('testify@example.com',None,422)
])


def  test_login_error(client,email,password,status_code):
    res= client.post('/login',data={"username":email,"password":password})

    assert res.status_code==status_code

