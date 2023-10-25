
import telebot
import smtplib
from emailsender_bot import EmailSender, EmailMessage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from telebot import types


# This is not a complete code for sending email with telegram bot  contact @toolsdark for purchasing our service !!


# Please note it is just a format as i couldnot reveal source code, lookup our bot for test mails:- @tooldark_bot


bot = telebot.TeleBot('TOKEN')


# Initialize the EmailSender bot
email_bot = EmailSender(provider='smtp', apiKey='API_KEY')

# Create an EmailMessage object
email_message = EmailMessage()
email_message.set_subject('Hello, World!')
email_message.set_recipient('recipient@example.com')
email_message.set_text('This is a test email sent from EmailSender Bot.')

# Attach a file if needed
email_message.attach_file('attachment.pdf')

# Send the email
response = email_bot.send_email(email_message)

if response.status_code == 200:
    print("Email sent successfully!")
else:
    print("Email sending failed.")

bot.polling()
