import pandas as pd
import smtplib
from email.mime.text import MIMEText

# Gmail SMTP server configuration
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
GMAIL_USERNAME = "Your_Email"  # Replace with your Gmail address
GMAIL_PASSWORD = "Your_Email_app_Password"  # Replace with your generated Gmail App Password

# Load CSV and email template
data = pd.read_csv("mail_merge_data.csv")
with open("Mail_sample.txt", "r") as file:
    template_str = file.read()

# Connect to Gmail SMTP server and send emails
with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
    server.starttls()  # Secure connection
    server.login(GMAIL_USERNAME, GMAIL_PASSWORD)

    for _, row in data.iterrows():
        # Replace placeholders in the template with actual data from the CSV
        email_content = template_str.replace("{FirstName}", row["FirstName"])\
                                    .replace("{LastName}", row["LastName"])\
                                    .replace("{City}", row["City"])\
                                    .replace("{State}", row["State"])

        msg = MIMEText(email_content)
        msg["Subject"] = "Exciting News from XYZ Company!"
        msg["From"] = GMAIL_USERNAME
        msg["To"] = row["Email"]

        server.sendmail(GMAIL_USERNAME, row["Email"], msg.as_string())
        print(f"Email sent to: {row['Email']}")

print("Mail merge process completed.")