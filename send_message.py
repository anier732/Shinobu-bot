import os
import requests

# 環境変数からウェブフックURLを取得
webhook_url = os.environ.get('DISCORD_WEBHOOK')

# 送るメッセージ
message = {"content": "胡蝶しのぶの足の裏🦶🏻🦶🏼🦶🏽🦶🏾🦶🏿🦶💨"}

# 送信処理
if webhook_url:
    response = requests.post(webhook_url, json=message)
    print(f"Sent: {response.status_code}")
else:
    print("Error: Webhook URLが設定されていません")
