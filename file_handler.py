import os
import json


def search_in_file(file_name,key,value):
    search_results=[]
    if os.path.exists(file_name):
        with open(file_name,'r') as myfile:
            data = json.load(myfile)
            for dictionary in data:
                if dictionary[key] == value:
                    search_results.append(dictionary)
        if search_results:
            return search_results
        else:
            return None







