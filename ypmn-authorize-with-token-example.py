from classes import *
from random import randint
import json


## Формирование Номера заказа в магазине, для примера генерируется рандомно
MERCH_ORDER_REF = str(randint(1, 10000000))


# Определяем объект класса paymentPageOptions, собираем блок настроек платежной страницы
token = merchantToken()
token.token_hash = "a1e8c1d3bba2461890d4f6fd7a64e946"
token.cvv = 123
token.owner = "123 123"
#print(token.to_dict())


# Определяем объект класса AuthorizationPP, собираем блок для авторизации
authorization = AuthorizationToken()
authorization.payment_method = "CCVISAMC"
authorization.merch_token = token.to_dict()
#print(authorization.to_dict())

# Определяем 1-ый объект класса Product, собираем блок 1-ого продукта 
product1 = Product()
product1.name = "Product name 1"
product1.sku = "productSKU1"
product1.unit_price = 500
product1.quantity = 2
product1.additional_details = "Product additional information1"
product1.vat = 0
#print(product1.to_dict())

# Определяем 2-ой объект класса Product, собираем блок 2-ого продукта
product2 = Product()
product2.name = "Product name 2"
product2.sku = "productSKU2"
product2.unit_price = 1000
product2.quantity = 1
product2.additional_details = "Product additional information2"
product2.vat = 0
#print(product2.to_dict())

# Определяем объект класса IdentityDocument, собираем блок идентификационные данные
identityDocument = IdentityDocument()
identityDocument.number = 12345
identityDocument.type = "PERSONALID"
#print(identityDocument.to_dict())

# Определяем объект класса Billing, собираем блок клиентских данные
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
#print(billing.to_dict())

# Определяем объект класса Delivery, собираем блок данных доставки
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
#print(delivery.to_dict())

# Определяем объект класса Client, собираем блок клиентских данных воедино
client = Client()
client.billing = billing
client.delivery = delivery
client.client_ip = "example"
client.client_time = "example"
#print(client.to_dict())

# Определяем объект класса PaymentRequest, собирает тело запроса
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




