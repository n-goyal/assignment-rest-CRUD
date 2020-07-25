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
@app.route('/search')
def getUniversity():
    search_key = request.args['name']
    matches = uni_details(search_key)
    return jsonify({
        "matches": matches
    })

# delete university information
# @app.route('/universities/<uni_name>', methods=['DELETE']):
# def delete_university 


if __name__ == '__main__':
    app.run(debug=True)