import requests
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

# Налаштування
base_url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange"
currency_code = "USD"  # Код валюти
today = datetime.now()
dates = [(today - timedelta(days=i)).strftime("%Y%m%d") for i in range(7)]

rates = []
labels = []

# Отримання даних
for date in dates:
    response = requests.get(f"{base_url}?date={date}&json")
    if response.status_code == 200:
        data = response.json()
        for currency in data:
            if currency["cc"] == currency_code:
                rates.append(currency["rate"])
                labels.append(date)
                break

# Побудова графіка
plt.plot(labels, rates, marker="o", label=f"Курс {currency_code}")
plt.title("Динаміка курсу валют за останній тиждень")
plt.xlabel("Дата")
plt.ylabel("Курс (грн)")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()
