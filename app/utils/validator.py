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