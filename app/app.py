from flask import Flask, request, jsonify, abort
from dataHelper.data_Helper import *

app = Flask(__name__)

# get json data
@app.route('/')
def index():
    universities = get_all()  # returning JSON
    # add pagination
    return jsonify({
        "succcess": True,
        "universities": universities,
        "totalUniversities": len(universities)
    }), 200

# search university info: <key: Name>
@app.route('/universities/<search_key>/get-details', methods=['GET'])
def get_university(search_key):
    print(search_key)
    matches = uni_details(search_key)

    if matches is None:
        abort(404)

    else:
        # add pagination
        return jsonify({
            "success": True
            "matches": matches
            "totalMatches": len(matches)
        }), 200

# delete university information
@app.route('/universities/<uni_name>/delete-record', methods=['DELETE'])
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
            "message": result
        }), 200
    else:
        abort(400)

# update university details
@app.route('/universities/<uni_name>/update', methods=['PUT'])
def update_details(uni_name):
    data = request.get_json()
    updated = update_record(uni_name, data)

    if updated:
        return jsonify({
            "success": True,
            "universityInserted": data,
            "message": "inserted successfully"
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