# django-todo-api 📝
A simple To Do API built with Django and djangorestframework. 

Utilizes ModelViewSet, which abstracts away the method handlers and provides operations or actions instead. URL routing is handled by DefaultRouter. TRULY MAGIC.

## Table of Contents 📑
* [Built with](#built-with)
* [Getting Started](#getting-started)
* [Endpoints](#endpoints)
* [Testing](#testing)

## <a name="built-with"></a>Built with 💻

* Django
* djangorestframework

## <a name="getting-started"></a>Getting Started 🛠

#### Requirements:
- Python 3+
- Django
- djangorestframework

__To run this app on your local computer, please follow the below steps:__

Clone repository.
```
$ git clone https://github.com/janetanne/django-todo-api.git
```

Create and activate a virtual environment.
```
$ python -m venv .env
$ source .env/bin/activate
```

Install the dependencies:
```
$ pip install -r requirements.txt
```

Create a <kbd>secrets.sh</kbd> file that holds your Django secret key:
```
export DJANGO_SECRET="INSERTSECRETKEYHERE"
```

Source your key from <kbd>secrets.sh</kbd> into your virtual environment.
```
$ source secrets.sh
```

Start the server from the command line:
```
$ python manage.py runserver
```

Navigate to 'http://127.0.0.1:8000/' in your browser.

## <a name="Endpoints"></a>Endpoints 👩🏻‍💻

This was built with REST API best practices in mind.

### GET /todos
Returns all todos.

Response:
```
[
    {
        "id": integer,
        "description": string,
        "completed": boolean,
        "created_at": datetime,
        "updated_at": datetime
    },
]
```

### POST /todos
Creates a new todo and returns it. Completed property defaults to False.

Example request:
```
{
  "description":"Finish READme",
  "completed":false
}
```

Response:
```
{
    "id": 5,
    "description": "Finish READme",
    "completed": false,
    "created_at": "2021-03-24T21:39:28.692402Z",
    "updated_at": "2021-03-24T21:39:28.692439Z"
}
```

Error handling:

### PATCH /todos/:id
Updates a todo and returns it. Can change either the "description" or "completed" properties here; does not need both to update the todo.

Example request for todos/5:
```
{
  "completed":true
}
```

Response:
```
{
    "id": 5,
    "description": "Finish READme",
    "completed": true,
    "created_at": "2021-03-24T21:39:28.692402Z",
    "updated_at": "2021-03-24T21:47:13.522333Z"
}
```

Error handling:

### DELETE /todos/:id
Deletes todo and returns nothing. Successful response is HTTP 204 status code.

## <a name="testing"></a>Testing 🧪

will be added soon!
