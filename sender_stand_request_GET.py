import configuration
import requests

from configuration import LOG_MAIN_PATH


#def get_logs():
    #return requests.get(configuration.URL_SERVICE + configuration.LOG_MAIN_PATH,params={"count":20}) _ejercicio1_
#response = get_logs() _ejercicio1_

#print(response.headers) _ejercicio1_
#print(response.status_code) _ejercicio1_

def get_users_table():
    return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH)
response = get_users_table()

print(response.status_code)