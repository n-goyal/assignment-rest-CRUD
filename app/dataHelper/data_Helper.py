import json

'''
{
    "alpha_two_code": "US",
    "country": "United States",
    "domain": "acu.edu",
    "name": "Abilene Christian University",
    "web_page": "http://www.acu.edu/"
}
'''

# class University:
#     def __init__(self, alphaCode, country, domain, name, web):
#         self.alphaCode = alphaCode
#         self.country = country
#         self.domain = domain
#         self.name = name 
#         self.web = web



jsonFile = open('universities.json')
jsonData = json.load(jsonFile)
jsonFile.close()

'''
data = 
[
    {
        id: 1,
        uni:{

        }
    }
]
'''

# def add_id():
#     print(len(jsonData))
#     # assign Id to each object with name
#     for i in range(len(jsonData)):
#         data[jsonData[i]['name']] = jsonData[i]
#     search = ''
#     return data


# index
def get_all():
    return jsonData

# Search - GET
def uni_details(search_key):
    # print(data.keys())
    matches = []
    for i in range(len(jsonData)):
        if search_key in jsonData[i]['name']:
            matches.append(jsonData[i])
    # matches = [value for key, value in data.items() if name in key]
    return matches

# delete - Record
def del_details(name):
    # remove element from data and jsonData
    # save new json file
    return ''


if __name__=='__main__':
    # print(getJSON())
    # print(len(jsonData))
    print(json)
    # print(len(getUniversity('Ad')))
    # print(addId())