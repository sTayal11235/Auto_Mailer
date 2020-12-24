import pandas as pd
import smtplib as srvr

#inputing the senders mail ID and password to log in
Sender_mail = input()
Sender_password = input()

#setting up server and logging in to the sender's mail through the server
#server 465 is secure server hence it is used
server = srvr.SMTP_SSL('smtp.gmail.com', 465)
server.ehlo()
server.login(Sender_mail,Sender_password)

#User Input Exact location of exel file and mail text file
excel_location = input("Input the location of Excel file and invert the slash")
mail_location = input("Input the location of Mail text file and invert the slash")

#Reading the Excel file through panda library
myXlFile = pd.read_excel(excel_location)

#storing the names, mails and fields as lists in respective variables
Names = myXlFile['Name']
Mails = myXlFile['Mail']
Field = myXlFile['Field']

#loop to send mail by iterating through mail list
for i in range(len(Mails)):
    name = Names[i]
    mail = Mails[i]
    field = Field[i]

    # Opening and reading the text file and replacing the {NAME} and {FIELD} by those in the list
    myTxTFile = open(mail_location)
    message = myTxTFile.read()
    message = message.replace("{NAME}", name)
    message = message.replace("{FIELD}", field)

    server.sendmail(Sender_mail, [mail], message)
    myTxTFile.close()

#closing the server
server.close()