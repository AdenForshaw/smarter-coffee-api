# smarter-coffee-api
Python script that acts as a API for a Smarter Coffee machine.

Designed to be used on a RaspberryPi, but could be run on anything with python, and easily be wrapped in a web service.

One method so far - "brew" passed as the only parameter.

Installation:
- A simple python script, 
- Install and change the IP address to that of the Smarter Coffee machine
- Run - "$python smarter-coffee-api.py brew"

Very early version - v0.1

ToDo:
- Add more error checking
- Add more methods (cup size, brew strength etc)
- Document example of how to wrap as a web service.
