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
    3) calcstrMD5(hashing_string, REQUEST_DATE, RequestStr) - функция формирования строки для хэширования, необходима для формирования подписи 
        - принимает на вход аргумент hashing_string, в котором храниться результат выполнения функции calcMD5()
        - принимает на вход аргумент REQUEST_DATE, в котором храниться результат выполнения функции data_time()
        - принимает на вход аргумент RequestStr, в каждой функции отправки запроса он разный
    4) calc_signature(md5_hash2) - функция формирования подписи, необходимо указывать в заголовке запроса 
        - принимает на вход аргумент md5_hash2, в котором храниться результат выполнения функции calcstrMD5()
    5) generate_headers(API_SIGNATURE) - функция формирования заголовка запроса 
        - принимает на вход аргумент API_SIGNATURE, в котором храниться результат выполнения функции calc_signature()
    6) request_authorize(body) - функция отправки запроса на авторизацию 
        - принимает на вход аргумент body, что является телом запроса
    7) request_create_token(ref) - функция отправки запроса на создание токена 
        - принимает на вход аргумент ref, что является номером транзакции
    8) request_refunds(body) - функция отправки запроса на возврат ДС 
        - принимает на вход аргумент body, что является телом запроса
    9) request_capture(body) - функция отправки запроса на списание 
        - принимает на вход аргумент body, что является телом запроса
    10) request_status(transaction_number) - функция отправки запроса статуса
        - принимает на вход аргументов transaction_number
    11) request_payout(body) - функция отправки запроса на выплату
        - принимает на вход аргумент body, что является телом запроса
    12) request_cancel_token(token_hash) - функция отправки запроса на удаление токена
        - принимает на вход аргументов token_hash, что является номером токена
    13) request_token_info(token_hash) - функция отправки запроса на получение информации по токену
        - принимает на вход аргументов token_hash, что является номером токена

    """


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
        

        ##отправка запроса на удаление токена
    def request_cancel_token(self, token_hash):
        try:
            body = ""
            RequestMethodType = "DELETE"
            RequestMethod = f"/api/v4/token/{token_hash}"
            RequestStr = RequestMethodType + RequestMethod
            API_SIGNATURE = self.generate_signature(body, RequestStr)
            header = self.generate_headers(API_SIGNATURE)
            url = self.HOST_BASE_URL + RequestMethod
            response = requests.delete(url, headers=header, timeout=10)
            response_dict = response.json()
        
            return response_dict
        except requests.exceptions.RequestException as e:
            print("Произошла ошибка при выполнении запроса:", e)

            return None
    

    def request_token_info(self, token_hash):
        try:
            body = ""
            RequestMethodType = "GET"
            RequestMethod = f"/api/v4/token/{token_hash}"
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
