import requests
import os

webhook_url = os.environ['DISCORD_WEBHOOK']
message = "胡蝶しのぶの足の裏🦶🏻🦶🏼🦶🏽🦶🏾🦶🏿🦶💨"

requests.post(webhook_url, json={"content": message})
