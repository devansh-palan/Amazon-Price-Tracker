# 🛒 Amazon Price Tracker

This is a simple Python script that tracks the price of a product on Amazon India and sends an email alert when the price drops below a specified threshold.

---

## 🚀 Features

- Scrapes product title and price from an Amazon India product page
- Sends an email notification if the price is below your target
- Uses environment variables for secure credential handling
- Easy to automate with Task Scheduler or `cron`

---

## 🧰 Requirements

- Python 3.7 or higher
- Libraries:
  - `requests`
  - `beautifulsoup4`
  - `python-dotenv`

Install all dependencies with:

```bash
pip install -r requirements.txt
