from ypmn_classes_general_function import *

with open('ypmn_api_response.json', 'r') as file:
  data = json.load(file)

# Извлекаем значения по ключам "payuPaymentReference" и "amount"
merchantPaymentRef = data.get('merchantPaymentReference')
file.close()

response_dict = YPMNApi().request_status(merchantPaymentRef)
print(json.dumps(response_dict, indent=4))