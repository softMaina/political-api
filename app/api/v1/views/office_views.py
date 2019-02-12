
from flask import Flask, Blueprint, request, make_response, jsonify
from app.api.v1.models import office_model
from app.utils.validator import format_response

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
  
    try:
        data = request.get_json(force=True)
    except:
        return make_response(jsonify({
            "status":400,
            "message":"wrong input"
        })),400  
    name = data["name"]
    office_type = data["office_type"]

    OFFICE.add_office(name, office_type)
    return make_response(jsonify({
        "status":201,
        "data":data
    })),201
    

@office_route.route('/update/<int:office_id>',methods=['PUT'])
def update_office(office_id):
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
  

    office = OFFICE.update_office(id,name,office_type)
    return format_response(200,"updated successfully",office)

@office_route.route('/getoffice/<int:office_id>',methods=['GET'])
def get_party(office_id):

    data = OFFICE.get_specific_office(office_id)
    if not data:
        return make_response(jsonify({
            'status':400,
            'msg':'data doesnt exists'
        }))
    else:

        return make_response(jsonify({
            'status':200,
            'data':data
        })),200    



# @office_route.route('/delete/<int:office_id>',methods=['DELETE'])
# def delete_office(office_id):
#     OFFICE.delete_office(office_id)
#     return make_response(jsonify({
#         "status":200,
#         "data":[{"message":"sucessful"}]
#     }))
