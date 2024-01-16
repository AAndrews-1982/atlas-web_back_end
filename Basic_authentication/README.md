# Basic authentication

### Background Context

In this project, you will learn what the authentication process means and implement a Basic Authentication on a simple API.

In the industry, you should not implement your own Basic authentication system and use a module or framework that doing it for you (like in Python-Flask: Flask-HTTPAuth Link: https://flask-httpauth.readthedocs.io/en/latest/).

Here, for the learning purpose, we will walk through each step of this mechanism to understand it by doing.

![6ccb363443a8f301bc2bc38d7a08e9650117de7c](https://github.com/AAndrews-1982/atlas-web_back_end/assets/116847683/0537beba-b8bb-4f02-a445-8401faeba83b)

# Resources
Read or watch:

#### REST API Authentication Mechanisms
Link: https://www.youtube.com/watch?v=501dpx2IjGY
#### Base64 in Python
Link: https://docs.python.org/3.7/library/base64.html
#### HTTP header Authorization
Link: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Authorization
#### Flask
Link: https://palletsprojects.com/p/flask/
#### Base64 - concept
Link: https://en.wikipedia.org/wiki/Base64

# Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

- General
- What authentication means
- What Base64 is
- How to encode a string in Base64
- What Basic authentication means
- How to send the Authorization header

# Requirements

### Python Scripts

- All your files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7)
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/env python3
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle style (version 2.5)
- All your files must be executable
- The length of your files will be tested using wc
- All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
- All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
- All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

Tasks
0. Simple-basic-API
mandatory
Download and start your project from this archive.zip

In this archive, you will find a simple API with one model: User. Storage of these users is done via a serialization/deserialization in files.

Setup and start server
bob@dylan:~$ pip3 install -r requirements.txt
...
bob@dylan:~$
bob@dylan:~$ API_HOST=0.0.0.0 API_PORT=5000 python3 -m api.v1.app
 * Serving Flask app "app" (lazy loading)
...
bob@dylan:~$
Use the API (in another tab or in your browser)
bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/status" -vvv
*   Trying 0.0.0.0...
* TCP_NODELAY set
* Connected to 0.0.0.0 (127.0.0.1) port 5000 (#0)
> GET /api/v1/status HTTP/1.1
> Host: 0.0.0.0:5000
> User-Agent: curl/7.54.0
> Accept: */*
> 
* HTTP 1.0, assume close after body
< HTTP/1.0 200 OK
< Content-Type: application/json
< Content-Length: 16
< Access-Control-Allow-Origin: *
< Server: Werkzeug/1.0.1 Python/3.7.5
< Date: Mon, 18 May 2020 20:29:21 GMT
< 
{"status":"OK"}
* Closing connection 0
bob@dylan:~$
Repo:
