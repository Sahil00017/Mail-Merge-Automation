# Mail Merge Automation using Python and Gmail SMTP

## 📌 Overview

  This project automates the process of sending personalized emails using Python, Pandas, and Gmail's SMTP server. The script reads recipient details from a CSV file, loads an email template, and sends customized emails to each recipient.

## 🔧 Features
- Reads recipient data from a CSV file.
- Uses an email template with placeholders for dynamic content.
- Connects to Gmail's SMTP server securely.
- Sends personalized emails to multiple recipients.

## 🛠 Prerequisites
  Ensure you have the following installed before running the script:
  - Python 3.x
  - Pandas library
  - smtplib (built-in Python module)
  - An active Gmail account with App Password enabled

## 📂 Project Structure

📂 Mail-Merge-Automation
├── 📄 mail_merge.py       # Main script for sending emails
├── 📄 mail_merge_data.csv # CSV file with recipient data
├── 📄 Mail_sample.txt     # Email template with placeholders
└── 📄 README.md           # Documentation

## 🚀 Installation and Setup
**1. Clone the repository:**
```bash
git clone https://github.com/your-username/Mail-Merge-Automation.git
cd Mail-Merge-Automation
```
**2. Install required dependencies:**
```bash
pip install pandas
```
**3. Set up your Gmail account:**
- Enable Less Secure Apps or generate an App Password.
- Update GMAIL_USERNAME and GMAIL_PASSWORD in mail_merge.py.

## 📝 Preparing Email Content
**1. CSV File (mail_merge_data.csv):**
| First Name| Last Name| Email            | City              | State     |
|-----------|----------|------------------|-------------------|-----------|
|**John**   |**Doe**   |**John@ex.com**   |**New York**       |**NY**     |
|**Jane**   |**Smith** |**Jane@ex.com**   |**Los Angeles**    |**CA**     |

**2. Email Template (Mail_sample.txt):**
```bash
Dear {FirstName} {LastName},

We have exciting news for you in {City}, {State}!
Stay tuned for more updates.

Best regards,
XYZ Company
```

## ▶️ Running the Script
Execute the script using:
```bash
python mail_merge.py
```

## 🔒 Security Note
- Never hardcode your Gmail password in the script.
- Use environment variables or .env files to store credentials securely.

## 📜 License
This project is licensed under the MIT License.
Feel free to copy this and use it directly in your GitHub repository! Let me know if you need any additional adjustments. 🚀
