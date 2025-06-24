Amazon Price Tracker
A Python script that monitors the price of a specified Amazon product and sends an email notification when the price drops below a user-defined threshold.
Features

Scrapes product price and title from an Amazon product page using BeautifulSoup.
Sends email alerts via SMTP when the price falls below the target price.
Uses environment variables for secure email credential management.
Configurable for any Amazon product URL and target price.

Requirements

Python 3.x
Required Python libraries:pip install beautifulsoup4 requests python-dotenv


A Gmail account with an App Password for SMTP access.

Setup

Clone the repository:
git clone https://github.com/your-username/amazon-price-tracker.git
cd amazon-price-tracker


Install dependencies:
pip install -r requirements.txt


Configure environment variables:

Create a .env file in the project root.
Add the following:SMTP_ADDRESS="smtp.gmail.com"
EMAIL_ADDRESS="your_email@gmail.com"
EMAIL_PASSWORD="your_app_password"


Replace your_email@gmail.com with your Gmail address and your_app_password with your Gmail App Password.


Update the script:

Open main.py and modify the url variable to the Amazon product URL you want to track.
Set the BUY_PRICE variable to your desired price threshold.



Usage
Run the script to check the product price and receive an email if the price is below the target:
python main.py


The script prints the current price and product title to the console.
If the price is below BUY_PRICE, it sends an email with the product title, price, and URL.

Example
For the product URL in main.py (Corsair Broadcast Camcorder), if BUY_PRICE = 60000 and the price drops to ₹55,000, you'll receive an email like:
Subject: Amazon Price Alert!

Corsair Broadcast Camcorder is on sale for ₹55,000!
https://www.amazon.in/Corsair-Broadcast-Camcorder-1080p60-Compact/dp/B07K3FN5MR/...

Notes

Amazon's bot protection may block requests if headers are not set properly. The script includes a basic User-Agent header to mimic a browser.
To avoid being blocked, do not run the script too frequently. Consider scheduling it (e.g., using cron or a task scheduler) to run once or twice daily.
Ensure the Amazon URL points to the correct product variation, as prices may differ.

License
This project is licensed under the MIT License. See the LICENSE file for details.