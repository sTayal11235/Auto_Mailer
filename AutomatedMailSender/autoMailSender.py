#import pandas as pd
#import smtplib as srvr
import tkinter as tk
from tkinter import font

# def sendingMail():
#     # inputing the senders mail ID and password to log in
#     Sender_mail = input()
#     Sender_password = input()
#
#     # setting up server and logging in to the sender's mail through the server
#     # server 465 is secure server hence it is used
#     server = srvr.SMTP_SSL('smtp.gmail.com', 465)
#     server.ehlo()
#     server.login(Sender_mail, Sender_password)
#
#     # User Input Exact location of exel file and mail text file
#     excel_location = input("Input the location of Excel file and invert the slash")
#     mail_location = input("Input the location of Mail text file and invert the slash")
#
#     # Reading the Excel file through panda library
#     myXlFile = pd.read_excel(excel_location)
#
#     # storing the names, mails and fields as lists in respective variables
#     Names = myXlFile['Name']
#     Mails = myXlFile['Email']
#
#     # loop to send mail by iterating through mail list
#     for i in range(len(Mails)):
#         name = Names[i]
#         mail = Mails[i]
#
#         # Opening and reading the text file and replacing the {NAME} and {FIELD} by those in the list
#         myTxTFile = open(mail_location)
#         message = myTxTFile.read()
#         message = message.replace("{NAME}", name)
#
#         server.sendmail(Sender_mail, [mail], message)
#         myTxTFile.close()
#
#     # closing the server
#     server.close()

def GUI():
    top = tk.Tk()
    top.title("AutoMailer")

    cnvs = tk.Canvas(top, highlightthickness = 2, highlightbackground = "black", bg = "#ffe4d2", height = 720, width = 1080)

    cnvs.create_rectangle(100, 30, 980, 700, width=1.5)
    cnvs.create_rectangle(150 , 10, 930, 50, width=1.5, fill = "tomato")

    headFont = font.Font(family = 'Courgette Regular', weight = "bold", size = 23)
    cnvs.create_text(540, 30, font = headFont, text = "Automated Mail Sender")

    cnvs.create_rectangle(130, 100, 950, 210, width=1.5)
    cnvs.create_rectangle(135, 87, 268, 113, width=1.5, fill ="#ffe4d2")

    subHead01 = font.Font(family = 'Minion Pro', weight = "bold", size = 18)
    cnvs.create_text(200, 100, font = subHead01, text = "Your Details")

    dataFont = font.Font(family = 'Minion Pro', weight = "bold", size = 12)

    cnvs.create_text(200, 140, font = dataFont, text = "Email ID :")
    userId = tk.Entry(top)
    cnvs.create_window(600, 140, height = 25, width = 500, window = userId)

    cnvs.create_text(200, 180, font = dataFont, text="Password :")
    pwd = tk.Entry(top)
    cnvs.create_window(600, 180, height=25, width=500, window=pwd)

    cnvs.pack()
    top.mainloop()

GUI()


