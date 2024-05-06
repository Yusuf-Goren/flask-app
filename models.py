from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String, ForeignKey, UniqueConstraint
   
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List

db = SQLAlchemy()

class Student(db.Model):
    __tablename__ = 'students'

    id:Mapped[str] = mapped_column(Integer, primary_key=True)
    std_number:Mapped[str] = mapped_column(String(10), unique=True)
    name:Mapped[str] = mapped_column(String(80), nullable=False)
    surname:Mapped[str] = mapped_column(String(80), nullable=False)
    grades: Mapped[List["Grade"]] = relationship("Grade", back_populates="student",lazy="selectin", viewonly=True) 

    def json(self):
        grades_json = [grade.json() for grade in self.grades] 
        return {'std_number': self.std_number, 'name': self.name, 'surname': self.surname, "grade":grades_json }

class Grade(db.Model):
    __tablename__ = 'grades'
   
    id:Mapped[int]  = mapped_column(Integer, primary_key=True)
    code:Mapped[str]  = mapped_column(String(80), nullable=False)
    value:Mapped[int] = mapped_column(Integer, nullable=False)
    student_id:Mapped[int] = mapped_column(ForeignKey("students.id", ondelete="CASCADE"))
    student:Mapped[Student] = relationship("Student", back_populates="grades")

    def json(self):
        return {  'code': self.code, 'value': self.value}
