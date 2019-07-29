import smtplib,ssl

smtp_ser='smtp.gmail.com'
port=465


sender="emailid@gmail.com"
pasw="password"

receiver="sender@gmail.com"
msg="Subject:HI HI HI, how are you"
context=ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_ser,port,context=context) as server:
    server.login(sender,pasw)
    server.sendmail(sender,receiver,msg)
