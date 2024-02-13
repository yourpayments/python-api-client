from ypmn_classes import CardDetails
from ypmn_classes import Authorization
from ypmn_classes import Billing
from ypmn_classes import Delivery
from ypmn_classes import IdentityDocument
from ypmn_classes import Client
from ypmn_classes import Product
from ypmn_classes import PaymentRequest
from ypmn_classes import PayUApi
from random import randint
import json


## Формирование Номера заказа в магазине
MERCH_ORDER_REF = str(randint(1, 10000))

# Определяем объект класса CardDetails 
carddetails = CardDetails(
  971, 
  "08",
  "2025",
  "4652035440667037",
  "John Doe"
  )

# Определяем объект класса Authorization 
authorization = Authorization(
  carddetails,
  "CCVISAMC"
  )

# Определяем 1-ый объект класса Product 
product1 = Product(
  "Product additional information1",
  "Product name 1",
  2,
  "productSKU1", 
  500, 
  0
  )

# Определяем 2-ой объект класса Product, 
product2 = Product(
  "Product additional information2", 
  "Product name 2", 
  1, 
  "productSKU2", 
  1000, 
  0
  )

# Определяем объект класса IdentityDocument, 
identityDocument = IdentityDocument(
  12345,
  "PERSONALID"
  )

# Определяем объект класса Billing, 
billing = Billing(
  "example", 
  "example", 
  "example", 
  "example", 
  123445, 
  "PERSONALID", 
  "RU", 
  "test@ypmn.ru", 
  "John", 
  identityDocument, 
  "Doe", 
  "0771346934", 
  "Bucharest", 
  "example", 
  "example"
  )

# Определяем объект класса Delivery, 
delivery = Delivery(
  "example", 
  "example", 
  "example", 
  "RU", 
  "test@ypmn.ru", 
  "example", 
  "example", 
  7716346934, 
  "example", 
  "example"
  )

# Определяем объект класса Client, 
client = Client(
  billing, 
  "example", 
  "example", 
  delivery
  )

# Определяем объект класса, 
paymentRequest = PaymentRequest(
  authorization, 
  client, 
  "RUB", 
  MERCH_ORDER_REF, 
  [
    product1.to_dict(), 
    product2.to_dict()
    ], 
  "https://sandbox.ypmn.ru/backend/simulators/return.php"
  )

#print(paymentRequest.to_dict())

## Формирование тела запроса
body = json.dumps(paymentRequest.to_dict())

## Определяем объект класса PayUApi, 
payu_api = PayUApi()

## Формирование даты
REQUEST_DATE = payu_api.data_time()
#print(REQUEST_DATE)

## Формирование контрольной суммы MD5
md5_hash = payu_api.calcMD5(body)
#print(md5_hash)

## Формирование строки для хэширования
md5_hash2 = payu_api.calcstrMD5(md5_hash, REQUEST_DATE)
#print(md5_hash2)

## Формирование signature, sha256
API_SIGNATURE = payu_api.calc_signature(md5_hash2)

## Формирование заголовка запроса
header = payu_api.generate_headers(API_SIGNATURE, REQUEST_DATE)
#print(header)
response_dict = payu_api.fun_authorize(header, body)
print(json.dumps(response_dict, indent=4))




