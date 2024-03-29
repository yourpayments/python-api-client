# Твои Платежи, интеграция на Python
![](https://repository-images.githubusercontent.com/638835276/ff494b04-d65b-4843-8759-e85c689a7e80)

## Версия Альфа v1.0
1) Файл [ypmn_classes_general_function.py](https://github.com/yourpayments/python-api-client/blob/main/ypmn_classes_general_function.py) структура следующая:
- Функция расчета подписи (calc_signature)
- Функция генерации заголовка запроса (generate_headers)
- Функция отправки запроса на авторизацию (request_authorize)
- Функция отправки запроса на создание токена (request_create_token)
- Функция отправки запроса на возврат ДС (request_refunds)
- Функция отправки запроса на списание (request_capture)
- Функция отправки запроса статуса (request_status)
- Функция отправки запроса на выплату (request_payout)


2) Файл [ypmn_classes_authorisation.py](https://github.com/yourpayments/python-api-client/blob/main/ypmn_classes_authorisation.py) :
- генерация тела запроса на авторизацию(у всех запросов общая структура сборки, отличия только в одном блоке json запроса)


3) Файл [ypmn_classes_payout.py](https://github.com/yourpayments/python-api-client/blob/main/ypmn_classes_payout.py) :
- генерация тела запроса на выплату(у всех запросов общая структура сборки, отличия только в одном блоке json запроса)


4) Файл [ypmn_classes_capture.py](https://github.com/yourpayments/python-api-client/blob/main/ypmn_classes_capture.py) :
- генерация тела запроса на списание


5) Файл [ypmn_classes_refund.py](https://github.com/yourpayments/python-api-client/blob/main/ypmn_classes_refund.py) :
- генерация тела запроса на отмену/возврат


6) Файл [config.json](https://github.com/yourpayments/python-api-client/blob/main/config.json) структура ключей следующая:
- секретный ключ
- код мерчанта
- код валюты
- код страны


7) Файл [ypmn_api_response.json](https://github.com/yourpayments/python-api-client/blob/main/ypmn_api_response.json) - буфер
- в данный файл записывается ответ API с каждого запроса на авторизацию, перед каждым запросом происходит отчистка файла


Примеры формирования запросов в папке Examples_requests

1) Файл [ypmn_authorize_pp_example.py](https://github.com/yourpayments/python-api-client/blob/main/Examples_requests/ypmn_authorize_pp_example.py) структура следующая:
- генерация тела запроса на авторизацию с платежной страницей
- отправка запроса по API

2) Файл [ypmn_authorize_fp_example.py](https://github.com/yourpayments/python-api-client/blob/main/Examples_requests/ypmn_authorize_fp_example.py) структура следующая:
- генерация тела запроса на авторизацию СБП
- отправка запроса по API

3) Файл [ypmn_authorize_card_example.py](https://github.com/yourpayments/python-api-client/blob/main/Examples_requests/ypmn_authorize_card_example.py) структура следующая:
- генерация тела запроса на авторизацию с карточными данными
- отправка запроса по API

4) Файл [ypmn_authorize_token_example.py](https://github.com/yourpayments/python-api-client/blob/main/Examples_requests/ypmn_authorize_token_example.py) структура следующая:
- генерация тела запроса на авторизацию с использованием токена
- отправка запроса по API
 
5) Файл [ypmn_capture_example.py](https://github.com/yourpayments/python-api-client/blob/main/Examples_requests/ypmn_capture_example.py) структура следующая:
- генерация тела запроса на списание
- отправка запроса по API

6) Файл [ypmn_refund_example.py](https://github.com/yourpayments/python-api-client/blob/main/Examples_requests/ypmn_refund_example.py) структура следующая:
- генерация тела запроса на возврат
- отправка запроса по API

7) Файл [ypmn_payout_card_example.py](https://github.com/yourpayments/python-api-client/blob/main/Examples_requests/ypmn_payout_card_example.py) структура следующая:
- генерация тела запроса на выплату
- отправка запроса по API

8) Файл [ypmn_payout_token_example.py](https://github.com/yourpayments/python-api-client/blob/main/Examples_requests/ypmn_payout_token_example.py) структура следующая:
- генерация тела запроса на выплату
- отправка запроса по API

9) Файл [ypmn_create_token_example.py](https://github.com/yourpayments/python-api-client/blob/main/Examples_requests/ypmn_create_token_example.py) структура следующая:
- генерация тела запроса на создание токена
- отправка запроса по API

10) Файл [ypmn_get_status_example.py](https://github.com/yourpayments/python-api-client/blob/main/Examples_requests/ypmn_get_status_example.py) структура следующая:
- отправка запроса на получение статуса транзакции по API 

11) Файл [ypmn_cancel_token_example.py](https://github.com/yourpayments/python-api-client/blob/main/Examples_requests/ypmn_cancel_token_example.py) структура следующая:
- отправка запроса на удаление токена по API 

12) Файл [ypmn_get_token_info_example.py](https://github.com/yourpayments/python-api-client/blob/main/Examples_requests/ypmn_get_token_info_example.py) структура следующая:
- отправка запроса информации о токене по API 


![](https://github.com/yourpayments/python-api-client/blob/main/ypmn-python-client.png)

## Ссылки
- [Основной сайт НКО "Твои Платежи"](https://YPMN.ru/)
- [Докуметация по API](https://ypmn.ru/ru/documentation/)
- [Реквизиты тестовых банковских карт](https://dev.payu.ru/ru/documents/rest-api/testing/#menu-2)
- [Задать вопрос или сообщить о проблеме](https://github.com/yourpayments/php-api-client/issues/new)

-------------
[НКО «Твои Платежи»](https://YPMN.ru/ "Платёжная система для сайтов, платформ и приложений") - платёжная система для сайтов, платформ, игр и приложений.
