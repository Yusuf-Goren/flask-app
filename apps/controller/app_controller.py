from apps.service import app_service
from flask import Blueprint,request
app_router = Blueprint('dbscan_handlers', __name__)

@app_router.route('/create', methods=['POST'])
def create_student():
    json_data = request.get_json()
    return app_service.create_student(json_data)

@app_router.route('/get-student/<std_number>', methods=['GET'])
def get_student(std_number):
    return app_service.get_student(std_number)

@app_router.route('/get-students', methods=['GET'])
def get_students():
    return app_service.get_all_student()

    
