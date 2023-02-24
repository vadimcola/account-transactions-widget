# импортируем нужные функции из utils
from utils.utils import load_data, transaction_date, payment_invoice, payment_to, amount_currency
# импортируем необходимые модули
from operator import itemgetter

# задаем констатну с ссылкой на банковскую выписку
BANK_STATEMENT_URL = "https://api.npoint.io/7e0408563a1ef990bc71"

# делаем сортировку списка словорей по определеным данным а также выводим первые пять словорей
transaction = sorted(load_data(BANK_STATEMENT_URL), key=itemgetter('date'), reverse=True)[0:6]

# запускаем цикл перебераем словори в списке
for list_transaction in transaction:

    # если транзакция была не выполнена то ее пропускаем
    if list_transaction['state'] == 'CANCELED':
        continue

    # если транзакция было открытием вклада то выводим сообщение с открытием вклада
    elif list_transaction['description'] == "Открытие вклада":
        print(f"{transaction_date(list_transaction)} {list_transaction['description']}\n"
              f"Вклад открыт -> {payment_to(list_transaction)}\n"
              f"{amount_currency(list_transaction)}")

    # если была оплата выводим сообщение с какого на какой счет
    else:
        print(f"{transaction_date(list_transaction)} {list_transaction['description']}\n"
              f"{payment_invoice(list_transaction)} -> {payment_to(list_transaction)}\n"
              f"{amount_currency(list_transaction)}")

    # добавляем один пробел между каждым выводом
    print()
