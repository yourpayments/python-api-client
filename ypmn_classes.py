from typing import List
from datetime import datetime
import hashlib
import hmac
import requests
from random import randint

        
class YPMNApi:
    def __init__(self):
        self.PAYU_SECRET_KEY = "SECRET_KEY" # Ключ API
        self.PAYU_MERCHANT_CODE = "CC1" # Код мерчанта
        self.request_method = "POST/api/v4/payments/authorize"
        self.HOST_BASE_URL = "https://sandbox.ypmn.ru" # test EndPoint
        #self.HOST_BASE_URL = "https://secure.ypmn.ru" # prod EndPoint
       

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
    
    def fun_authorize(self, headers, body):
        url = self.HOST_BASE_URL + '/api/v4/payments/authorize'
        response = requests.post(url, data=body, headers=headers, timeout=10)
        response_dict = response.json()
        
        return response_dict


class CardDetails:
    cvv: int
    expiry_month: str
    expiry_year: int
    number: str
    owner: str

    def __init__(
            self, 
            cvv: int = 0, 
            expiry_month: str = "0", 
            expiry_year: int = "0", 
            number: str = "0", 
            owner: str = "0"
            ) -> None:        
        self.cvv = cvv
        self.expiry_month = expiry_month
        self.expiry_year = expiry_year
        self.number = number
        self.owner = owner
        
    
    def display_info(self):
        print(self)
    
    
    def to_dict(self):
        return {
            "number": self.number,
            "expiryMonth": self.expiry_month,
            "expiryYear": self.expiry_year,
            "cvv": self.cvv,
            "owner": self.owner
        }

class AuthorizationCard:
    card_details: CardDetails
    payment_method: str

    def __init__(
            self, 
            card_details: CardDetails = None, 
            payment_method: str = ""
            ) -> None:
        
        self.card_details = card_details if card_details is not None else CardDetails()
        self.payment_method = payment_method

    def display_info(self):
        print(self)

    def to_dict(self):
        return {
            "paymentMethod": self.payment_method,
            "cardDetails": self.card_details.to_dict()
            
        }    
    

class paymentPageOptions:
    order_timeout: str

    def __init__(
            self, 
            order_timeout: str = "43800"
            ) -> None:

        self.order_timeout = order_timeout

    def to_dict(self):
        return {
            "orderTimeout": self.order_timeout,
            
        } 


class AuthorizationPP:
    payment_method: str 
    use_paymen_page: str = "YES"
    payment_page_options: object

    def __init__(
            self, 
            payment_method: str = "",
            use_paymen_page: str = "",
            payment_page_options: paymentPageOptions = None
            ) -> None:
            
        self.payment_page_options = payment_page_options if payment_page_options is not None else paymentPageOptions().to_dict()
        self.use_paymen_page = use_paymen_page
        self.payment_method = payment_method

    def display_info(self):
        print(self)

    def to_dict(self):
        return {
            "paymentMethod": self.payment_method,
            "usePaymentPage": self.use_paymen_page,
            "paymentPageOptions": paymentPageOptions().to_dict()
                
        } 
    

class merchantToken:
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
        return {
            "tokenHash": self.token_hash,
            "cvv": self.cvv,
            "owner": self.owner
                
        } 


class AuthorizationToken:
    payment_method: str 
    merch_token: object

    def __init__(
            self, 
            payment_method: str = "",
            merch_token: paymentPageOptions = None
            ) -> None:
            
        self.merch_token = merch_token if merch_token is not None else merchantToken().to_dict()
        self.payment_method = payment_method

    def display_info(self):
        print(self)

    def to_dict(self):
        return {
            "paymentMethod": self.payment_method,
            "merchantToken": self.merch_token
                
        } 













class IdentityDocument:
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
        return {
            "number": self.number,
            "type": self.type
            
        }  


class Billing:
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
        return {
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


class Delivery:
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
        return {
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


class Client:
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
        return {
            "billing": self.billing.to_dict(),
            "delivery": self.delivery.to_dict(),
            "clientIp": self.client_ip,
            "clientTime": self.client_time

            
        }



class Product:
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
        return {
            "name": self.name,
            "sku": self.sku,           
            "unitPrice": self.unit_price,
            "quantity": self.quantity,
            "additionalDetails": self.additional_details
            
        }


class PaymentRequest:
    authorization: object
    client: Client
    currency: str
    merchant_payment_reference: int
    products: List[Product]
    return_url: str

    def __init__(
            self, 
            authorization: object = None, 
            client: Client = None, 
            currency: str = "", 
            merchant_payment_reference: int = 0, 
            products: List[Product] = [], 
            return_url: str = ""
            ) -> None:
        
        self.authorization = authorization if authorization is not None else object()
        self.client = client if client is not None else Client()
        self.currency = currency
        self.merchant_payment_reference = merchant_payment_reference
        self.products = products
        self.return_url = return_url

    def display_info(self):
        print(self)

    def to_dict(self):
        return {
            "merchantPaymentReference": self.merchant_payment_reference,
            "currency": self.currency,
            "returnUrl": self.return_url,
            "authorization": self.authorization.to_dict(),
            "client": self.client.to_dict(),
            "products": self.products
            
        }