#Available fonts - ('System', 'Terminal', 'Fixedsys', 'Modern', 'Roman', 'Script', 'Courier',
#                   'MS Serif', 'MS Sans Serif', 'Small Fonts', 'Adobe Caslon Pro Bold', 'Adobe Caslon Pro',
#                   'Adobe Fangsong Std R', '@Adobe Fangsong Std R', 'Adobe Fan Heiti Std B', '@Adobe Fan Heiti Std B',
#                   'Adobe Gothic Std B', '@Adobe Gothic Std B', 'Adobe Heiti Std R', '@Adobe Heiti Std R', 'Adobe Kaiti Std R',
#                   '@Adobe Kaiti Std R', 'Adobe Naskh Medium', 'Adobe Garamond Pro Bold', 'Adobe Garamond Pro',
#                   'Birch Std', 'Blackoak Std', 'Brush Script Std', 'Chaparral Pro', 'Chaparral Pro Light',
#                   'Charlemagne Std', 'Hobo Std', 'Kozuka Gothic Pro B', '@Kozuka Gothic Pro B',
#                   'Kozuka Gothic Pro EL', '@Kozuka Gothic Pro EL', 'Kozuka Gothic Pro H', '@Kozuka Gothic Pro H',
#                   'Kozuka Gothic Pro L', '@Kozuka Gothic Pro L', 'Kozuka Gothic Pro M', '@Kozuka Gothic Pro M', 'Kozuka Gothic Pro R',
#                   '@Kozuka Gothic Pro R', 'Kozuka Mincho Pro B', '@Kozuka Mincho Pro B', 'Kozuka Mincho Pro EL', '@Kozuka Mincho Pro EL',
#                   'Kozuka Mincho Pro H', '@Kozuka Mincho Pro H', 'Kozuka Mincho Pro L', '@Kozuka Mincho Pro L', 'Kozuka Mincho Pro M',
#                   '@Kozuka Mincho Pro M', 'Kozuka Mincho Pro R', '@Kozuka Mincho Pro R', 'Lithos Pro Regular', 'Minion Pro Cond', 'Minion Pro Med',
#                   'Minion Pro SmBd', 'Myriad Arabic', 'Nueva Std', 'Nueva Std Cond', 'OCR A Std', 'Orator Std',
#                   'Poplar Std', 'Prestige Elite Std', 'Source Sans Pro Black', 'Source Sans Pro', 'Source Sans Pro ExtraLight',
#                   'Source Sans Pro Light', 'Source Sans Pro Semibold', 'Tekton Pro', 'Tekton Pro Cond', 'Tekton Pro Ext',
#                   'Trajan Pro 3', 'Adobe Arabic', 'Adobe Devanagari', 'Adobe Gurmukhi', 'Adobe Hebrew', 'Adobe Ming Std L',
#                   '@Adobe Ming Std L', 'Adobe Myungjo Std M', '@Adobe Myungjo Std M', 'Adobe Song Std L', '@Adobe Song Std L',
#                   'Kozuka Gothic Pr6N B', '@Kozuka Gothic Pr6N B', 'Kozuka Gothic Pr6N EL', '@Kozuka Gothic Pr6N EL', 'Kozuka Gothic Pr6N H',
#                   '@Kozuka Gothic Pr6N H', 'Kozuka Gothic Pr6N L', '@Kozuka Gothic Pr6N L', 'Kozuka Gothic Pr6N M', '@Kozuka Gothic Pr6N M',
#                   'Kozuka Gothic Pr6N R', '@Kozuka Gothic Pr6N R', 'Kozuka Mincho Pr6N B', '@Kozuka Mincho Pr6N B', 'Kozuka Mincho Pr6N EL',
#                   '@Kozuka Mincho Pr6N EL', 'Kozuka Mincho Pr6N H', '@Kozuka Mincho Pr6N H', 'Kozuka Mincho Pr6N L', '@Kozuka Mincho Pr6N L',
#                   'Kozuka Mincho Pr6N M', '@Kozuka Mincho Pr6N M', 'Kozuka Mincho Pr6N R', '@Kozuka Mincho Pr6N R', 'Letter Gothic Std',
#                   'Minion Pro', 'Myriad Hebrew', 'Myriad Pro', 'Myriad Pro Cond', 'Myriad Pro Light', 'The Skinny',
#                   'The Skinny bold', 'The Light Font', 'Coyote SemiBold DEMO', 'TeamViewer15', 'Marlett', 'Arial', 'Arabic Transparent',
#                   'Arial Baltic', 'Arial CE', 'Arial CYR', 'Arial Greek', 'Arial TUR', 'Arial Black', 'Bahnschrift Light', 'Bahnschrift SemiLight',
#                   'Bahnschrift', 'Bahnschrift SemiBold', 'Bahnschrift Light SemiCondensed', 'Bahnschrift SemiLight SemiConde',
#                   'Bahnschrift SemiCondensed', 'Bahnschrift SemiBold SemiConden', 'Bahnschrift Light Condensed', 'Bahnschrift SemiLight Condensed',
#                   'Bahnschrift Condensed', 'Bahnschrift SemiBold Condensed', 'Calibri', 'Calibri Light', 'Cambria', 'Cambria Math', 'Candara',
#                   'Comic Sans MS', 'Consolas', 'Constantia', 'Corbel', 'Courier New', 'Courier New Baltic', 'Courier New CE', 'Courier New CYR',
#                   'Courier New Greek', 'Courier New TUR', 'Ebrima', 'Franklin Gothic Medium', 'Gabriola', 'Gadugi', 'Georgia', 'Impact', 'Ink Free',
#                   'Javanese Text', 'Leelawadee UI', 'Leelawadee UI Semilight', 'Lucida Console', 'Lucida Sans Unicode', 'Malgun Gothic',
#                   '@Malgun Gothic', 'Malgun Gothic Semilight', '@Malgun Gothic Semilight', 'Microsoft Himalaya', 'Microsoft JhengHei',
#                   '@Microsoft JhengHei', 'Microsoft JhengHei UI', '@Microsoft JhengHei UI', 'Microsoft JhengHei Light', '@Microsoft JhengHei Light',
#                   'Microsoft JhengHei UI Light', '@Microsoft JhengHei UI Light', 'Microsoft New Tai Lue', 'Microsoft PhagsPa',
#                   'Microsoft Sans Serif', 'Microsoft Tai Le', 'Microsoft YaHei', '@Microsoft YaHei', 'Microsoft YaHei UI', '@Microsoft YaHei UI',
#                   'Microsoft YaHei Light', '@Microsoft YaHei Light', 'Microsoft YaHei UI Light', '@Microsoft YaHei UI Light', 'Microsoft Yi Baiti',
#                   'MingLiU-ExtB', '@MingLiU-ExtB', 'PMingLiU-ExtB', '@PMingLiU-ExtB', 'MingLiU_HKSCS-ExtB', '@MingLiU_HKSCS-ExtB',
#                   'Mongolian Baiti', 'MS Gothic', '@MS Gothic', 'MS UI Gothic', '@MS UI Gothic', 'MS PGothic', '@MS PGothic', 'MV Boli',
#                   'Myanmar Text', 'Nirmala UI', 'Nirmala UI Semilight', 'Palatino Linotype', 'Segoe MDL2 Assets', 'Segoe Print',
#                   'Segoe Script', 'Segoe UI', 'Segoe UI Black', 'Segoe UI Emoji', 'Segoe UI Historic', 'Segoe UI Light', 'Segoe UI Semibold',
#                   'Segoe UI Semilight', 'Segoe UI Symbol', 'SimSun', '@SimSun', 'NSimSun', '@NSimSun', 'SimSun-ExtB', '@SimSun-ExtB', 'Sitka Small', 'Sitka Text', 'Sitka Subheading', 'Sitka Heading', 'Sitka Display', 'Sitka Banner', 'Sylfaen', 'Symbol', 'Tahoma', 'Times New Roman', 'Times New Roman Baltic', 'Times New Roman CE', 'Times New Roman CYR', 'Times New Roman Greek', 'Times New Roman TUR', 'Trebuchet MS', 'Verdana', 'Webdings', 'Wingdings', 'Yu Gothic', '@Yu Gothic', 'Yu Gothic UI', '@Yu Gothic UI', 'Yu Gothic UI Semibold', '@Yu Gothic UI Semibold', 'Yu Gothic Light', '@Yu Gothic Light', 'Yu Gothic UI Light', '@Yu Gothic UI Light', 'Yu Gothic Medium', '@Yu Gothic Medium', 'Yu Gothic UI Semilight', '@Yu Gothic UI Semilight', 'HoloLens MDL2 Assets', 'MS Outlook', 'Book Antiqua', 'Century Gothic', 'Bookshelf Symbol 7', 'MS Reference Sans Serif', 'MS Reference Specialty', 'Freestyle Script', 'Juice ITC', 'Kristen ITC', 'Lucida Handwriting', 'Mistral', 'Tempus Sans ITC', 'Garamond', 'Monotype Corsiva', 'Bookman Old Style', 'Algerian', 'Baskerville Old Face', 'Bauhaus 93', 'Bell MT', 'Berlin Sans FB', 'Berlin Sans FB Demi', 'Bernard MT Condensed', 'Bodoni MT Poster Compressed', 'Britannic Bold', 'Broadway', 'Brush Script MT', 'Californian FB', 'Centaur', 'Chiller', 'Colonna MT', 'Cooper Black', 'Footlight MT Light', 'Harlow Solid Italic', 'Harrington', 'High Tower Text', 'Jokerman', 'Kunstler Script', 'Lucida Bright', 'Lucida Calligraphy', 'Lucida Fax', 'Magneto', 'Matura MT Script Capitals', 'Modern No. 20', 'Niagara Engraved', 'Niagara Solid', 'Old English Text MT', 'Onyx', 'Parchment', 'Playbill', 'Poor Richard', 'Ravie', 'Informal Roman', 'Showcard Gothic', 'Snap ITC', 'Stencil', 'Viner Hand ITC', 'Vivaldi', 'Vladimir Script', 'Wide Latin', 'Century', 'Wingdings 2', 'Wingdings 3', 'Arial Unicode MS', '@Arial Unicode MS', 'MS Mincho', '@MS Mincho', 'Noto Sans', 'Bowlby One SC', 'Cabin Sketch', 'Cookie', 'Doppio One', 'Courgette', 'Dead Kansas', 'Euphorigenic', 'Great Vibes', 'Kalam Light', 'Kalam', 'Lemon', 'Limelight', 'Megrim', 'Montserrat Subrayada', 'Permanent Marker', 'Russo One', 'Sigmar One', 'Yellowtail', 'Arial Narrow', 'The Light Font', 'Gloss And Bloom', 'Futurist Fixed-width', 'Earth Orbiter', 'Earth Orbiter 3D', 'Earth Orbiter 3D Italic', 'Earth Orbiter Leftalic', 'Earth Orbiter Outline', 'Earth Orbiter Outline Italic', 'Earth Orbiter Punch', 'Earth Orbiter Punch Italic', 'Earth Orbiter Semi-Italic', 'Earth Orbiter Super-Italic', 'Earth Orbiter Title', 'Earth Orbiter Title Italic', 'Earth Orbiter Extra-Bold', 'Earth Orbiter Extra-Bold Italic', 'Earth Orbiter Academy', 'Earth Orbiter Academy Italic', 'Earth Orbiter Bold', 'Earth Orbiter Bold Italic', 'Earth Orbiter Condensed', 'Earth Orbiter Condensed Italic', 'Earth Orbiter Deep 3D', 'Earth Orbiter Deep 3D Italic', 'Earth Orbiter Engraved', 'Earth Orbiter Engraved Italic', 'Earth Orbiter Expanded', 'Earth Orbiter Expanded Italic', 'Earth Orbiter Gradient', 'Earth Orbiter Gradient Italic', 'Earth Orbiter Halftone', 'Earth Orbiter Halftone Italic', 'Earth Orbiter Italic', 'Earth Orbiter Laser', 'Earth Orbiter Laser Italic', 'Coyote SemiBold DEMO', 'Cinematografica', 'go around the books', 'Tamuragaki', '@Tamuragaki', 'Neon')
