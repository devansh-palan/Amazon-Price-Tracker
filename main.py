# ================= Amazon Price Tracker =================
# This script checks the price of a specific Amazon product
# and sends you an email notification if the price drops below a defined threshold.

from bs4 import BeautifulSoup
import requests
import smtplib
import os
from dotenv import load_dotenv

# Load environment variables from the .env file (for email credentials)
load_dotenv()

# Amazon product URL (Make sure it's the correct product variation)
url = "https://www.amazon.in/Corsair-Broadcast-Camcorder-1080p60-Compact/dp/B07K3FN5MR/ref=s9_acsd_al_ot_cv2_0_t?_encoding=UTF8&pf_rd_m=A21TJRUUN4KGV&pf_rd_s=merchandised-search-13&pf_rd_r=DSJ812TZP6NE927JNSG1&pf_rd_p=0f4b741e-cd58-4473-8d3a-abe27d975ee5&pf_rd_t=976460031&pf_rd_i=976460031&th=1"

# Set a minimal header to avoid being blocked by Amazon's bot protection
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

# Send HTTP request to Amazon product page
response = requests.get(url, headers=header)
soup = BeautifulSoup(response.content, "html.parser")

# Parse the product price from the HTML
price = soup.find(class_="a-offscreen").get_text()
price_without_currency = price.split("₹")[1]  # Remove ₹ symbol
price_without_currency = price_without_currency.replace(',', '')  # Remove comma for thousands
price_as_float = float(price_without_currency)  # Convert to float
print(price_as_float)

# Parse the product title from the HTML
title = soup.find(id="productTitle").get_text().strip()
print(title)

# Define your target price — if the product is below this, an email will be sent
BUY_PRICE = 60000

# If price condition is met, send an email alert
if price_as_float < BUY_PRICE:
    message = f"{title} is on sale for {price}!"

    # ====================== Send Email Notification ======================
    try:
        with smtplib.SMTP(os.environ["SMTP_ADDRESS"], port=587) as connection:
            connection.starttls()  # Secure the connection
            connection.login(os.environ["EMAIL_ADDRESS"], os.environ["EMAIL_PASSWORD"])  # Login to SMTP server
            connection.sendmail(
                from_addr=os.environ["EMAIL_ADDRESS"],
                to_addrs=os.environ["EMAIL_ADDRESS"],  # You can use a different recipient too
                msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}".encode("utf-8")
            )
        print("✅ Email sent successfully!")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")
