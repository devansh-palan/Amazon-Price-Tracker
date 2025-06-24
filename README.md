# 🛒 Amazon Price Tracker

This is a Python script that checks the price of a specific Amazon product and sends you an email notification when the price drops below a specified threshold.

---

## 🚀 Features

- Scrapes the product title and price from Amazon India
- Sends an email alert if the product's price is below your target
- Uses environment variables to securely handle email credentials
- Lightweight and ready for automation (cron/Task Scheduler)

---

## 🧰 Requirements

- Python 3.7+
- Dependencies:
  - `requests`
  - `beautifulsoup4`
  - `python-dotenv`

Install them using:

```bash
pip install -r requirements.txt
