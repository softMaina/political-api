import re
from flask import jsonify, make_response


def return_error(status_code, message):
    """ function to format response """
    response = {
        "status":status_code,
        "error": message
    }
    return make_response(jsonify(response),status_code)

def check_is_valid_url(url):
    """check if the url provided is valid"""
    if re.match(r"https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)",
               url):
       return True
    return False

def sanitize_input(input_data):
    """ check if input is of alphanumeric characters """
    if input_data.isalpha() == False:
        return False

def validate_ints(data):
    """ensures that data is of integer data type"""
    if not isinstance(data, int):
        return False
    return True
def validate_strings(data):
    if not isinstance(data, str):
        return False
    return True

def validate_office_json_keys(request):
    request_keys = ["name", "office_type"]
    errors = [] #define an error arror array
    for key in request_keys:
        if not key in request.json:
            errors.append(key)
    return errors

def validate_party_json_keys(request):
    request_keys = ["name","hqaddress","logoUrl"]

    errors = []
    for key in request_keys:
        if not key in request.json:
            errors.append(key)
    return errors

def format_response(status_code, msg, data=list()):

    response = {
        "status":status_code,
        "message": msg,
        "data":data
    }
    return make_response(jsonify(response),status_code)