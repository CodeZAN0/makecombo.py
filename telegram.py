import requests

token = "6721323145:AAGjqUY9hn9_mS0yBFFCfe9M40mf_U30dGs"

chat_id = "1235034767"

message = "hi"


url1 = "https://api.telegram.org/bot{token}/getUpdates"

url = "https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}"

print(requests.get(url).json())