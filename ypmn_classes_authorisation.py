from typing import List
import json

with open('configs.json', 'r') as file:
      data = json.load(file) 


class AuthorizationFP:

    """
    Класс создающий блок authorization, необходим для генерации тела запроса на авторизацию СБП
    """

    payment_method: str

    def __init__(
            self, 
            payment_method: str = "FASTER_PAYMENTS"
            ) -> None:
        
        self.payment_method = payment_method

    def display_info(self):
        print(self)

    def to_dict(self):
        auth_card_dict = {
            "paymentMethod": self.payment_method
            
        }  
        return {key: value for key, value in auth_card_dict.items() if value}  

#print(AuthorizationFP.__doc__)


class CardDetails:

    """
    Класс создающий блок cardDetails, необходим для генерации тела запроса на авторизацию с карточными данными
    В блоке входит CVV карты, срок действия карты разделен на месяц и год, номер карты и держатель карты
    """
    
    cvv: str
    expiry_month: str
    expiry_year: str
    number: str
    owner: str


    def __init__(
            self, 
            cvv: str = "", 
            expiry_month: str = "", 
            expiry_year: str = "", 
            number: str = "", 
            owner: str = ""
            ) -> None:        
        self.cvv = cvv
        self.expiry_month = expiry_month
        self.expiry_year = expiry_year
        self.number = number
        self.owner = owner
        
    
    def display_info(self):
        print(self)
    
    
    def to_dict(self):
        card_details_dict = {
            "number": self.number,
            "expiryMonth": self.expiry_month,
            "expiryYear": self.expiry_year,
            "cvv": self.cvv,
            "owner": self.owner
        }
        return {key: value for key, value in card_details_dict.items() if value} 
    
#print(CardDetails.__doc__)


class AuthorizationCard:

    """
    Класс создающий блок authorization, необходим для генерации тела запроса на авторизацию с карточными данными
    В блок входят метод оплаты картой, который прописан по умолчанию, и результат функции to_dict() класса CardDetails 
    """

    card_details: CardDetails
    payment_method: str

    def __init__(
            self, 
            card_details: CardDetails = None, 
            payment_method: str = "CCVISAMC"
            ) -> None:
        
        self.card_details = card_details if card_details is not None else CardDetails()
        self.payment_method = payment_method

    def display_info(self):
        print(self)

    def to_dict(self):
        auth_card_dict = {
            "paymentMethod": self.payment_method,
            "cardDetails": self.card_details.to_dict()
            
        }  
        return {key: value for key, value in auth_card_dict.items() if value}  

#print(AuthorizationCard.__doc__)
    

class paymentPageOptions:

    """
    Класс создающий блок paymentPageOptions, необходим для генерации тела запроса на авторизацию с платежной страницей
    В блок входит настройка срока действия платежной страницы, измеряется в минутах
    """

    order_timeout: str

    def __init__(
            self, 
            order_timeout: str = "43800"
            ) -> None:

        self.order_timeout = order_timeout

    def to_dict(self):
        pp_options_dict = {
            "orderTimeout": self.order_timeout,
            
        } 
        return {key: value for key, value in pp_options_dict.items() if value}

#print(paymentPageOptions.__doc__)


class AuthorizationPP:

    """
    Класс создающий блок authorization, необходим для генерации тела запроса на авторизацию с платежной страницей
    В блок входят метод оплаты картой и параметр использования платежной страницы, которые прописаны по умолчанию, 
    и результат функции to_dict() класса paymentPageOptionsу
    """

    payment_method: str = "CCVISAMC"
    use_paymen_page: str = "YES"
    payment_page_options: object

    def __init__(
            self, 
            payment_method: str = "CCVISAMC",
            use_paymen_page: str = "YES",
            payment_page_options: paymentPageOptions = None
            ) -> None:
            
        self.payment_page_options = payment_page_options if payment_page_options is not None else paymentPageOptions().to_dict()
        self.use_paymen_page = use_paymen_page
        self.payment_method = payment_method

    def display_info(self):
        print(self)

    def to_dict(self):
        auth_pp_dict = {
            "paymentMethod": self.payment_method,
            "usePaymentPage": self.use_paymen_page,
            "paymentPageOptions": paymentPageOptions().to_dict()
                
        } 
        return {key: value for key, value in auth_pp_dict.items() if value}

#print(AuthorizationPP.__doc__)


