from classes import *
from random import randint
import json


## Формирование Номера заказа в магазине
MERCH_ORDER_REF = str(randint(1, 10000))


# Определяем объект класса CardDetails 
carddetails = CardDetails()
carddetails.cvv = 971
carddetails.expiry_month = "08"
carddetails.expiry_year = "2025"
carddetails.number = "4652035440667037"
carddetails.owner = "John Doe"


# Определяем объект класса Authorization 
authorization = AuthorizationCard()
authorization.payment_method = "CCVISAMC"
authorization.card_details = carddetails


# Определяем 1-ый объект класса Product 
product1 = Product()
product1.name = "Product name 1"
product1.sku = "productSKU1"
product1.unit_price = 500
product1.quantity = 2
product1.additional_details = "Product additional information1"
product1.vat = 0


# Определяем 2-ой объект класса Product, 
product2 = Product()
product2.name = "Product name 2"
product2.sku = "productSKU2"
product2.unit_price = 1000
product2.quantity = 1
product2.additional_details = "Product additional information2"
product2.vat = 0

# Определяем объект класса IdentityDocument, 
identityDocument = IdentityDocument()
identityDocument.number = 12345
identityDocument.type = "PERSONALID"


# Определяем объект класса Billing, 
billing = Billing()
billing.first_name = "John"
billing.last_name = "Doe"
billing.compay_id_type = "example"
billing.compay_id = 123445
billing.email = "test@ypmn.ru"
billing.phone = "example"
billing.city = "example"
billing.country_code = "RU"
billing.state = "Bucharest"
billing.company_name = "example"
billing.tax_id = "example"
billing.address_line1 = "example"
billing.address_line2 = "example"
billing.zip_code = "example"
billing.identity_document = identityDocument.to_dict()


# Определяем объект класса Delivery, 
delivery = Delivery()
delivery.first_name = "John"
delivery.last_name = "Doe"
delivery.phone = 7716346934
delivery.address_line1 = "example"
delivery.address_line2 = "example"
delivery.zip_code = "example"
delivery.city = "example"
delivery.state = "example"
delivery.country_code = "RU"
delivery.email = "test@ypmn.ru"


# Определяем объект класса Client, 
client = Client()
client.billing = billing
client.delivery = delivery
client.client_ip = "example"
client.client_time = "example"


# Определяем объект класса, 
paymentRequest = PaymentRequest()
paymentRequest.merchant_payment_reference = MERCH_ORDER_REF
paymentRequest.currency = "RUB"
paymentRequest.return_url = "https://sandbox.ypmn.ru/backend/simulators/return.php"
paymentRequest.authorization = authorization
paymentRequest.client = client
paymentRequest.products =   [
    product1.to_dict(), 
    product2.to_dict()
    ]
#print(paymentRequest.to_dict())

## Формирование тела запроса
body = json.dumps(paymentRequest.to_dict())

## Определяем объект класса PayUApi, 
ypmn_api = YPMNApi()

## Формирование даты
REQUEST_DATE = ypmn_api.data_time()
#print(REQUEST_DATE)

## Формирование контрольной суммы MD5
md5_hash = ypmn_api.calcMD5(body)
#print(md5_hash)

## Формирование строки для хэширования
md5_hash2 = ypmn_api.calcstrMD5(md5_hash, REQUEST_DATE)
#print(md5_hash2)

## Формирование signature, sha256
API_SIGNATURE = ypmn_api.calc_signature(md5_hash2)

## Формирование заголовка запроса
header = ypmn_api.generate_headers(API_SIGNATURE, REQUEST_DATE)
#print(header)
response_dict = ypmn_api.fun_authorize(header, body)
print(json.dumps(response_dict, indent=4))




