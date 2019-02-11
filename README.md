[![Build Status](https://travis-ci.org/softMaina/political-api.svg?branch=develop)](https://travis-ci.org/softMaina/political-api)
[![Maintainability](https://api.codeclimate.com/v1/badges/95ebc6a5f1ce41b4ca0e/maintainability)](https://codeclimate.com/github/softMaina/political-api/maintainability)
[![Coverage Status](https://coveralls.io/repos/github/softMaina/political-api/badge.svg?branch=develop)](https://coveralls.io/github/softMaina/political-api?branch=develop)
# political-api

This is an application to help electral commisions to register voters and politicians online and carry out the voting exercise

## EndPoints

| Http method  | EndPoint | Functionality |
| ------------- | ------------- |---------|
| Get  | api/v1/office  | used by user and admin to get all offices |
| Post  | api/v1/office/add  | used by admin to add office |
| Put | api/v1/office/update/:id | used by admin to update office|
| Get | api/v1/party | used by admin and user to get all parties |
| Post | api/v1/party/add | used by admin to add new party |
| Put | api/v1/party/update/:id | used by admin to patch a party |
| Delete | api/v1/party/delete/:id | used by admin to delete a party |

## Installing The Application
- 1. open terminal in your preferred folder
- 2. clone this repo `git clone https://github.com/softMaina/political-api.git` to have a copy locally
- 3. `cd political-api`
- 4. create a virtual environment for the repo `virtualenv venv`
- 5. Install dependencies from the requirements.txt file `pip3 install -r requirements.txt`
- 6. Export environment variables to your environment `export FLASK_APP="run.py"`
- 7. Run the application using flask command `flask run` or `using python3 python3 run.py`

## Running tests
Inside the virtual environment created above, run command: `coverage run --source=app.api.v1 -m pytest app/tests/v1 -v -W error::UserWarning && coverage report`

## Technologies used
- 1. Pytests for running tests
- 2. Flask python framework

## Deployment
 (https://political-api-v1.herokuapp.com)

## Author
Allan Maina

## Credits
This api was build as a part of andela cycle 37 challenge