class merchantToken:

    """
    Класс создающий блок merchantToken, необходим для генерации тела запроса на авторизацию с использованием токена
    В блок входят хэш токена карты, cvv карты и держатель карты
    """

    token_hash: str
    cvv: int
    owner: str

    def __init__(
            self, 
            token_hash: str = "",
            cvv: int = 0,
            owner: str = ""
            ) -> None:
        
        self.token_hash = token_hash
        self.cvv = cvv
        self.owner = owner

    def display_info(self):
        print(self)

    def to_dict(self):
        merchant_token_dict = {
            "tokenHash": self.token_hash,
            "cvv": self.cvv,
            "owner": self.owner
                
        } 
        return {key: value for key, value in merchant_token_dict.items() if value}

#print(merchantToken.__doc__)


class AuthorizationToken:

    """
    Класс создающий блок authorization, необходим для генерации тела запроса на авторизацию с использованием токена
    В блок входят метод оплаты картой, который прописан по умолчанию, и результат функции to_dict() класса merchantToken
    """
    
    payment_method: str 
    merch_token: object

    def __init__(
            self, 
            payment_method: str = "CCVISAMC",
            merch_token: merchantToken = None
            ) -> None:
            
        self.merch_token = merch_token if merch_token is not None else merchantToken().to_dict()
        self.payment_method = payment_method

    def display_info(self):
        print(self)

    def to_dict(self):
        auth_token_dict = {
            "paymentMethod": self.payment_method,
            "merchantToken": self.merch_token
                
        } 
        return {key: value for key, value in auth_token_dict.items() if value}
    
#print(AuthorizationToken.__doc__)


class IdentityDocument:

    """
    Данный блок не является обязательным, он будет закомичен в примерах кода авторизаций
    Класс создающий блок identityDocument, необходим для генерации тела запроса на авторизацию
    (общий для всех вариаций блока авторизации)
    В блок входят идентификационные данные, к примеру серия и номер паспорта и наименование документа
    """

    number: int
    type: str

    def __init__(
            self, 
            number: int = 0, 
            type: str = ""
            ) -> None:
        
        self.number = number
        self.type = type

    def display_info(self):
        print(self)

    def to_dict(self):
        identity_document_dict = {
            "number": self.number,
            "type": self.type
            
        }  
        return {key: value for key, value in identity_document_dict.items() if value}
#print(IdentityDocument.__doc__)    



class Billing:

    """
    Класс создающий блок billing, необходим для генерации тела запроса на авторизацию
    (общий для всех вариаций блока авторизации)
    Обязательные параметры, которые должны быть не путстые first_name, last_name, email, phone, country_code. Остальные по желанию
    """

    address_line1: str = ""
    address_line2: str = ""
    city: str = ""
    company_name: str = ""
    compay_id: int = 0
    compay_id_type: str = ""
    country_code: str = ""
    email: str = ""
    first_name: str = ""
    identity_document: IdentityDocument = None
    last_name: str = ""
    phone: str = ""
    state: str = ""
    tax_id: str = ""
    zip_code: str = ""

    def __init__(
            self, 
            address_line1: str = "", 
            address_line2: str = "", 
            city: str = "", 
            company_name: str = "", 
            compay_id: int = 0, 
            compay_id_type: str = "", 
            country_code: str = "", 
            email: str = "", 
            first_name: str = "", 
            identity_document: IdentityDocument = None, 
            last_name: str = "", 
            phone: str = "", 
            state: str = "", 
            tax_id: str = "", 
            zip_code: str = ""
            ) -> None:
        
        self.address_line1 = address_line1
        self.address_line2 = address_line2
        self.city = city
        self.company_name = company_name
        self.compay_id = compay_id
        self.compay_id_type = compay_id_type
        self.country_code = country_code
        self.email = email
        self.first_name = first_name
        self.identity_document = identity_document if identity_document is not None else IdentityDocument().to_dict()
        self.last_name = last_name
        self.phone = phone
        self.state = state
        self.tax_id = tax_id
        self.zip_code = zip_code

    def display_info(self):
        print(self)

    def to_dict(self):
        billing_dict = {
            "firstName": self.first_name,
            "lastName": self.last_name,
            "compayIdType": self.compay_id_type,
            "compayId": self.compay_id,
            "email": self.email,
            "phone": self.phone,
            "city": self.city,
            "countryCode": self.country_code,
            "state": self.state,
            "companyName": self.company_name,
            "taxId": self.tax_id,
            "addressLine1": self.address_line1,
            "addressLine2": self.address_line2,
            "zipCode": self.zip_code,
            "identityDocument": self.identity_document
                        
        }
        return {key: value for key, value in billing_dict.items() if value}
        
    
