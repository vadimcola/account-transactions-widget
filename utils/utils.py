import requests
import time


def load_data(path):
    """
    выгрузка данных из файла

    """
    data = requests.get(path)
    data_ = data.json()
    return data_


def transaction_date(list_transaction: list) -> str:
    '''
    форматирование даты в нужный вариант
    :param list_transaction: список транзакций
    :return: выдает дату в формате ДД.ММ.ГГГГ
    '''
    date = list_transaction['date'][0:10]
    pre_format_date = time.strptime(date, "%Y-%m-%d")
    format_date = time.strftime("%d.%m.%Y", pre_format_date)
    return format_date
