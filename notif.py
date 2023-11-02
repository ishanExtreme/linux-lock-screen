import requests

from config import PUSHOVER_TOKEN, PUSHOVER_USER, PUSHOVER_DEVICE

url = "https://api.pushover.net/1/messages.json"


def send_notification(title, message):
  payload = {'user': PUSHOVER_USER,
  'token': PUSHOVER_TOKEN,
  'priority': '0',
  'title': title,
  'message': message,
  'device': PUSHOVER_DEVICE}
  files=[

  ]
  headers = {}

  requests.request("POST", url, headers=headers, data=payload, files=files)
