import configuration
import data
import requests

#Metodos GET



#Metodos POST
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)

def create_new_kit(body_kit):
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json=body_kit,
                         headers=data.headers)