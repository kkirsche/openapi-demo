# OpenAPI Demonstration Application

This application is designed to assist with learning how to work with the OpenAPI standard.

## Usage

To use the application locally, the following commands (prefixed by `$` to indicate that these should be run from a terminal):

```shell
$ python3 -m venv venv
$ source ./venv/bin/activate
$ python3 -m pip -r requirements.txt
$ export FLASK_APP=main.py
$ flask run
```

This will begin the application on port 5000 bound to localhost (127.0.0.1).

## Endpoints

This application exposes the following endpoints on the host running the application:

* `GET /api/v1/fighters` - List fighters
* `GET /api/v1/fighters/{id}` - Show fighter
* `POST /api/v1/fighters` - Create fighter
* `PUT /api/v1/fighters/{id}` - Update fighter
* `DELETE /api/v1/fighters/{id}` - Destroy fighter

## Structures
### Fighter

A fighter includes the following information:

* `id` - The numeric ID representing the entry
* `name` - The fighter's name
* `weightclass` - The fighter's weightclass

An example of a fighter would be:

```json
{
  "id": 1,
  "name": "Jon Jones",
  "weightclass": "Light heavyweight (205 lbs)"
}
```

### Error

An error includes the following information:

* `error` - The error message

An example of an error would be:

```json
{
  "error": "404 - Not Found"
}
```
