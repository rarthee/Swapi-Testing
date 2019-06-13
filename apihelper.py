import requests
import os
import logging
import wrapt

@wrapt.decorator
def log_args(wrapped, instance, args, kwargs):
    log = logging.getLogger()  # root logger
    log.setLevel(logging.INFO)
    return wrapped(*args, **kwargs)

class Apihelper:

    def __init__(self):
        self.api = "https://swapi.co/api/people"
        self.character_data = {}

    @log_args
    def star_wars_characters(self, page_nr):
        # Get name,height and gender for each character

        return (page_nr['name'],page_nr['height'],page_nr['gender'])


    def append_to_file(self, filepath,name,height,gender):
        with open(filepath, "a")as f:
                f.write(",".join([name,height,gender]))
                f.write("\n")

    def get_results(self):
        response = requests.get(url=self.api)
        results = response.json()['results']
        count = len(response.json()['results'])
        with open(os.getcwd()+"\\data.txt", mode='w') as f:
            print('header')
            f.write("Name")
            f.write(",")
            f.write("Height")
            f.write(",")
            f.write("Gender")
            f.write("\n")
        # get all characters in json
        page_nr_data_list = []
        for i in range(1, count):
            newapi = self.api + "/?page=" + str(i)
            newresponse = requests.get(url=newapi)


            for item in newresponse.json()['results']:
                page_nr_data_list.append(self.star_wars_characters(item))
                self.append_to_file(os.getcwd()+"\\data.txt",item['name'],item['height'],item['gender'])
        return page_nr_data_list




