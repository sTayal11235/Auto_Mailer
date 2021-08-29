import pandas as pd
import smtplib, ssl
from email.mime.text import MIMEText

def sendingMail(Sender_mail, Sender_password, excel_location, subject, eMail):

    # setting up server and logging in to the sender's mail through the server
    # server 465 is secure server hence it is used
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(Sender_mail, Sender_password)

    # Reading the Excel file through panda library
    myXlFile = pd.read_excel(excel_location)

    # storing the names, mails and fields as lists in respective variables
    Mails = myXlFile['Email']

    message = MIMEText(eMail)
    message['Subject'] = subject
    message['From'] = Sender_mail
    # loop to send mail by iterating through mail list
    for i in range(len(Mails)):
        mail = Mails[i]
        message['To'] = mail

        # Opening and reading the text file

        server.sendmail(Sender_mail, [mail], message.as_string())

    # closing the server
    server.quit()