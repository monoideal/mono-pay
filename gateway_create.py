import requests
import time
from web3.auto import w3
from eth_account.messages import encode_defunct
import secrets
from web3 import Web3
from eth_account import Account
import json
from django.urls import reverse

CONSTANT_PK = 'private key of gateway creator'
#metadata
msg = {
    
}

msg = json.dumps(msg)
massage = encode_defunct(text=msg)
signature = w3.eth.account.sign_message(massage, CONSTANT_PK)

sign = bytes.hex(signature['signature'])

data = {
    'config': 'slug', # slug
    'address': '', # recipient address
    'metadata': msg,
    'amount': 00, # INT 
    'signature': sign, # STR
    'callback':'' # post payment url
}
url = 'PROJECT_BASE_URL/payments/create'
requests.post(url, data)
```