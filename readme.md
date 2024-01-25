# TODO APP

## SETUP AND INSTALLATION

PRE - REQUISITE
1. PYTHON MUST BE INSTALLED
2. POETRY MUST BE INSTALLED OR INSTALL THE DEPENDENCIES FROM PYPOETRY.TOML MANUALLY.

### CLONE THE CODE
```
https://github.com/SkMishra77/Todo.git
```

### SETUP THE POETRY ENV
```
poetry shell
poetry install
```

### SETUP DJANGO PROJECT
```
python manage.py makemigrations
python manage.py migrate
```

### START THE DJANGO SERVER 
```
python manage.py runserver
```
THIS WILL RUN THE CODE AT 
```
http:localhost:8000/
```

# DOCUMENTATION

### REGISTER USER / OUTPUT
```curl
POST http://localhost:8000/api/user/register/
Content-Type: application/json

{
    "email": "sanat123@example.com",
    "name": "SKM",
    "password": "12345678",
    "password2": "12345678"
}
```
```
OUTPUT
{
    "error": false,
    "responseData": "Registration Successful",
    "status_code": 200
}
```

### LOGIN USER / OUTPUT
```curl
POST http://localhost:8000/api/user/login/
Content-Type: application/json

{
    "email": "sanat123@example.com",
    "password": "12345678"
}
```
```
OUTPUT
{
    "error": false,
    "responseData": {
        "token": {
            "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcwODgwNTcxNCwiaWF0IjoxNzA2MjEzNzE0LCJqdGkiOiJhYTBhYjkyNTg1MGY0ODYxYWVmMDRjZjBmYWE5NjcyMiIsInVzZXJfaWQiOiJzYW5hdDEyM0BleGFtcGxlLmNvbSJ9.KATjzaV9PsAw8E85a7G4mEiwzbnEQlpZiXqSrHF2TfY",
            "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzA2MjE3MzE0LCJpYXQiOjE3MDYyMTM3MTQsImp0aSI6IjU5M2JhZTk1ODJhZjQwZGRiZjdiY2JmOThmMWM0ODY3IiwidXNlcl9pZCI6InNhbmF0MTIzQGV4YW1wbGUuY29tIn0.ehNSpLseukyfrfXZyprhkQz-CBWout7XBnZ-mJ-Xujo"
        },
        "msg": "Login Successful"
    },
    "status_code": 200
}
```

### ADD TASK / OUTPUT
```curl
POST http://localhost:8000/api/todo/addTask/
Authorization: Bearer {{auth_token}}
Content-Type: application/json

{
    "title": "TODO",
    "description": "Testing for todo",
    "due_date": "2024-02-01"
}

--> AUTH TOKEN IS JWT TOKEN FROM LOGIN
```
```
OUTPUT
{
    "error": false,
    "responseData": "Task added",
    "status_code": 200
}
```

### UPDATE TASK / OUTPUT
```curl
PATCH http://localhost:8000/api/todo/updateTask/
Content-Type: application/json
Authorization: Bearer {{auth_token}}

{
    "TaskId": "Task_39d6b1681cae2e78bf8d6f5c7fb0730f",
    "status": 1
}

--> TITLE, NAME & STATUS CAN BE UPDATED ONLY
```
```
OUTPUT
{
    "error": false,
    "responseData": "Task updated",
    "status_code": 200
}
```

### DELETE TASK / OUTPUT
```curl
DELETE http://localhost:8000/api/todo/deleteTask/?task_id=Task_d0cccbd037e84a94c6db894eb215099e
Authorization: Bearer {{auth_token}}

--> ADD TASK_ID AS QUERY PARAMS
```
```
OUTPUT
{
    "error": false,
    "responseData": "Task deleted",
    "status_code": 200
}

```

### GET ALL TASK / OUTPUT
```curl
GET http://localhost:8000/api/todo/getAllTasks/
```
```
OUTPUT
{
    "error": false,
    "responseData": [
        {
            "TaskId": "Task_39d6b1681cae2e78bf8d6f5c7fb0730f",
            "title": "TODO",
            "description": "Testing for todo",
            "status_display": "In Progress"
        },
        {
            "TaskId": "Task_0c91ef6b6ca18cd7bd575687c41d5005",
            "title": "TODO",
            "description": "Testing for todo",
            "status_display": "Pending"
        },
        {
            "TaskId": "Task_199fd87765daac41272788217d049638",
            "title": "TODO",
            "description": "Testing for todo",
            "status_display": "Pending"
        },
        {
            "TaskId": "Task_f2568a728548e1f64e75ed2702b907b7",
            "title": "TODO",
            "description": "Testing for todo",
            "status_display": "Pending"
        },
        {
            "TaskId": "Task_c3c37ee4a52478e6065cee57a2c933cd",
            "title": "TODO",
            "description": "Tesing for todo",
            "status_display": "Pending"
        },
        {
            "TaskId": "Task_773e6a396140ef2cb983d88b1ee8d9df",
            "title": "TODO",
            "description": "Tesing for todo",
            "status_display": "Pending"
        }
    ],
    "status_code": 200
}
```

### GET ONE TASK / OUTPUT
```curl
GET http://localhost:8000/api/todo/getTask/?task_id=Task_d0cccbd037e84a94c6db894eb215099e

--> ADD TASK_ID AS QUERY PARAMS
```
```
OUTPUT
{
    "error": false,
    "responseData": {
        "TaskId": "Task_773e6a396140ef2cb983d88b1ee8d9df",
        "title": "TODO",
        "description": "Tesing for todo",
        "status_display": "Pending"
    },
    "status_code": 200
}
```