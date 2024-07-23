import pytest
import requests
import json

import config

# test database connection
def test_db_conn():
    conn, cursor, api = config.start()
    cursor.execute("SELECT * FROM stock")
    stocks = cursor.fetchall()
    for stock in stocks:
        print(stock)

# print etfs
def test_etfs():
    conn, cursor, api = config.start()
    cursor.execute("SELECT * FROM stock WHERE is_etf = TRUE")
    etfs = cursor.fetchall()
    for etf in etfs:
        print(etf)

# basic ark api hiting
def test_ark_api():
    etf = "ARKK"
    date = "2024-06-10"
    url = config.create_url(etf, date_to=date)
    r = requests.get(url)
    if r.status_code == 200:
        print(json.dumps(r.json(), indent=2))

# parse json from ark api
def test_json_parsing():
    etf = "ARKK"
    date = "2024-06-10"
    url = config.create_url(etf, date_to=date, limit=3)
    r = requests.get(url)
    if r.status_code == 200:
        holdings = r.json()["holdings"]
        for holding in holdings:
            print(holding)
