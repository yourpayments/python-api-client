from datetime import datetime
import hashlib
import hmac
import requests
from random import randint
import json

with open('configs.json', 'r') as file:
      data = json.load(file) 

class YPMNApi:

    """
    Класс в который входят все основные функции:
    1) data_time() - функция формирования даты, необходима для формирования подписи 
        - не принимает аргументов на вход
    2) calcMD5(body) - функция формирования контрольной суммы MD5, необходима для формирования подписи 
        - принимает на вход аргумент body, в котором храниться тело запроса
    3) calcstrMD5(hashing_string, REQUEST_DATE) - функция формирования строки для хэширования, необходима для формирования подписи 
        - принимает на вход аргумент hashing_string, в котором храниться результат выполнения функции calcMD5()
        - принимает на вход аргумент REQUEST_DATE, в котором храниться результат выполнения функции data_time()
    4) calc_signature(md5_hash2) - функция формирования подписи, необходимо указывать в заголовке запроса 
        - принимает на вход аргумент md5_hash2, в котором храниться результат выполнения функции calcstrMD5()
    5) generate_headers(API_SIGNATURE, REQUEST_DATE) - функция формирования заголовка запроса 
        - принимает на вход аргумент API_SIGNATURE, в котором храниться результат выполнения функции calc_signature()
        - принимает на вход аргумент REQUEST_DATE, в котором храниться результат выполнения функции data_time()
    6) функция отправки запроса на авторизацию - fun_authorize(headers, body)
        - принимает на вход аргумент headers, в котором храниться результат выполнения функции generate_headers()
        - принимает на вход аргумент body, в котором храниться тело запроса
    7) функция отправки запроса на списание - fun_capture()
        - принимает на вход аргумент headers, в котором храниться результат выполнения функции generate_headers()
        - принимает на вход аргумент body, в котором храниться тело запроса
    8) функция отправки запроса на выплату - fun_payout()
        - принимает на вход аргумент headers, в котором храниться результат выполнения функции generate_headers()
        - принимает на вход аргумент body, в котором храниться тело запроса
    """
    
