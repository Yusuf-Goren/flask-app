from app import app

def test_student():
    response = app.test_client().get('/get-students')
    assert response.status_code == 200
    