#print(Billing.__doc__)    


class Delivery:

    """
    Данный блок не является обязательным, он будет закомичен в примерах кода авторизаций  
    Класс создающий блок delivery, необходим для генерации тела запроса на авторизацию
    (общий для всех вариаций блока авторизации)

    """

    address_line1: str
    address_line2: str
    city: str
    country_code: str
    email: str
    first_name: str
    last_name: str
    phone: int
    state: str
    zip_code: str

    def __init__(
            self, 
            address_line1: str = "", 
            address_line2: str = "", 
            city: str = "", 
            country_code: str = "", 
            email: str = "", 
            first_name: str = "", 
            last_name: str = "", 
            phone: int = 0, 
            state: str = "", 
            zip_code: str = ""
            ) -> None:
        
        self.address_line1 = address_line1
        self.address_line2 = address_line2
        self.city = city
        self.country_code = country_code
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.state = state
        self.zip_code = zip_code

    def display_info(self):
        print(self)

    def to_dict(self):
        delivery_dict = {
            "firstName": self.first_name,
            "lastName": self.last_name,
            "phone": self.phone,
            "addressLine1": self.address_line1,
            "addressLine2": self.address_line2,
            "zipCode": self.zip_code,
            "city": self.city,
            "state": self.state,
            "countryCode": self.country_code,
            "email": self.email
        }

        return {key: value for key, value in delivery_dict.items() if value}
    
#print(Delivery.__doc__)      


class Client:

    """
    Класс создающий блок client, необходим для генерации тела запроса на авторизацию
    (общий для всех вариаций блока авторизации)

    """

    billing: Billing
    client_ip: str
    client_time: str
    delivery: Delivery

    def __init__(
            self, 
            billing: Billing = None, 
            client_ip: str = "", 
            client_time: str = "", 
            delivery: Delivery = None
            ) -> None:
        
        self.billing = billing if billing is not None else Billing()
        self.client_ip = client_ip
        self.client_time = client_time
        self.delivery = delivery if delivery is not None else Delivery()

    def display_info(self):
        print(self)

    def to_dict(self):
        client_dict = {
            "billing": self.billing.to_dict(),
            "delivery": self.delivery.to_dict(),
            "clientIp": self.client_ip,
            "clientTime": self.client_time

            
        }
        return {key: value for key, value in client_dict.items() if value} 

#print(Client.__doc__)


class Product:

    """
    Класс создающий блок product, необходим для генерации тела запроса на авторизацию
    (общий для всех вариаций блока авторизации)

    """

    additional_details: str
    name: str
    quantity: int
    sku: str
    unit_price: float
    vat: int

    def __init__(
            self, 
            additional_details: str = "", 
            name: str = "", 
            quantity: int = 0, 
            sku: str = "", 
            unit_price: float = 0, 
            vat: int = 0
            ) -> None:
        
        self.additional_details = additional_details
        self.name = name
        self.quantity = quantity
        self.sku = sku
        self.unit_price = unit_price

    def display_info(self):
        print(self)

    def to_dict(self):
        product_dict = {
            "name": self.name,
            "sku": self.sku,           
            "unitPrice": self.unit_price,
            "quantity": self.quantity,
            "additionalDetails": self.additional_details
            
        }
        return {key: value for key, value in product_dict.items() if value} 
    
#print(Product.__doc__)    


class AuthRequest:

    """
    Класс создающий тело запроса, необходим для генерации тела запроса на авторизацию
    (общий для всех вариаций блока авторизации)

    """

    authorization: object
    client: Client
    merchant_payment_reference: int
    products: List[Product]
    return_url: str

    def __init__(
            self, 
            authorization: object = None, 
            client: Client = None, 
            merchant_payment_reference: int = 0, 
            products: List[Product] = []
            ) -> None:
        
        self.authorization = authorization if authorization is not None else object()
        self.client = client if client is not None else Client()
        self.merchant_payment_reference = merchant_payment_reference
        self.products = products

    def display_info(self):
        print(self)

    def to_dict(self):
        auth_request_dict = {
            "merchantPaymentReference": self.merchant_payment_reference,
            "currency": data.get('Currency'),
            "returnUrl": data.get('returnURL'),
            "authorization": self.authorization.to_dict(),
            "client": self.client.to_dict(),
            "products": self.products
            
        }
        return {key: value for key, value in auth_request_dict.items() if value} 
    
#print(AuthRequest.__doc__)  