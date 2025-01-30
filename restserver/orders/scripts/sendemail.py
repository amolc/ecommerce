import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def smtpserver(recipient: str, subject: str, body: str):
    SMTP_SERVER = 'smtp.zoho.in'
    SMTP_PORT = 587  # For TLS
    USERNAME = 'support@stayvillas.co'
    PASSWORD = '10gXWOqeaf!'  # Replace with your password or app-specific password

    # Email content
    sender = 'support@stayvillas.co'
   
    try:
        # Create the email
        msg = MIMEMultipart()
        msg['From'] = sender
        msg['To'] = recipient
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        # Add attachment

        # Connect to SMTP server
        smtp = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        smtp.ehlo()
        smtp.starttls()
        smtp.login(USERNAME, PASSWORD)
        
        # Send email
        smtp.sendmail(sender, recipient, msg.as_string())
        print("Email sent successfully!")
        
        smtp.quit()
    except Exception as e:
        print(f"Failed to send email: {e}")


def run():
    # SMTP configuration
   
    subject = 'This is the Subject'
    body = 'This is the body of the email.'
    recipient = 'amolch001@gmail.com'
    smtpserver(recipient,subject,body)