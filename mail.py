import smtplib

# https://myaccount.google.com/lesssecureapps
def send(mail,msg):
    rec = mail
    sen = "boda.lakshmikanth@gmail.com"
    passw = "Password@123"
    mess = msg
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sen, passw)
    print ("login succes")
    server.sendmail(sen, rec, mess)
    print ("email sent")

