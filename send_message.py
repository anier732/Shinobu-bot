import os
import requests

webhook_url = os.environ.get('DISCORD_WEBHOOK')

# 送るメッセージを固定するよ
message = {"content": "胡蝶しのぶの足の裏🦶🏻🦶🏼🦶🏽🦶🏾🦶🏿🦶💨"}

if webhook_url:
    response = requests.post(webhook_url, json=message)
    print(f"Status Code: {response.status_code}")
else:
    print("Webhook URLが設定されていません！")
