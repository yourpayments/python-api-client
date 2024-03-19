from ypmn_classes_general_function import *

token = '217eaff440a900f1259ee66dcbff4097'

response_dict = YPMNApi().request_cancel_token(token)
print(json.dumps(response_dict, indent=4))