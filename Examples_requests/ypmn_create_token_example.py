from ypmn_classes_general_function import *

with open('ypmn_api_response.json', 'r') as file:
  data = json.load(file)

# Извлекаем значения по ключам "payuPaymentReference" и "amount"
payuPaymentRef = data.get('payuPaymentReference')
file.close()

print(payuPaymentRef)


response_dict = YPMNApi().request_create_token(str(payuPaymentRef))
print(json.dumps(response_dict, indent=4))