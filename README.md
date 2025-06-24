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

⚙️ Setup Instructions
1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/your-username/amazon-price-tracker.git
cd amazon-price-tracker
2. Create a .env File
Create a file named .env in the root directory using this template:

env
Copy
Edit
SMTP_ADDRESS="smtp.gmail.com"
EMAIL_ADDRESS="your_email@gmail.com"
EMAIL_PASSWORD="your_app_password"
✅ If you’re using Gmail, you must generate an App Password instead of using your actual email password (if 2FA is enabled).

3. Modify main.py
Change the url variable to the Amazon product you want to track

Set your desired BUY_PRICE in INR

4. Run the Script
bash
Copy
Edit
python main.py
You’ll see output like:

Copy
Edit
54990.0
Corsair Broadcast Camcorder 1080p60 Compact
✅ Email sent successfully!
🗓 Automate the Script
To check prices daily or hourly:

Windows: Use Task Scheduler

Linux/macOS: Add a cron job

Example cron job to run daily at 9 AM:

cron
Copy
Edit
0 9 * * * /usr/bin/python3 /path/to/your/main.py
📁 Project Structure
bash
Copy
Edit
amazon-price-tracker/
├── .env.example       # Environment variable template (do NOT upload .env)
├── main.py            # Main tracking and email script
├── requirements.txt   # Python dependencies
└── README.md          # Project documentation
⚠️ Disclaimer
This script is for educational purposes only.

Web scraping Amazon may violate their terms of service — use responsibly.

Amazon layout may change — in which case the scraper may need updates.

👤 Author
Devansh Palan
🔗 GitHub

