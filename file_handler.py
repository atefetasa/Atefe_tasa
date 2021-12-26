import os
import json
import logging
logging.basicConfig(filename='logfile.log',filemode='w',level=logging.DEBUG,format='%(levelname)s:%(asctime)s:%(message)s')


def search_in_file(file_name,key,value):
    search_results=[]
    if os.path.exists(file_name):
        logging.info(f"the {file_name} file exists.")
        with open(file_name,'r') as myfile:
            data = json.load(myfile)
            for dictionary in data:
                if dictionary[key] == value:
                    search_results.append(dictionary)
        if search_results:
            logging.info("the search has some results")
            return search_results
        else:
            logging.info("the search had no results.")
            return None







