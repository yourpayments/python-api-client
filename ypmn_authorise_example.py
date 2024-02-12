from ypmn_classes import PayUApi
import json
from datetime import datetime
import hashlib
import hmac
import requests
from random import randint

MERCH_ORDER_REF = str(randint(1, 10000))
payu_api = PayUApi(MERCH_ORDER_REF)
products = [
    {"name":"test1", 
     "sku":"123456", 
     "unitPrice":"1000", 
     "quantity":"1", 
     "additionalDetails":"string"},
    {"name":"test2", 
     "sku":"654321", 
     "unitPrice":"200",
     "quantity":"5", 
     "additionalDetails":"string"}
]
request_body = payu_api.generate_request_body(products)
#print(request_body)

REQUEST_DATE = payu_api.data_time()
md5_hash = payu_api.calcMD5(request_body)
#print(md5_hash)

md5_hash2 = payu_api.calcstrMD5(md5_hash, REQUEST_DATE)
#print(md5_hash2)

API_SIGNATURE = payu_api.calc_signature(md5_hash2)
header = payu_api.generate_headers(API_SIGNATURE, REQUEST_DATE)
#print(header)

response_dict = payu_api.fun_authorize(header, request_body)
print(json.dumps(response_dict, indent=4))