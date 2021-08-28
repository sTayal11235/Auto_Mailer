import pandas as pd
import smtplib as srvr

def sendingMail(Sender_mail, Sender_password, excel_location, mail_location):

    # setting up server and logging in to the sender's mail through the server
    # server 465 is secure server hence it is used
    server = srvr.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(Sender_mail, Sender_password)

    # Reading the Excel file through panda library
    myXlFile = pd.read_excel(excel_location)

    # storing the names, mails and fields as lists in respective variables
    Mails = myXlFile['Email']

    # loop to send mail by iterating through mail list
    for i in range(len(Mails)):
        mail = Mails[i]

        # Opening and reading the text file
        myTxTFile = open(mail_location)
        message = myTxTFile.read()

        server.sendmail(Sender_mail, [mail], message)
        myTxTFile.close()

    # closing the server
    server.close()