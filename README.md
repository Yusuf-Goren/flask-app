## flask backend with postgres

to Run application open docker and then open a terminal in porject folder type in
`docker compose up --build flask_app`

## avaliable routes

/create
example body
`
{
"surname":"474",
"name":" 8888",
"stdNumber":"588",
"grades": [
{
"code": "R2",
"value": 40
},
{
"code": "R3",
"value": 50
}
]
}
`

/get-student/<student_id>

/get-students
