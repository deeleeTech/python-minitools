from email import message
from email.message import EmailMessage
import smtplib


fromaddr = "deeleetech@gmail.com"
toaddr = "dillon_lee@live.com"

htmlHeader = "Welcome"
htmlText = "This is sent frm python and the smptlib library... and it worked!!!!"

html = f"""
<html>
    <body>
        <h1>{htmlHeader}</h1>
        <br/>
        <p>{htmlText}</p>
    </body>
</html>
"""

# html = open("testHTML.html")
msg = EmailMessage()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Automatic Weekly Report"

msg.add_alternative(html, subtype="html")

debug = False
if debug:
    print(msg.as_string())
else:
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login("deeleetech@gmail.com", "fuckXbox225!")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    print('SENT SUCESS!!!!')
    server.quit()