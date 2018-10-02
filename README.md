# Code Grader
This web application is based on (http://#)[Michael Herman's microservices
tutorial] but has been modified to deploy to Google Cloud Platform instead of
AWS. It also includes infrastructure codified using Terraform and a CI/CD
pipeline to automate the process of deployment.

[Screenshot of final product]

## Development
The development environment was built with `docker 18.03.1`, `docker-compose 1.21.1` and `docker-machine 0.14.0`.

#### Bring Up the App
To run the development server, enter the following command from the root directory of this repo:
```
$ docker-compose -f docker-compose-dev.yml up -d
```

#### Environment Variables
The following environment variables are defined in the appropriate compose file,
either `docker-compose-dev.yml` or `docker-compose-prod.yml`, so if you are
using the `docker-compose` CLI commands describe below you won't need to set
these environment variables on your machine.
- `FLASK_ENV`
- `APP_SETTINGS`
- `DATABASE_URL`
- `DATABASE_TEST_URL`


#### CLI Helper Commands
The following commands may be useful for dev and testing purposes.

- Recreate the database (`drop_all()`, `create_all()`, `commit()`):
```
$ docker-compose -f docker-compose-dev.yml run users python manage.py recreate_db
```
- Seed the database (adds two users):
```
$ docker-compose -f docker-compose-dev.yml run users python manage.py seed_db
```

#### Status Check
To ensure the services and API are us, navigate your browser to `http://localhost:5001/users/ping`
and you should see the following response:
```
{
    "message": "pong!",
    "status": "success"
}
```

#### Unit Tests
To run all unit tests, enter the following command from the root directory of
this repo:
```
$ docker-compose -f docker-compose-dev.yml run users python manage.py test
```

## Deployment
[stuff here]

## RESTful Routes
Endpoint | HTTP Method | CRUD Method | Result
--- | --- | --- | ---
`/users` | GET | READ | get all users
`/users/:id` | GET | READ | get single user
`/users` | POST | CREATE | add a user
