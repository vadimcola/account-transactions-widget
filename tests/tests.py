from utils import utils


def test_load_data():
    assert utils.load_data('https://api.npoint.io/84633d18dad22794d84b') != []


def test_transaction_date():
    assert utils.transaction_date({"date": "2019-08-26T10:50:58.294041"}) == "26.08.2019"
