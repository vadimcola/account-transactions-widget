import requests
import time
import json


def load_data(filename):
    """
    выгрузка данных из файла

    """
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data


def transaction_date(list_transaction: list) -> str:
    """
    форматирование даты в нужный вариант
    :param list_transaction: список транзакций
    :return: выдает дату в формате ДД.ММ.ГГГГ
    """
    date = list_transaction['date'][0:10]
    pre_format_date = time.strptime(date, "%Y-%m-%d")
    format_date = time.strftime("%d.%m.%Y", pre_format_date)
    return format_date


def payment_invoice(list_transaction: list) -> str:
    """
    функция выводит с какого счета была произведена оплата
    :param list_transaction: список транзакция
    :return: вывод в зашифрованном виде номер карты или счета показывается
    не польностью
    """
    payment = list_transaction['from']
    if len(payment.split()) == 3:
        account_number = payment.split()[2]
        number_output = f'{" ".join(payment.split()[0:2])} {account_number[:4]}' \
                        f' {account_number[4:6]}** **** {account_number[-4:]}'
    elif len(payment.split()) == 2:
        account_number = payment.split()[1]
        if len(payment.split()[1]) == 16:
            number_output = f'{payment.split()[0]} {account_number[:4]}' \
                            f' {account_number[4:6]}** **** {account_number[-4:]}'
        elif len(payment.split()[1]) == 20:
            number_output = f'{payment.split()[0]} {account_number[:4]}' \
                            f' {account_number[4:6]}** **** **** {account_number[-4:]}'

    return number_output


def payment_to(list_transaction: list) -> str:
    '''
    функция выводит на какой счет был осуществлен перевод
    :param list_transaction:
    :return: выводит счет в зашифрованном виде
    '''
    payment = list_transaction['to']
    account_number = payment.split()[1]
    return f'{payment.split()[0]} **{account_number[-4:]}'


def amount_currency(list_transaction: list) -> str:
    '''
    функция выводит суммы перевода и валюту
    :param list_transaction: список транзакций
    :return:
    '''
    amount = list_transaction['operationAmount']['amount']
    currency = list_transaction['operationAmount']['currency']['name']
    return f"{amount} {currency}"
