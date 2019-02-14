import os
from flask import request,jsonify

from app import create_app

app = create_app('development')

@app.errorhandler(Exception)
def handle_error(e):
    if request.mimetype != 'application/json':
        return jsonify({
            "error":str(e),
            "msg":"data must be of mimetype application/json"
        }),406

if __name__ == '__main__':
    app.run(debug=True)
    