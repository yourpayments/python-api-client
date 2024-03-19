from ypmn_classes_general_function import *
from ypmn_classes_authorisation import *


## Формирование Номера заказа в магазине
MERCH_ORDER_REF = str(randint(1, 10000)) # поменять на timestamp


# Определяем объект класса CardDetails, собираем блок информации по карте
carddetails = CardDetails()
#print(CardDetails.__doc__)

carddetails.cvv = 971
carddetails.expiry_month = "08"
carddetails.expiry_year = "2025"
carddetails.number = "4652035440667037"
carddetails.owner = "John Doe"
#print(carddetails.to_dict())


# Определяем объект класса AuthorizationCard, собираем блок для авторизации
authorization = AuthorizationCard()
#print(AuthorizationCard.__doc__)

authorization.card_details = carddetails
#print(authorization.to_dict())


# Определяем 1-ый объект класса Product, собираем блок 1-ого продукта 
product1 = Product()
#print(Product.__doc__)

product1.name = "Product name 1"
product1.sku = "productSKU1"
product1.unit_price = 500
product1.quantity = -1 # можно постепенно менять прямое назначение на setter-ы с проверкой
# напр. product1.setQuantity( -1 ) # ошибка!
# либьо оставить так и добавить валидацию перед отправкой
product1.additional_details = "Product additional information1"
product1.vat = 0
#print(product1.to_dict())


# Определяем 2-ой объект класса Product, собираем блок 2-ого продукта 
product2 = Product()
#print(Product.__doc__)

product2.name = "Product name 2"
product2.sku = "productSKU2"
product2.unit_price = 1000
product2.quantity = 1
product2.additional_details = "Product additional information2"
product2.vat = 0
#print(product2.to_dict())


# Определяем объект класса IdentityDocument, собираем блок идентификационные данные
#identityDocument = IdentityDocument()
#print(IdentityDocument.__doc__)

#identityDocument.number = 12345
#identityDocument.type = "PERSONALID"
#print(identityDocument.to_dict())


# Определяем объект класса Billing, собираем блок клиентских данные
billing = Billing()
#print(Billing.__doc__)

# Имя
billing.first_name = "John"
billing.last_name = "Doe"
billing.email = "test@ypmn.ru"
billing.phone = "example"
billing.country_code = "RU"
#billing.compay_id_type = "example"
#billing.compay_id = 123445
#billing.city = "example"
#billing.state = "Bucharest"
#billing.company_name = "example"
#billing.tax_id = "example"
#billing.address_line1 = "example"
#billing.address_line2 = "example"
#billing.zip_code = "example"
#billing.identity_document = identityDocument.to_dict()
#print(billing.to_dict())


# Определяем объект класса Delivery, собираем блок данных доставки
#delivery = Delivery()
#print(Delivery.__doc__)

#delivery.first_name = "John"
#delivery.last_name = "Doe"
#delivery.phone = 7716346934
#delivery.address_line1 = "example"
#delivery.address_line2 = "example"
#delivery.zip_code = "example"
#delivery.city = "example"
#delivery.state = "example"
#delivery.country_code = "RU"
#delivery.email = "test@ypmn.ru"
#print(delivery.to_dict())


# Определяем объект класса Client, собираем блок клиентских данных воедино
client = Client()
#print(Client.__doc__)

client.billing = billing
#client.delivery = delivery
#client.client_ip = "example"
#client.client_time = "example"
#print(client.to_dict())


# Определяем объект класса AuthRequest, собирает тело запроса
paymentRequest = AuthRequest()
#print(AuthRequest.__doc__)

paymentRequest.merchant_payment_reference = MERCH_ORDER_REF
paymentRequest.authorization = authorization
paymentRequest.client = client
paymentRequest.products =   [
    product1.to_dict(), 
    product2.to_dict()
    ]
#print(paymentRequest.to_dict())


## Формирование тела запроса
body = json.dumps(paymentRequest.to_dict())
#print(body)


## Отправка запроса и получение ответа с выводом в терминал
response_dict = YPMNApi().request_authorize(body)
print(json.dumps(response_dict, indent=4))




