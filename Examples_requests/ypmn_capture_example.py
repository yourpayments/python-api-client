from ypmn_classes_general_function import *
from ypmn_classes_capture import *


amount = 1500


paymentRequest = CaptureRequest()
#print(CaptureRequest.__doc__)


paymentRequest.amount = amount
#print(paymentRequest.to_dict())


## Формирование тела запроса
body = json.dumps(paymentRequest.to_dict())
#print(body)


## Отправка запроса и получение ответа с выводом в терминал
response_dict = YPMNApi().request_capture(body)
print(json.dumps(response_dict, indent=4))
