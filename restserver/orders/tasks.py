import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_mail(
    recipient: str,
    subject: str,
    body: str
) -> None:
    SMTP_SERVER = 'smtp.zoho.in'
    SMTP_PORT = 587
    USERNAME = 'support@pamosapicks.com'
    PASSWORD = 'Pamosa@2023'
    SENDER = 'support@pamosapicks.com'
   
    try:
        # Create the email
        msg = MIMEMultipart()
        msg['From'] = SENDER
        msg['To'] = f"{recipient}, {SENDER}"
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'html'))  # Change 'plain' to 'html'

        smtp = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        smtp.ehlo()
        smtp.starttls()
        smtp.login(USERNAME, PASSWORD)
        
        smtp.sendmail(SENDER, [recipient, SENDER], msg.as_string())

        smtp.quit()
    except Exception as e:
        print(f"Failed to send email: {e}")
