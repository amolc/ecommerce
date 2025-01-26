
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


from icecream import ic

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders



def sendmail_smtp(recipient,subject,body):

    SMTP_SERVER = 'smtp.zoho.in'
    SMTP_PORT = 587  # For TLS
    USERNAME = 'support@pamosapicks.com'
    PASSWORD = 'Pamosa@2023'  # Replace with your password or app-specific password

    # Email content
    sender = 'support@pamosapicks.com'
   
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


def send_order_confirmation_email(customer_email, customer_name, order_id, order_status, order_items):
    subject = 'Order Confirmation'
    # body = f"Dear {customer_name},\n\nYour order with ID {order_id} has been received with status {order_status}.\n\nItems:\n{order_items}\n\nThank you for your order!"
   
    body = f"""
        <html>
        <head>
            <style>
                .header {{
                    font-size: 24px;
                    font-weight: bold;
                    color: green;
                }}
                .order-details, .order-items {{
                    margin-top: 20px;
                }}
                .order-items th, .order-items td {{
                    border: 1px solid #ddd;
                    padding: 8px;
                }}
                .order-items th {{
                    background-color: #f2f2f2;
                }}
                .order-summary {{
                    margin-top: 20px;
                    font-weight: bold;
                }}
            </style>
        </head>
        <body>
            <p class="header">Order Status Update</p>
            <p>Dear { customer_name },</p>
            <p>Your order status has been received with status <strong>{order_status}</strong> .</p>
            <div class="order-details">
                <p><strong>Order Details:</strong></p>
                <p>Order ID: {order_id}</p>
            </div>
            <div class="order-items">
                <p><strong>Items:</strong></p>
                <table>
                    <tr>
                        <th>Product Name</th>
                        <th>Quantity</th>
                        <th>Price</th>
                    </tr>
        """
   
    sendmail_smtp(customer_email, subject, body)
    sendmail_smtp("support@pamosapicks.com", subject, body)
    sendmail_smtp("amolch001@gmail.com", subject, body)