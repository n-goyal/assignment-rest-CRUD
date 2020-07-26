# University-CRUD
This repository contains assignment files to implement CURD operations over a REST service

# Documentation
## Getting started

This project contains 2 parts, API service & Web Interface.

API service is built using python, Flask and the web interface's backend is using Javascript & frontend using  HTML, CSS and Bootstrap.

***Note**: Web Interface is not fully interated with api service as of now but frontend works fine*

## API: universities

*To run service on your system, Please create a virtual environment and install dependencies from requirement.txt file using command ```pip install -r requirements.txt```*

**Base URL:**
```http://127.0.0.1:5000/universities/```

**Data**
A university JSON Object looks like this:
```
{
    "country": "Viet Nam", 
    "alpha_two_code": "VN", 
    "domain": "tesing.123", 
    "web_page": "http://www.huflit.vnn.vn/", 
    "name": "Ho Chi rajasthan university of Natural 
     Sciences"
}
```
**Operations:** 

```[GET, POST, DELETE, PUT]``` methods are used to implement search, create, update and delete a record in the database.

## Search: To perform search in database using university name
**operation:** GET
**URL:** 
```
http://127.0.0.1:5000/universities/get-details/<string:search_key>/<int:page>
```

**params:** 
```
search_key: String, name of the university
page: Int, page number (default=1), 10 records per page
```
**sample-input**
```
http://127.0.0.1:5000/universities/get-details/Ho Chi rajasthan university of Natural/1
```
**sample-output**
```
{
    "matches": [
        {
            "alpha_two_code": "VN",
            "country": "Viet Nam",
            "domain": "tesing.123",
            "name": "Ho Chi rajasthan university of Natural Sciences",
            "web_page": "http://www.huflit.vnn.vn/"
        }
    ],
    "message": "success",
    "pages": 0,
    "success": true,
    "totalMatches": 1
}
```
**Error Handling**
HTTP 404 will be thrown, incase no records were found

## Get all records
**operation:** GET
**URL:** 
```
http://127.0.0.1:5000/universities/<int:page>
```
**params:** 
```
page: Int, page number (default=1), 10 records per page
```
**sample-input**
```
http://127.0.0.1:5000/universities/1
```
**sample-output**
```
{
    "page": 1,
    "pages": 836,
    "succcess": true,
    "totalUniversities": 8365,
    "universities": [
        {
            "alpha_two_code": "RO",
            "country": "Romania",
            "domain": "uab.ro",
            "name": "1 December University of Alba Iulia",
            "web_page": "http://www.uab.ro/"
        },
        {
            "alpha_two_code": "CN",
            "country": "China",
            "domain": "smmu.edu.cn",
            "name": "2nd Military Medical University",
            "web_page": "http://www.smmu.edu.cn/"
        },
        ...
    ]
}
```
**Error Handling**
HTTP 404 will be thrown, incase no records were found

## delete a record
**operation:** DELETE
**URL:** 
```
http://127.0.0.1:5000/universities/<string:uni_name>/delete-record
```
**params:** 
```
uni_name: String, university name
```
**sample-input**
```
http://127.0.0.1:5000/universities/Ho Chi rajasthan university of Natural Sciences/delete-record
```
**sample-output**
```
{
    "message": "deleted successfully",
    "success": true,
    "university": "Ho Chi rajasthan university of Natural Sciences"
}
```
## update a record
**operation:** PUT
**URL:** 
```
http://127.0.0.1:5000/universities/<string:uni_name>/update

body{
    # Updated JSON Obj
}
```
**params:** 
```
uni_name: String, university name
```
**sample-input**
```
http://127.0.0.1:5000/universities/Ho Chi rajasthan university of Natural Sciences/update

body: {
	"country": "Viet Nam", 
	"alpha_two_code": "VN", 
	"web_page": "http://www.huflit.vnn.vn/", 
	"domain": "UPDATED-DOMAIN", 
	"name": "Ho Chi Minh City University of Natural Sciences"
}
```
**sample-output**
```
{
    "message": "updated successfully",
    "success": true,
    "universityInserted": {
        "alpha_two_code": "VN",
        "country": "Viet Nam",
        "domain": "UPDATED-DOMAIN",
        "name": "Ho Chi Minh City University of Natural Sciences",
        "web_page": "http://www.huflit.vnn.vn/"
    }
}
```
**Error Handling**
HTTP 404 will be thrown, incase no records were found

## create record
**operation:** POST

**URL:** 
```
http://127.0.0.1:5000/universities/create

body{
    # JSON Obj
}
```
**sample-input**
```
http://127.0.0.1:5000/universities/create

body: {
	"country": "Viet Nam", 
	"alpha_two_code": "VN", 
	"web_page": "http://www.huflit.vnn.vn/", 
	"domain": "tesing.123", 
	"name": "Ho Chi Minh City University of Natural Sciences"
}
```
**sample-output**
```
{
    "createdUniversity": {
        "alpha_two_code": "VN",
        "country": "Viet Nam",
        "domain": "tesing.123",
        "name": "Ho Chi Minh City University of Natural Sciences",
        "web_page": "http://www.huflit.vnn.vn/"
    },
    "message": "inserted successfully",
    "success": true
}
```
**Error Handling**
HTTP 400 will be thrown, incase request was not processed

- Apart from the error defined there is addition HTTP 405 is set, incase wrong method is used to send request