# посмотреть, есть ли авто-документация по комментариям типа Doxygen или phpDoc

    request_method: str


    def __init__(self):
        self.HOST_BASE_URL = "https://sandbox.ypmn.ru" # test EndPoint
        #self.HOST_BASE_URL = "https://secure.ypmn.ru" # prod EndPoint

        self.PAYU_SECRET_KEY = data.get('SecretKey') # Ключ API 
        self.PAYU_MERCHANT_CODE = data.get('MerchantCode') # Код мерчанта

    
    ##формирование даты
    def data_time(self):
        today = datetime.now().now().astimezone().replace(microsecond=0).isoformat()
        REQUEST_DATE = str(today)
        return REQUEST_DATE
    

    ##формирование контрольной суммы MD5
    def calcMD5(self, body):
        md5_hash = hashlib.md5(str(body).encode('utf-8')).hexdigest()
        return md5_hash


    ##формирование строки для хэширования
    def calcstrMD5(self, hashing_string, REQUEST_DATE, RequestStr):
        md5_hash2 = self.PAYU_MERCHANT_CODE + REQUEST_DATE + RequestStr + str(hashing_string)
        md5_hash2 = md5_hash2.encode('utf-8')
        return md5_hash2
    

    ##формирование подписи, используется sha256
    def calc_signature(self, md5_hash2):
        API_SIGNATURE = hmac.new(self.PAYU_SECRET_KEY.encode('utf-8'), msg=md5_hash2, digestmod=hashlib.sha256).hexdigest()
        return API_SIGNATURE
    
    
    ##получение подписи
    def generate_signature(self, body, RequestStr):
        REQUEST_DATE = self.data_time()
        hashing_string = self.calcMD5(body)
        md5_hash2 = self.calcstrMD5(hashing_string, REQUEST_DATE, RequestStr)
        signature = self.calc_signature(md5_hash2)
        return signature
    

    ##формирование заголовка запроса
    def generate_headers(self, API_SIGNATURE):
        headers = {
            "Accept": "application/json",
            "X-Header-Signature": API_SIGNATURE,
            "X-Header-Merchant": self.PAYU_MERCHANT_CODE,
            "X-Header-Date": self.data_time(),
            "Content-Type": "application/json"
        }
        return headers
    

    ##отправка запроса на авторизацию
    def request_authorize(self, body):
        try:
            RequestMethodType = "POST"
            RequestMethod = "/api/v4/payments/authorize"
            RequestStr = RequestMethodType + RequestMethod
            API_SIGNATURE = self.generate_signature(body, RequestStr)
            header = self.generate_headers(API_SIGNATURE)
            url = self.HOST_BASE_URL + RequestMethod
            response = requests.post(url, data=body, headers=header, timeout=10)
            response_dict = response.json()

            # Очищаем и записываем ответ API в JSON-файл
            with open('ypmn_api_response.json', 'w') as file:
                file.write('')
                json.dump(response_dict, file, indent=4)

            return response_dict
        except requests.exceptions.RequestException as e:
            print("Произошла ошибка при выполнении запроса:", e)

            return None


    ##отправка запроса на списание
    def request_capture(self, body):
        try:
            RequestMethodType = "POST"
            RequestMethod = "/api/v4/payments/capture"
            RequestStr = RequestMethodType + RequestMethod
            API_SIGNATURE = self.generate_signature(body, RequestStr)
            header = self.generate_headers(API_SIGNATURE)
            url = self.HOST_BASE_URL + RequestMethod
            response = requests.post(url, data=body, headers=header, timeout=10)
            response_dict = response.json()
        
            return response_dict
        except requests.exceptions.RequestException as e:
            print("Произошла ошибка при выполнении запроса:", e)

            return None
        

    ##отправка запроса на выплату
    def request_payout(self, body):
        try:
            RequestMethodType = "POST"
            RequestMethod = "/api/v4/payout/"
            RequestStr = RequestMethodType + RequestMethod
            API_SIGNATURE = self.generate_signature(body, RequestStr)
            header = self.generate_headers(API_SIGNATURE)
            url = self.HOST_BASE_URL + RequestMethod
            response = requests.post(url, data=body, headers=header, timeout=10)
            response_dict = response.json()
        
            return response_dict
        except requests.exceptions.RequestException as e:
            print("Произошла ошибка при выполнении запроса:", e)

            return None
        

    ##отправка запроса на возврат
    def request_refunds(self, body):
        try:
            RequestMethodType = "POST"
            RequestMethod = "/api/v4/payments/refund"
            RequestStr = RequestMethodType + RequestMethod
            API_SIGNATURE = self.generate_signature(body, RequestStr)
            header = self.generate_headers(API_SIGNATURE)
            url = self.HOST_BASE_URL + RequestMethod
            response = requests.post(url, data=body, headers=header, timeout=10)
            response_dict = response.json()
        
            return response_dict
        except requests.exceptions.RequestException as e:
            print("Произошла ошибка при выполнении запроса:", e)

            return None


    ##отправка запроса на создание токена
    def request_create_token(self, ref):
        try:
            body = '''{
                "payuPaymentReference": ''' + str(ref) + '''
            }'''
            RequestMethodType = "POST"
            RequestMethod = "/api/v4/token"
            RequestStr = RequestMethodType + RequestMethod
            API_SIGNATURE = self.generate_signature(str(body), RequestStr)
            header = self.generate_headers(API_SIGNATURE)
            url = self.HOST_BASE_URL + RequestMethod
            response = requests.post(url, data=body, headers=header, timeout=10)
            response_dict = response.json()
        
            return response_dict
        except requests.exceptions.RequestException as e:
            print("Произошла ошибка при выполнении запроса:", e)

            return None

    
    ##отправка запроса на возврат
    def request_status(self, transaction_number):
        try:
            body = ""
            RequestMethodType = "GET"
            RequestMethod = f"/api/v4/payments/status/{transaction_number}"
            RequestStr = RequestMethodType + RequestMethod
            API_SIGNATURE = self.generate_signature(body, RequestStr)
            header = self.generate_headers(API_SIGNATURE)
            url = self.HOST_BASE_URL + RequestMethod
            response = requests.get(url, headers=header, timeout=10)
            response_dict = response.json()
        
            return response_dict
        except requests.exceptions.RequestException as e:
            print("Произошла ошибка при выполнении запроса:", e)

            return None
    

#print(YPMNApi.__doc__)
