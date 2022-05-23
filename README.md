# Syndio Backend App

## Requirements
This project requires Python3 be installed on your machine. You can download the latest version at https://www.python.org/downloads/

Install Flask using `pip`. I recommend using a virtual environment if already activated.
```
pip install Flask
```


## Instructions

### Set Port
Set a permanent environment variable `$PORT` to a port number of your choosing. This will be the port used to run your flask app.
Because we will be using separate terminals to run the application and make requests, the environment variable cannot be temporary.

EX.

Edit ```~/.bash_profile``` with a text editor. Use the export command to add the new `PORT` environment variable as shown.
Save changes.

```
PORT=5432
export PORT
```

### Run App
Open a terminal and navigate to the project path `/backend-engineer-app`.

Run the following to start the Flask application.

```
export FLASK_APP=app.py
python -m flask run -h localhost -p $PORT
```

You should see this in your terminal
```
 * Serving Flask app 'app.py' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://localhost:5432 (Press CTRL+C to quit)
```

### Request
In a separate terminal, type the following command:
```
curl localhost:$PORT/employees
```

### Result
```
[
    {
        "gender": "male",
        "id": 1
    },
    {
        "gender": "male",
        "id": 2
    },
    {
        "gender": "male",
        "id": 3
    },
    {
        "gender": "female",
        "id": 4
    },
    {
        "gender": "female",
        "id": 5
    },
    {
        "gender": "female",
        "id": 6
    }
]
```
