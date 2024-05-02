import requests
import math
import time
from datetime import datetime
import json

webhook_url = ""

with open("modules/url.json") as file:
    webhook_url = json.loads(file.read())["url"]

def get_emoji(status):
    if status: return "✅"
    return "❌"

def send_status_webhook(status):
    current_datetime = datetime.now()
    formatted_datetime = current_datetime.strftime("%d/%m/%Y %H:%M")
    payload = {
                "content": "",
                "tts": False,
                "embeds": [
                    {
                    "id": 652627557,
                    "title": "Blockcoin Status",
                    "color": 12059647,
                    "fields": [
                        {
                        "id": 677117560,
                        "name": "Blockcoin",
                        "value": f'[Blockcoin](https://blockcoin.social): `{get_emoji(status["Blockcoin"]["success"])} {status["Blockcoin"]["code"]} {status["Blockcoin"]["time"]}ms`\n[Blockcoin Beta](https://beta.blockcoin.social): `{get_emoji(status["Blockcoin Beta"]["success"])} {status["Blockcoin Beta"]["code"]} {status["Blockcoin Beta"]["time"]}ms`',
                        "inline": False
                        },
                        {
                        "id": 648664888,
                        "name": "Tatom",
                        "value": f'[Tatom](https://tatom.herasium.dev): `{get_emoji(status["Tatom"]["success"])} {status["Tatom"]["code"]} {status["Tatom"]["time"]}ms`\n[Tatom Auth](https://auth.tatom.herasium.dev): `{get_emoji(status["Tatom Auth"]["success"])} {status["Tatom Auth"]["code"]} {status["Tatom Auth"]["time"]}ms`',
                        "inline": False
                        }
                    ],      
                    "footer": {
                        "text": f"Blockcoin's Status, current: {formatted_datetime}. Update every 5 mins."
                    }
                    }
                ],
                "components": [],
                "actions": {}
            }
    response = requests.post(webhook_url+"?wait=true", json=payload)
    return response.json()["id"]

def delete_id(id):
    response = requests.delete(webhook_url+f"/messages/{id}")