#Импорт библиотек
import json
from datetime import datetime
import hashlib
import hmac
import requests
from random import randint

class PayUApi:
    def __init__(self, MERCHANT_ORDER_REF):
        self.PAYU_MERCHANT_CODE = "CC1" # Код мерчанта
        self.PAYU_SECRET_KEY = "SECRET_KEY" # Ключ API 
        self.request_method = "POST/api/v4/payments/authorize"
        self.HOST_BASE_URL = "https://sandbox.ypmn.ru" # test EndPoint
        #self.HOST_BASE_URL = "https://secure.ypmn.ru" # prod EndPoint
        self.MERCHANT_ORDER_REFERENCE = MERCHANT_ORDER_REF

    ##формирование даты
    def data_time(self):
        today = datetime.now()
        today2 = today.now().astimezone().replace(microsecond=0).isoformat()
        REQUEST_DATE = str(today2)
        return REQUEST_DATE
    
    ##формирование контрольной суммы MD5
    def calcMD5(self, body):
        md5_hash = hashlib.md5(str(body).encode('utf-8')).hexdigest()
        return md5_hash

    ##формирование строки для хэширования
    def calcstrMD5(self, hashing_string, REQUEST_DATE):
        md5_hash2 = self.PAYU_MERCHANT_CODE + REQUEST_DATE + self.request_method + str(hashing_string)
        md5_hash2 = md5_hash2.encode('utf-8')
        return md5_hash2
    
    ##формирование signature, sha256
    def calc_signature(self, md5_hash2):
        API_SIGNATURE = hmac.new(self.PAYU_SECRET_KEY.encode('utf-8'), msg=md5_hash2, digestmod=hashlib.sha256).hexdigest()
        return API_SIGNATURE
    
    ##формирование заголовка запроса
    def generate_headers(self, API_SIGNATURE, REQUEST_DATE):
        headers = {
            "Accept": "application/json",
            "X-Header-Signature": API_SIGNATURE,
            "X-Header-Merchant": self.PAYU_MERCHANT_CODE,
            "X-Header-Date": REQUEST_DATE,
            "Content-Type": "application/json"
        }
        return headers

    ##формирование тела запроса
    def generate_request_body(self, products):
        request_body = {
            "merchantPaymentReference": self.MERCHANT_ORDER_REFERENCE,
            "currency": "RUB",
            "returnUrl": f"{self.HOST_BASE_URL}/backend/simulators/return.php",
            "authorization": {
                "paymentMethod": "CCVISAMC",
                "cardDetails": {
                    "number": "4652035440667037",
                    "expiryMonth": "08",
                    "expiryYear": "2025",
                    "cvv": "971",
                    "owner": "John Doe"
                }
            },
            "client": {
                "billing": {
                    "firstName": "John",
                    "lastName": "Doe",
                    "compayIdType": "PERSONALID",
                    "compayId": "123445",
                    "email": "test@payu.ro",
                    "phone": "0771346934",
                    "city": "Bucharest",
                    "countryCode": "RO",
                    "state": "Bucharest",
                    "companyName": "PayU",
                    "taxId": "example",
                    "addressLine1": "example",
                    "addressLine2": "example",
                    "zipCode": "example",
                    "identityDocument": {
                        "number": "12345",
                        "type": "PERSONALID"
                    }
                },
                "delivery": {
                    "firstName": "John",
                    "lastName": "Doe",
                    "phone": "40898625",
                    "addressLine1": "example",
                    "addressLine2": "example",
                    "zipCode": "example",
                    "city": "Bucharest",
                    "state": "Bucharest",
                    "countryCode": "RO",
                    "email": "name@example.com"
                },
                "clientIp": "127.0.0.1",
                "clientTime": "TEST"
            },
            "products": products
        }
        return json.dumps(request_body)
    
    ##формирование запроса
    def fun_authorize(self, headers, request_body):
        url = self.HOST_BASE_URL + '/api/v4/payments/authorize'
        response = requests.post(url, data=request_body, headers=headers, timeout=10)
        response_dict = response.json()
        
        return response_dict
