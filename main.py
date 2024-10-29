import requests

def get_exchange_rates():

    url = "https://bank.gov.ua/NBU_Exchange/exchange_site?start=20241022&end=20241029&valcode=usd&sort=exchangedate&order=desc&json"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        for item in data:
            print(f"Дата: {item['exchangedate']}, Валюта: {item['cc']}, Курс: {item['rate']}")
    else:
        print("Error")

if __name__ == "__main__":
    get_exchange_rates()