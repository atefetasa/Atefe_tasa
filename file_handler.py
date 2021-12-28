import os
import json
import log


def search_in_file(file_name,key,value):
    search_results=[]
    try:
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
        else:
            raise ValueError(f"the {file_name} file does not exist.")
    except ValueError as e:
        print(e)
        log.warning_logger.error(e)
    except Exception as e:
        print(e)
        log.warning_logger.error(e)







