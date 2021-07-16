import datetime
from dateutil import relativedelta
import requests
import re
import csv


def date_to_token(date):
    day = '0' + str(date.day) if 1 <= date.day <= 9 else str(date.day)
    month = f'0{date.month}' if 1 <= date.month <= 9 else f'{date.month}'
    return 'https://www.cbr.ru/scripts/XML_daily.asp?date_req=' + day + '/' + month + '/' + str(date.year)


def parse_currency_list(date):
    aux = requests.get(date_to_token(date))
    currency_list = []
    for elem in re.findall(r'<CharCode>[A-Z]{3}<\/CharCode>', aux.text):
        currency_list.append(elem[10:13])
    return currency_list


def parse_currency_value(date):
    aux = requests.get(date_to_token(date))
    currency_value = []
    for elem in re.findall(r'<Value>[-,0-9]{7,8}<\/Value>', aux.text):
        currency_value.append(elem[7:14])
    return currency_value


def create_csv(date_range):
    currency_column = parse_currency_list(date_range[0])
    data = []
    header = ['Валюта']
    delta = relativedelta.relativedelta(days=1)
    next_date = date_range[0]
    while next_date <= date_range[1]:
        data.append(parse_currency_value(next_date))
        header.append(str(next_date))
        next_date += delta
    data_all = []
    data_all.append(currency_column)
    data_all = data_all + data
    data_all = zip(*data_all)
    with open('parsing_results.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(data_all)


if __name__ == '__main__':
    create_csv([datetime.datetime.now() - relativedelta.relativedelta(days=3), datetime.datetime.now()])
