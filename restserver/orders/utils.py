
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
        msg.attach(MIMEText(body, 'html'))

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
    <body>
        <p style="font-size: 24px; font-weight: bold; color: green;">Order Received</p>
        <p>Dear {customer_name},</p>
        <p>Your Order <strong>{order_id}</strong> has been received with status <strong>{order_status}</strong>.</p>
        <div style="margin-top: 20px;">
            <p><strong>Order Details:</strong></p>
            <p>Order ID: {order_id}</p>
        </div>
        <div style="margin-top: 20px;">
            <p><strong>Items:</strong></p>
            <table style="border-collapse: collapse; width: 100%; margin-top: 10px;">
                <tr>
                    <th style="border: 1px solid #ddd; padding: 8px; background-color: #f2f2f2;">Product Name</th>
                    <th style="border: 1px solid #ddd; padding: 8px; background-color: #f2f2f2;">Quantity</th>
                    <th style="border: 1px solid #ddd; padding: 8px; background-color: #f2f2f2;">Price</th>
                    <th style="border: 1px solid #ddd; padding: 8px; background-color: #f2f2f2;">Product Sub Total</th>
                </tr>
        """
    for item in order_items:
            order_total = sum(float(item['product_subtotal']) for item in order_items)
            body += f"""
                <tr>
                    <td style="border: 1px solid #ddd; padding: 8px;">{item['product_name']}</td>
                    <td style="border: 1px solid #ddd; padding: 8px;">{item['product_qty']}</td>
                    <td style="border: 1px solid #ddd; padding: 8px;">{item['product_price']}</td>
                    <td style="border: 1px solid #ddd; padding: 8px;">{item['product_subtotal']}</td>
                </tr>
            """

   
    body += f"""
                <tr>
                    <td style="border: 1px solid #ddd; padding: 8px;" colspan="3"><strong>Order Total:</strong></td>
                    <td style="border: 1px solid #ddd; padding: 8px;"><strong>{order_total}</strong></td>
                </tr>
            """
    body += """
                </table>
            </div>
            <p>Thank you for your order!</p>
            <p>Best regards,</p>
            <p>Pamosapicks</p>
        </body>
        </html>
        """

   
    sendmail_smtp(customer_email, subject, body)
    sendmail_smtp("support@pamosapicks.com", subject, body)
    sendmail_smtp("amolch001@gmail.com", subject, body)