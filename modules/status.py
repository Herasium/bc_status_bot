import requests
import time
import math

url = {
    "Blockcoin": "https://blockcoin.social",
    "Blockcoin Beta":"https://beta.blockcoin.social",
    "Tatom":"https://tatom.herasium.dev",
    "Tatom Auth":"https://auth.tatom.herasium.dev"
}
def get_status():

    status = {}

    for i in url:
        try:
            start_time = time.time()
            r = requests.get(url[i])
            end_time = time.time()
            elapsed_time = end_time - start_time
            status[i] = {
                "name":i,
                "code":r.status_code,
                "success":r.status_code == 200,
                "time":math.floor(elapsed_time*1000)
            }
        except:
            status[i] = {
                "name":i,
                "code":"???",
                "success":False,
                "time":"???"
            }
    return status

get_status()