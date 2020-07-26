from flask import Flask, request, jsonify, abort
from flask_cors import CORS, cross_origin
from dataHelper.data_Helper import *

app = Flask(__name__)
CORS(app)

@app.after_request # blueprint can also be app~~
def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-type, Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET, PUT, POST, DELETE')
    return response

# get json data
@app.route('/universities/<string:code>/<int:page>', methods=['GET'])
@cross_origin(origins='*')
def index(page = 1, code=''):
    if(code!=''):
        universities = sorted(filter_all(code), key = lambda i: i['name']) # returning JSON
    else:
        universities = sorted(get_all(), key = lambda i: i['name'])  # returning JSON
    if(len(universities)!=0):
        # add pagination
        offset = 10
        start = (page - 1) * offset
        end = start + offset
        noPages = round(len(universities)/offset)
        return jsonify({
            "succcess": True,
            "universities": universities[start:end],
            "pages": noPages,
            "page": page,
            "totalUniversities": len(universities)
        }), 200
    else:
        abort(404)

# search university info: <key: Name>
@app.route('/universities/get-details/<string:search_key>/<int:page>', methods=['GET'])
def get_university(search_key, page = 1):
    print(search_key)
    matches = uni_details(search_key)

    if matches is None:
        abort(404)
    else:
        # add pagination
        output = sorted(matches, key = lambda i: i['name'])  # returning JSON
        offset = 10
        start = (page - 1) * offset
        end = start + offset
        noPages = round(len(matches)/offset)
        return jsonify({
            "success": True,
            "totalMatches": len(matches),
            "pages": noPages,
            "matches": output[start:end],
            "message": "success"
        }), 200

# delete university information
@app.route('/universities/<string:uni_name>/delete-record', methods=['DELETE'])
def delete_university(uni_name):
    # print(uni_name)
    result = del_details(uni_name)

    if result:
        return jsonify({
            "success": True,
            "university": uni_name,
            "message": "deleted successfully"
        }), 200
    else:
        abort(404)

# insert new university details
@app.route('/universities/create', methods=['POST'])
def insert_record():
    data = request.get_json()
    inserted = create_record(data)

    if inserted:
        return jsonify({
            "success": True,
            "createdUniversity": data,
            "message": "inserted successfully"
        }), 200
    else:
        abort(400)

# update university details
@app.route('/universities/<string:uni_name>/update', methods=['PUT'])
def update_details(uni_name):
    data = request.get_json()
    updated = update_record(uni_name, data)

    if updated:
        return jsonify({
            "success": True,
            "universityInserted": data,
            "message": "updated successfully"
        }), 200
    else:
        abort(400)

'''
ERROR HANDLING
'''
@app.errorhandler(404)
def notFound(error):
    return jsonify({
        "success": False,
        "error": 404,
        "message": "record not found"
    }), 404


@app.errorhandler(400)
def notFound(error):
    return jsonify({
        "success": False,
        "error": 400,
        "message": "bad request"
    }), 400


@app.errorhandler(405)
def unprocessable(error):
    return jsonify({
        "success": False,
        "error": 405,
        "message": "method not allowed"
    }), 405

if __name__ == '__main__':
    app.run(debug=True)