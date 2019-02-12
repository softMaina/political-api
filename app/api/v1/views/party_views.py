
from flask import Flask, Blueprint, request, make_response, jsonify
from app.api.v1.models import party_model
from app.utils.validator import sanitize_input,validate_party_json_keys,format_response
PARTY = party_model.Party()

# return all the political parties
party_route = Blueprint('party',__name__,url_prefix='/api/v1/party')
@party_route.route('',methods=['GET'])
def get_parties():
    data = PARTY.get_parties()
    # return make_response(jsonify({
    #     'status':200,
    #     'data':data
    # })),200

    if data:
        return format_response(200,"request was successful",data)
    
    return format_response(400,"There are no registered parties")


@party_route.route('/add',methods=['POST'])
def add_party():
  
    try:
        data = request.get_json(force=True)
    except:
        return make_response(jsonify({
            "status":400,
            "message":"wrong input"
        })),400  
    name = data["name"]
    hqaddress = data["hqaddress"]
    logoUrl = data["logoUrl"]

    party = PARTY.add_party(name, hqaddress,logoUrl)
    if party:
        return format_response(201, "party was created",party)
    return format_response(400,"an error occured")


@party_route.route('/getparty/<int:party_id>',methods=['GET'])
def get_party(party_id):
    data = PARTY.get_specific_party(party_id)
    
    if data:
        return format_response(200,"successfully retrived",data)
    
    return format_response(400,"party with that id wasn't found")


@party_route.route('/update/<int:party_id>',methods=['PUT'])
def update_party(party_id):
    try:
        data = request.get_json(force=True)
    except:
        return format_response(400,"Wrong input, ensure data is in json format")
    id=party_id
    name = data["name"]
    hqaddress = data["hqaddress"]
    logoUrl = data["logoUrl"]

    PARTY.update_party(id,name,hqaddress,logoUrl)
    return make_response(jsonify({
        "status":200,
        "data":data
    })),200

@party_route.route('/delete/<int:party_id>',methods=['DELETE'])
def delete_party(party_id):
    PARTY.delete_party(party_id)
    return make_response(jsonify({
        "status":200,
        "data":[{"message":"sucessful"}]
    }))
