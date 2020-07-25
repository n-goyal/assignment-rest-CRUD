from flask import Flask, request, jsonify, abort
from dataHelper.data_Helper import *

# def createApp(test_config = None):
app = Flask(__name__)
# add_id()

# get json data
@app.route('/')
def index():
    universities = get_all()  # returning JSON
    return jsonify({
        "universities": universities
    })

    # return app

# search university info
@app.route('/search/<search_key>/get-details', methods=['GET'])
def get_university(search_key):
    print(search_key)
    matches = uni_details(search_key)
    return jsonify({
        "matches": matches
    })

# delete university information
@app.route('/universities/<uni_name>/delete-records', methods=['DELETE'])
def delete_university(uni_name):
    print(uni_name)
    result = del_details(uni_name)
    print(result)
    return result

# insert university details
@app.route('/universities/create', methods=['POST'])
def insert_record():
    data = request.get_json()
    result = create_record(data)
    # return incoming
    return jsonify({
        "data": data,
        "status_message": result
    })

# update university details
@app.route('/universities/<uni_name>/update', methods=['PUT'])
def update_details(uni_name):
    data = request.get_json()
    result = update_record(uni_name, data)
    # return jsonify({
    #     "result": result
    # })
    return result

if __name__ == '__main__':
    app.run(debug=True)