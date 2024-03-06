from typing import List
from datetime import datetime
import hashlib
import hmac
import requests
from random import randint
import json

with open('configs.json', 'r') as file:
      data = json.load(file) 


class Amount:



    value: float
    
    def __init__(
            self, 
            value: float = 0

            ) -> None:
        
        self.value = value
    
    def to_dict(self):
        amount_dict = {
            "currency": data.get('Currency'),
            "value": self.value
            
        }
        return {key: value for key, value in amount_dict.items() if value} 


class Card:



    card_number: str

    def __init__(
            self, 
            card_number: str = ""

            ) -> None:
        
        self.card_number = card_number
    
    def to_dict(self):
        card_dict = {
            "cardNumber": self.card_number
            
        }
        return {key: value for key, value in card_dict.items() if value} 
    
class Token:


    token_hash: str

    def __init__(
            self, 
            token_hash: str = ""

            ) -> None:
        
        self.token_hash = token_hash
    
    def to_dict(self):
        token_dict = {
            "tokenHash": self.token_hash
            
        }
        return {key: value for key, value in token_dict.items() if value} 


class Recipient:



    type: str
    email: str
    city: str
    address: str
    postal_code: int
    first_name: str
    last_name: str

    def __init__(
            self, 
            type: str = "",
            email: str = "",
            city: str = "",
            address: str = "",
            postal_code: int = 0,
            first_name: str = "",
            last_name: str = ""

            ) -> None:
        
        self.type = type
        self.email = email
        self.city = city
        self.address = address
        self.postal_code = postal_code
        self.first_name = first_name
        self.last_name = last_name

    def to_dict(self):
        recipient_dict = {
            "type": self.type,
            "email": self.email,
            "city": self.city,
            "address": self.address,
            "postalCode": self.postal_code,
            "countryCode": data.get('CountryCode'),
            "firstName": self.first_name,
            "lastName": self.last_name

        }
        return {key: value for key, value in recipient_dict.items() if value} 


class Destination:



    card: Card
    recipient: Recipient

    def __init__(
            self, 
            card: Card = None,
            recipient: Recipient = ""

            ) -> None:
        
        self.type = type
        self.card = Card
        self.recipient = Recipient

    def to_dict(self):
        destination_dict = {
            "type": "card",
            "card": self.card,
            "recipient": self.recipient

        }
        return {key: value for key, value in destination_dict.items() if value}
    

class DestinationToken:



    token: Token
    recipient: Recipient

    def __init__(
            self, 
            token: Token = None,
            recipient: Recipient = ""

            ) -> None:
        
        self.type = type
        self.token = Token
        self.recipient = Recipient

    def to_dict(self):
        destination_token_dict = {
            "type": "token",
            "token": self.token,
            "recipient": self.recipient

        }
        return {key: value for key, value in destination_token_dict.items() if value}


class Sender:



    first_name: str
    last_name: str
    email: str
    phone: str

    def __init__(
            self, 
            phone: str = "",
            first_name: str = "",
            last_name: str = "",
            email: str = ""

            ) -> None:
        
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone

    def to_dict(self):
        sender_dict = {
            "firstName": self.first_name,
            "lastName": self.last_name,
            "email": self.email,
            "phone": self.phone

        }
        return {key: value for key, value in sender_dict.items() if value}
    

class Source:

    """
    Класс создающий блок source, необходим для генерации тела запроса на выплату с карточными данными
    В блоке входит CVV карты, срок действия карты разделен на месяц и год, номер карты и держатель карты
    """

    type: str
    sender: Sender

    def __init__(
            self, 
            sender: Sender = None

            ) -> None:
        
        self.sender = Sender

    def to_dict(self):
        source_dict = {
            "type": "merchantBalance",
            "sender": self.sender

        }
        return {key: value for key, value in source_dict.items() if value}


class PayoutRequest:

    """
    Класс создающий тело запроса, необходим для генерации тела запроса на выплату
    """

    merchant_payout_reference: str
    amount: Amount
    description: str
    destination: Destination
    source: Source

    def __init__(
            self, 
            merchant_payout_reference: str = "",
            amount: Amount = None,
            description: str = "",
            destination: Destination = None,
            source: Source = None

            ) -> None:
        
        self.merchant_payout_reference = merchant_payout_reference
        self.amount = Amount
        self.description = description
        self.destination = Destination
        self.source = Source



    def to_dict(self):
        payout_request_dict = {
            "merchantPayoutReference": self.merchant_payout_reference,
            "amount": self.amount,
            "description": self.description,
            "destination": self.destination,
            "source": self.source
            
        }
        return {key: value for key, value in payout_request_dict.items() if value}

#print(PayoutRequest.__doc__)