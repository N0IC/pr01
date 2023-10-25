import requests
import json

class APIException(Exception):
    pass

class CurrencyConverter:
    @staticmethod
    def get_price(base_currency, target_currency):
        # Отправляем запрос к API для получения текущей цены валют
        response = requests.get(f'https://api-пример/{base_currency}')
        data = json.loads(response.text)

        # Проверяем, получен ли ответ
        if response.status_code != 200:
            raise APIException('Ошибка взаимодействия с API')

        # Проверяем, существует ли указанная валюта
        if base_currency not in data['rates']:
            raise APIException('Исходная валюта не найдена')

        if target_currency not in data['rates']:
            raise APIException('Целевая валюта не найдена')

        # Получаем и возвращаем цену валюты
        price = data['rates'][target_currency]
        return price