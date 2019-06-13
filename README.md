# SW APITEST 
### https://swapi.co/api/people

This project gets paginated response from the above API and returns a list of character name, height and gender of each Star Wars character.

##Prerequisites
Install python latest version from https://www.python.org/downloads/

##Technologies
Python 3.7.3

### ApiHelper

* This class will access the API and prints the character name , height and gender to a file.
* It has two methods : star_wars_characters returns the list and append_to_file method writes the content to a text file.
* A decorator has been used to the function 'star_wars_characters' to facilitate logging the arguments passed to the function.
* Wrapt module has been used to create the decorators
###Testing
* This is a unittest class that executes the Apihelper class and validates if the returned data is non-empty or not.

## Steps to Execute:
* Git clone the folder "apitest"(Python package) from the repo.
* Execute the python file apihelper_unittest.py (This calls the python file apihelper.py which returns the relevant data and prints data to a text file.)

### PyPI packages 
* pip install requests
* pip install unittest
* pip install wrapt
* pip install logging
* pip install os

##Author
Arthee Raghunathan--Initial work
