import os
import requests
import json

token = os.getenv('TELE_TOKEN')#터미널에 설정해놓은 TELE_TOKEN값을 가져옴
method = 'getUpdates'

#token이 보이면 안되므로 환경변수에 저장할 것
url = "https://api.telegram.org/bot{}/{}".format(token,method)

#c9에서는 블랙리스트로 되어 있어서 안됨
#local에서는 되지만 이곳에서는 안되므로 우회하여 진행
url = "https://api.hphk.io/telegram/bot{}/{}".format(token,method)

res = requests.get(url).text
data = json.loads(res,encoding="UTF-8")

user_id = data["result"][0]["message"]["from"]["id"]
msg = "Hello"

method = 'sendMessage'

msg_url = "https://api.hphk.io/telegram/bot{}/{}?chat_id={}&text={}".format(token,method,user_id,msg)

requests.get(msg_url)