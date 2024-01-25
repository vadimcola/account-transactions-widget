# импортируем нужные функции из utils
from utils.utils import load_data, transaction_date, payment_invoice, payment_to, amount_currency
# импортируем необходимые модули
from operator import itemgetter

# создаем константу с сылкой на файл json
BANK_STATEMENT = 'operations.json'

# создаем пустой список
transaction_no_sort = []

# в цикле вызываем фурнкцию и перебараем её
for i in load_data(BANK_STATEMENT):
    # если в списке есть пустой словарь то его пропускаем
    # остольные словори добавляем в пустой список
    if i == {}:
        continue
    transaction_no_sort.append(i)

# сортируем список с словорями по заданному условию
transaction = sorted(transaction_no_sort, key=itemgetter('date'), reverse=True)

# создаем счетчик
counter = 0

# запускаем цикл перебераем словори в списке
for list_transaction in transaction:

    # если транзакция была не выполнена то ее пропускаем
    if list_transaction['state'] == 'CANCELED':
        continue

    # если счетчик меньше 5 то выводим сообщение
    if counter < 5:
        counter += 1
        # если транзакция было открытием вклада то выводим сообщение с открытием вклада
        if list_transaction['description'] == "Открытие вклада":
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
    # если счетчик больше или равен 5 то цикл останавливаем
    else:
        break
