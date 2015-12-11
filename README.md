# smarter-coffee-api
Python script that acts as a API for a Smarter Coffee machine.

Designed to be used on a RaspberryPi, but could be run on anything with python, and easily be wrapped in a web service to act as a REST API.

Methods:
- One method so far - "brew" passed as the only parameter. It'll respond with success, or the appropriate error message.

Installation:
- It's a simple python script, so just clone the repo to your machine 
- change the IP address to that of your Smarter Coffee machine
- Run it like - "$python smarter-coffee-api.py brew"

Version:
- Very early version - v0.1

ToDo:
- Add more error checking
- Add more methods (cup size, brew strength etc)
- Document example of how to wrap as a web service.
