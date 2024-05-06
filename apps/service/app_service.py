from apps.repository import app_repository
from forms import student_form
from werkzeug.datastructures import MultiDict

def create_student(json_data):

    data = MultiDict(json_data)
    form = student_form.StudentForm(data)
    if form.validate():

        is_exist_student = app_repository.get_student(json_data["stdNumber"])
      
        if is_exist_student:
            if "grades" in json_data:
                for grade in json_data["grades"]:
                    is_exist_grade = app_repository.get_grade(is_exist_student.id, grade["code"])
                    if is_exist_grade:
                        grade_value = (is_exist_grade.value + grade["value"])/2
                        app_repository.change_grade_value(is_exist_student.id, grade["code"], grade_value)
                    else:
                        app_repository.create_grade(is_exist_student.id, grade)
            return is_exist_student.json()            
        
        else:
            student = app_repository.create_student(json_data["name"], json_data["surname"], json_data["stdNumber"] )
            if not student:
                return {"message":"There is a error while creating student"}

            if "grades" in json_data:
                for grade in json_data["grades"]:
                    is_exist_grade = app_repository.get_grade(student.id, grade["code"])
                    if is_exist_grade:
                        grade_value = (is_exist_grade.value + grade["value"])/2
                        app_repository.change_grade_value(student.id, grade["code"], grade_value)
                
                    else:
                        app_repository.create_grade(student.id, grade)

            return student.json()
    return {"errors": form.errors}, 422


def get_student(std_number):
    return app_repository.get_student(std_number).json()

def get_all_student():
    students=  app_repository.get_all_student()
    students_json = [student.json() for student in students] 
    return students_json

    