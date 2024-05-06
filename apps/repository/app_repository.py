from app import db
from models import Student, Grade

def create_student(name, surname, std_number):
    student = Student(name=name, surname = surname, std_number=std_number)
    db.session.add(student)
    db.session.commit()

    return student

def get_student(std_number):
    student = db.session.query(Student).where(Student.std_number == std_number).first()
    return student

def get_all_student():
    students = db.session.query(Student).all()
    return students

def create_grade(student_id, grade):
    grade = Grade(student_id=student_id , code = grade["code"],value=grade["value"])
    db.session.add(grade)
    db.session.commit()
    return grade

def get_grade(student_id,code):
    grade = db.session.query(Grade).where(Grade.student_id == student_id,Grade.code == code ).first()
    return grade

def change_grade_value(student_id,code,value):
    grade = db.session.query(Grade).where(Grade.student_id == student_id,Grade.code == code ).first()
    grade.value = value
    db.session.commit()
    return grade
