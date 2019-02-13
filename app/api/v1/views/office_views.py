
from flask import Flask, Blueprint, request, make_response, jsonify
from app.api.v1.models import office_model
from app.utils.validator import format_response,validate_office_json_keys,return_error
from app.utils.validator import validate_ints,validate_strings

OFFICE = office_model.Office()

# return all the political parties
office_route = Blueprint('office',__name__,url_prefix='/api/v1/office')

@office_route.route('',methods=['GET'])
def get_offices():
    data = OFFICE.get_offices()
    if data:
        return format_response(200,"request successful",data)
    return format_response(400,"There are no registered political offices")


@office_route.route('/add',methods=['POST'])
def add_office():
  
    # validate json keys
    json_key_errors=validate_office_json_keys(request)

    if json_key_errors:
        return return_error(400, "invalid keys {}".format(json_key_errors))

    try:
        data = request.get_json(force=True)
    except:
        return return_error(400,"wrong input")

    name = data["name"]
    office_type = data["office_type"]

    # validate request data
    if(validate_strings(name) == False):
        return return_error(400,"Name should be of a string data type")
    
    if(validate_strings(office_type) == False):
        return return_error(400, "Office_type should be of a string data type")


    OFFICE.add_office(name, office_type)
    return make_response(jsonify({
        "status":201,
        "data":data
    })),201
    

@office_route.route('/update/<int:office_id>',methods=['PUT'])
def update_office(office_id):

      # validate json keys
    json_key_errors=validate_office_json_keys(request)

    if json_key_errors:
        return return_error(400, "invalid keys")

    try:
        data = request.get_json(force=True)
    except:
        return make_response(jsonify({
            "status":400,
            "message":"wrong input"
        })),400
    id=office_id
    name = data["name"]
    office_type = data["office_type"]
  
     # validate request data
    if(validate_strings(name) == False):
        return return_error(400,"Name should be of a string data type")
    
    if(validate_strings(office_type) == False):
        return return_error(400, "Office_type should be of a string data type")

    office = OFFICE.update_office(id,name,office_type)
    return format_response(200,"updated successfully",office)

@office_route.route('/getoffice/<int:office_id>',methods=['GET'])
def get_party(office_id):

    # validate that id is of type int
    if(validate_ints(office_id) == False):
        return return_error(400,"Wrong Id data type provided")

    data = OFFICE.get_specific_office(office_id)
    if not data:
        return return_error(400,"Data was not found")
    else:

        return format_response(200,"retrieved party successfully",data) 
