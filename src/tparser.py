import logging
from datetime import date, timedelta

import requests

from src.utils import form_data_for_message, get_all_orders

logging.basicConfig(level=logging.INFO)


class TParser:
    """ Класс для парсинга заказов с Трипстера """

    def __init__(self, base_url: str, token: str) -> None:
        self.base_url = base_url
        self.token = token
        self.headers = {
            "Authorization": f"Token {self.token}",
        }

    def get_orders(self) -> list[dict]:
        """
        Получение списка всех будущих заказов, учитывая сегодня.
        Базовый метод.
        """

        try:
            all_orders = get_all_orders(self.base_url, headers=self.headers)
            logging.info(f'Total orders found: {len(all_orders)}.')
            # print(all_orders)
            return all_orders
        except requests.RequestException as e:
            logging.warning(f"Ошибка при получении данных: {e}")
            return []

    def get_next_tours(self) -> list[dict]:
        """
        Получение списка оплаченных заказов на сегодня и завтра.
        Фильтруются заказы из метода get_orders.
        """

        next_tour_data = self.get_orders()
        next_tours = []
        for order in next_tour_data:
            tour_date = date.fromisoformat(order['event']['date'])
            if order['status'] == 'paid' and tour_date - date.today() <= timedelta(days=1):
                next_tours.append(order)
        if not next_tours:
            print('No excursions found.')
        # print(next_tours)
        logging.info(f'Found {len(next_tours)} orders for today and tomorrow.')
        return next_tours

    def get_tours_data(self) -> list[dict]:
        """
        Получение списка словарей только с нужными данными:
        название экскурсии, дата, время, имя и телефон туриста, сумма к доплате
        для дальнейшего формирования сообщения.
        Используется метод get_next_tours для получения списка ближайших экскурсий.
        """
        orders = self.get_next_tours()
        data = form_data_for_message(orders)  # get data for messages sending
        return data
