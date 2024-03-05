import json

class CaptureRequest:

    """
    Класс создающий тело запроса, необходим для генерации тела запроса на списание
    (общий для всех вариаций блока авторизации)
    """

    payuReference: str
    original_amount: float
    amount: float

    def __init__(
            self, 
            payuReference: str = "", 
            original_amount: float = 0,
            amount: float = 0
            ) -> None:
        
        # Открываем файл с ответом API для чтения
        with open('ypmn_api_response.json', 'r') as file:
            data = json.load(file)

        # Извлекаем значения по ключам "payuPaymentReference" и "amount"
        payuReference = data.get('payuPaymentReference')
        originalAmount = data.get('amount')
        
        self.payuReference = payuReference
        self.original_amount = originalAmount
        self.amount = amount

    def display_info(self):
        print(self)




    def to_dict(self):
        return {
            "payuPaymentReference": self.payuReference,
            "originalAmount": self.original_amount,
            "amount": self.amount,
            "currency": "RUB"
            
        }

#print(AuthRequest.__doc__) 