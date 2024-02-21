from ypmn_classes import *

amount = 2000


RequestMethodType = "POST"
RequestMethod = "/api/v4/payments/capture"
RequestStr = RequestMethodType + RequestMethod


paymentRequest = CaptureRequest()
#print(CaptureRequest.__doc__)


paymentRequest.amount = amount
#print(paymentRequest.to_dict())


## Формирование тела запроса
body = json.dumps(paymentRequest.to_dict())
#print(body)


## Определяем объект класса PayUApi
ypmn_api = YPMNApi(RequestStr)
#print(YPMNApi.__doc__)


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
#print(API_SIGNATURE)


## Формирование заголовка запроса
header = ypmn_api.generate_headers(API_SIGNATURE, REQUEST_DATE)
#print(header)


response_dict = ypmn_api.fun_capture(header, body)
print(json.dumps(response_dict, indent=4))