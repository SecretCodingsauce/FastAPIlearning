from fastapi.testclient import TestClient
from app.main import app
import app.schemas as schemas

from app.database import get_db

from tests.database import override_get_db


app.dependency_overrides[get_db] = override_get_db


client = TestClient(app)

def test_root():
    res = client.get("/")
    print(res.json())
    assert res.json()=="appp withhh faaassst aaapppiiii"


def test_create_user():
    res= client.post("/users/newuser",json={"email":"test@gmail.com", "password":"pass123"})

    new_user=schemas.UserOut(**res.json())
    assert new_user.email== "test@gmail.com"
    assert res.status_code==201
    

    