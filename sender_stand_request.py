import configuration
import requests
import data

def get_user_body(user_body):
    return requests.post(configuration.URL_SERVICE + configuration.MAIN_USER,
                         json=user_body,
                         headers=data.headers)
response = get_user_body(data.user_body)
print(response.status_code)