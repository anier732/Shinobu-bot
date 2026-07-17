import os
import requests

webhook_url = os.environ.get('DISCORD_WEBHOOK')
message = {"content": "しのぶボットが起動したよ！"}

if webhook_url:
    response = requests.post(webhook_url, json=message)
    print(f"Status Code: {response.status_code}")
else:
    print("Webhook URLが設定されていません！")
