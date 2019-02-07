
from flask import Flask, Blueprint, request, make_response, jsonify
from app.api.v1.models import office_model

OFFICE = office_model.Office()

# return all the political parties
office_route = Blueprint('office',__name__,url_prefix='/api/v1/office')
@office_route.route('',methods=['GET'])
def get_offices():
    data = OFFICE.get_offices()
    return make_response(jsonify({
        'status':200,
        'data':[{"party":data}]
    })),200

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
        "data":[{"message":"success"}]
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
  

    OFFICE.update_office(id,name,office_type)
    return make_response(jsonify({
        "status":200,
        "data":[{"message":"success"}]
    })),200

# @office_route.route('/delete/<int:office_id>',methods=['DELETE'])
# def delete_office(office_id):
#     OFFICE.delete_office(office_id)
#     return make_response(jsonify({
#         "status":200,
#         "data":[{"message":"sucessful"}]
#     }))
