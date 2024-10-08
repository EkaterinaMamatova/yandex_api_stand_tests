import configuration
import requests
import data

def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)

user_response = post_new_user(data.user_body)


def post_new_client_kit(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_KIT_NAME,
                         json=body,
                         headers=data.headers_kit)

kit_response = post_new_client_kit(data.kit_body)