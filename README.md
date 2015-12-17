# smarter-coffee-api
Python script that acts as an Unofficial API for a Smarter Coffee machine - http://smarter.am/coffee/

Designed to be used on a RaspberryPi, but could be run on anything with python, and easily be wrapped in a web service to act as a REST API.

Basic installation guide: http://adenforshaw.com/smarter-coffee-machine-raspberry-pi-iot-coffeetime/

Methods: a string passed as the only parameter.
- "reset" - resets the machine to default settings. Useful to test with and saves your beans.
- "brew" - Starts brewing with current settings. It'll respond with success, or the appropriate error message.

Response:
JSON - { code:String, success:Boolean, message:String }

Installation:
- Clone the repo to your machine
- Edit the IP address to that of your Smarter Coffee machine
- Call from the command line e.g. $python smarter-coffee-api.py brew

Version:
- Very early version - v0.1

ToDo:
- Add more error checking
- Add more methods (cup size, brew strength etc)
- Document example of how to wrap as a web service.
