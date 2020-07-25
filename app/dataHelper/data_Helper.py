import json

'''
template JSON object:
{
    "alpha_two_code": "US",
    "country": "United States",
    "domain": "acu.edu",
    "name": "Abilene Christian University",
    "web_page": "http://www.acu.edu/"
}
'''
# read JSON

jsonFile = open('universities.json')
jsonData = json.load(jsonFile)
jsonFile.close()

# index
def get_all():
    return jsonData

# GET - Search
def uni_details(search_key):
    matches = []
    for obj in jsonData:
        if search_key in obj['name']:
            matches.append(obj)
    # matches = [value for key, value in data.items() if name in key]
    return matches

# DELETE - Record
def del_details(uni_name, data=jsonData):
    x = len(data)
    data = [obj for obj in data if obj['name'] != uni_name]
    y = len(data)
    if x != y:
        # data = json.dumps(cleanData)
        with open("universities.json","w") as jsonFile:
            json.dump(data, jsonFile)
        return 'Success'
    else:
        return 'No record was found'

# CREATE - Record
def create_record(record):
    jsonData.append(record)
    with open("universities.json", "w") as jsonFile:
        json.dump(jsonData, jsonFile)
    return 'Inserted Successfully'

# UPDATE - Record
def update_record(uni_name, data):
        # update any matching articles
    for obj in jsonData:
        if obj['name'] == uni_name:
            obj['alpha_two_code'] = data['alpha_two_code']
            obj['country'] = data['country']
            obj['domain'] = data['domain']
            obj['name'] = data['name']
            obj['web_page'] = data['web_page']
            break

    # rewrite the whole JSON file with updated dictionary
    with open("universities.json", "w") as jsonFile:
        json.dump(jsonData, jsonFile)

    return 'Updated Successfully'

# testing purpose
if __name__=='__main__':
    # get_all()
    print(len(jsonData))
    # print(del_details('Ho Chi Minh City University of Natural Sciences'))
    # print(update_record("Ho Chi Minh City University of Natural Sciences", {
    #     "country": "Viet Nam", 
    #     "alpha_two_code": "VN", 
    #     "web_page": "http://www.CHANIGN.vnn.vn/", 
    #     "domain": "huflit.vnn.vn", 
    #     "name": "Ho Chi Minh City University of Natural Sciences"}))
    print(len(jsonData))