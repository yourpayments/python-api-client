from ypmn_classes_general_function import *
from ypmn_classes_payout import *

MERCHANT_ORDER_REFERENCE = str(randint(1, 10000000))

amountPayout = Amount()

amountPayout.value = 1000

cardPayout = Card()

cardPayout.card_number = 4149605380309302

recipientPayout = Recipient()

recipientPayout.type = "individual"
recipientPayout.email = "example@email.com"
recipientPayout.city = "Bucharest"
recipientPayout.address = "Sector 2"
recipientPayout.postal_code = "510002"
recipientPayout.first_name = "John"
recipientPayout.last_name = "Doe"

destination = Destination()

destination.type = "individual"
destination.card = cardPayout.to_dict()
destination.recipient = recipientPayout.to_dict()


sender = Sender()

sender.first_name = "John"
sender.last_name = "John"
sender.email = "senderEmail@mail.com"
sender.phone = "0764111111"

source = Source()

source.sender = sender.to_dict()


requestPayout = PayoutRequest()

requestPayout.merchant_payout_reference = MERCHANT_ORDER_REFERENCE
requestPayout.amount = amountPayout.to_dict()
requestPayout.description = "Description of payout"
requestPayout.destination = destination.to_dict()
requestPayout.source = source.to_dict()
#print(requestPayout.to_dict())


## Формирование тела запроса
body = json.dumps(requestPayout.to_dict())
#print(body)


## Отправка запроса и получение ответа с выводом в терминал
response_dict = YPMNApi().request_payout(body)
print(json.dumps(response_dict, indent=4))


