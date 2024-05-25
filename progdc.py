import requests
import os, uuid

url = "https://api.warpcast.com/v2/ext-send-direct-cast"
api_key = os.getenv("WARPCAST_API_KEY")
print(api_key)

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

gen_uuid = uuid.uuid4()
msgTxt = "What's up?"

data = {
    "recipientFid": 6846,
    "message": msgTxt,
    "idempotencyKey": "ed3d9b95-5eed-475f-9c7d-58bdc3b9ac00" 
}

response = requests.put(url, headers=headers, json=data)

print(response.status_code)
print(response.text)
