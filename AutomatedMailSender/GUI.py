import tkinter as tk
from tkinter import font
from tkinter import filedialog
from sendingServer import sendingMail

def BrowseXlsFile(cnvs, xlsPathBox):
    global xlsFilePath
    xlsFilePath = filedialog.askopenfile(title = "Browse xls File").name
    xlsPathBox.insert(0, xlsFilePath)

def BrowseTxtFile(mail, cnvs, txtPathBox):
    global txtFilePath
    txtFilePath = filedialog.askopenfile(title = "Browse text File").name
    txtPathBox.insert(0, txtFilePath)
    txtFile = open(str(txtFilePath)).read()
    mail.insert(0.0,txtFile)

def SaveChanges(mail):
    txtFile = open(str(txtFilePath), 'a+')
    txtFile.truncate(0)
    txtFile.write(mail.get(0.0, 100000000000.0) + '\n')

def GUI():
    top = tk.Tk()
    top.title("AutoMailer")
    #top.resizable(0,0)

    cnvs = tk.Canvas(top, highlightthickness = 2, highlightbackground = "black", bg = "#ffe4d2", height = 720, width = 1080)

    cnvs.create_rectangle(100, 30, 980, 700, width=1.5)
    cnvs.create_rectangle(150 , 10, 930, 50, width=1.5, fill = "tomato")

    headFont = font.Font(family = 'Courgette Regular', weight = "bold", size = 23)
    cnvs.create_text(540, 30, font = headFont, text = "Automated Mail Sender")

    cnvs.create_rectangle(130, 100, 950, 210, width=1.5)
    cnvs.create_rectangle(145, 87, 277, 113, width=1.5, fill ="#ffe4d2")

    subHead01 = font.Font(family = 'Minion Pro', weight = "bold", size = 18)
    cnvs.create_text(210, 100, font = subHead01, text = "Your Details")

    dataFont = font.Font(family = 'Minion Pro', weight = "bold", size = 12)
    entryFont = font.Font(family='Fixedsys', weight="bold", size=12)

    cnvs.create_text(200, 140, font = dataFont, text = "Email ID :")
    userId = tk.Entry(top, font = entryFont, fg='#000080')
    cnvs.create_window(600, 140, height = 25, width = 500, window = userId)

    cnvs.create_text(200, 180, font = dataFont, text="Password :")
    pwd = tk.Entry(top, font = entryFont, fg='#000080')
    cnvs.create_window(600, 180, height=25, width=500, window=pwd)

    cnvs.create_rectangle(130, 250, 950, 675, width=1.5)
    cnvs.create_rectangle(145, 235, 315, 265, width=1.5, fill="#ffe4d2")

    subHead01 = font.Font(family='Minion Pro', weight="bold", size=18)
    cnvs.create_text(230, 250, font=subHead01, text="Compose Mail")

    cnvs.create_text(310, 300, font = dataFont, text = "Enter or Browse xls File Location")
    xlsPathBox = tk.Entry(cnvs, font = entryFont, fg='#000080')
    cnvs.create_window(580, 332, height=25, width=620, window= xlsPathBox)
    xlsFileBtn = tk.Button(cnvs, text = "Browse", command = lambda : BrowseXlsFile(cnvs, xlsPathBox))
    xlsFileBtn.place(x = 200, y = 320)

    cnvs.create_text(280, 445, font=dataFont, text="Edit/Enter Desired Mail")
    mail = tk.Text(cnvs)
    cnvs.create_window(550, 540, height = 170, width = 700, window=mail)

    cnvs.create_text(332, 380, font=dataFont, text="Enter or Browse Mail Text File Location")
    txtPathBox = tk.Entry(cnvs, font = entryFont, fg='#000080')
    cnvs.create_window(580, 412, height=25, width=620, window=txtPathBox)
    textFileBtn = tk.Button(cnvs, text = "Browse", command = lambda : BrowseTxtFile(mail, cnvs, txtPathBox))
    textFileBtn.place(x = 200, y = 400)

    saveChanges = tk.Button(cnvs, text = "Save Changes", command = lambda : SaveChanges(mail))
    saveChanges.place(x = 815, y = 600)

    sendMail = tk.Button(cnvs, text = "Send Mails", bg = "#7bb574", command = lambda : sendingMail(userId.get(), pwd.get(), xlsFilePath, txtFilePath))
    sendMail.place(x = 540, y = 635)

    cnvs.pack()
    top.mainloop()

GUI()