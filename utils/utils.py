import requests


def load_data(path):
    """
    выгрузка данных из файла

    """
    data = requests.get(path)
    data_ = data.json()
    return data_
