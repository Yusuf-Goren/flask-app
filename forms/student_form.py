from wtforms import Form, BooleanField, StringField, PasswordField, validators

class StudentForm(Form):
    name = StringField('Name', [validators.input_required(message="Name is required"), validators.Length(min=3, max=80 , message="Surname name be more than 80 characters")])
    surname = StringField('Surname', [validators.input_required(message="Surname is required") ,validators.Length(min=2, max=80, message="Surname cant be more than 80 characters")])
    stdNumber = StringField('Student Number', [validators.input_required(message="Student Number is required") ,validators.Length(min=2, max=10, message="Student Number cant be more than 10 characters")])
