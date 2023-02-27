from utils import utils


def test_load_data():
    assert utils.load_data('https://api.npoint.io/84633d18dad22794d84b') != []


def test_transaction_date():
    assert utils.transaction_date({"date": "2019-08-26T10:50:58.294041"}) == "26.08.2019"


def test_payment_invoice():
    assert utils.payment_invoice({"from": "MasterCard 7158300734726758"}) == "MasterCard 7158 30** **** 6758"
    assert utils.payment_invoice({"from": "Счет 75106830613657916952"}) == "Счет 7510 68** **** **** 6952"
    assert utils.payment_invoice({"from": "Visa Platinum 2256483756542539"}) == "Visa Platinum 2256 48** **** 2539"


def test_payment_to():
    assert utils.payment_to({"to": "Счет 35383033474447895560"}) == "Счет **5560"


def test_amount_currency():
    assert utils.amount_currency({"operationAmount": {"amount": "31957.58", "currency":
        {"code": "RUB", "name": "руб."}}}) == "31957.58 руб."
