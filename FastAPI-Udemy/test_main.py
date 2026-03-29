
from main import app
from fastapi.testclient import TestClient

client=TestClient(app)

def test_get_all_product():
    response=client.get("/response/get_all")
    assert response.status_code==200
    
def test_auth_error():
    response=client.post("/token",data={'username':"",'password':''})
# No access token should be returned
    assert response.json().get("access_token") is None

def test_auth_sucess():
    response=client.post("/token",data={'username':"cat",'password':'cat'})
    assert response.json().get("access_token")
    
def test_post_article():
    # 1. Login to get token
    auth = client.post("/token", data={"username": "cat", "password": "cat"})
    access_token = auth.json().get("access_token")

    assert access_token  # ensure token exists

    # 2. Create article
    response = client.post(
        "/db_route2/create_article",
        json={
            "title": "test_title",
            "content": "test_content",
            "published": True,
            "creator_id": 1
        },
        headers={"Authorization": f"Bearer {access_token}"}
    )

    # 3. Assertions
    assert response.status_code == 200
    assert response.json().get("title") == "test_title"