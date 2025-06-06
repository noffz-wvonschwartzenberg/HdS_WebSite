import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

TEMPLATE = """\
<html>
  <body>
    <p><span style="color: black;">Lieber {0},</span></p>
    <p>
      {1}
    </p>
    <p>
      Kind Regards,<br />
      WebSite - Backend :-)
    </p>
  </body>
</html>
"""

def sendEmail(betreff, body):
    name = "Vorstand - Haus der Sonne"
    recipient_email_address = "w.v.schwartzenberg@hausdersonne-kempen.de"
    sender_email_address = "w.v.schwartzenberg@hausdersonne-kempen.de"
    
    message = MIMEMultipart("alternative")
    message["Subject"] = betreff
    message["From"] = sender_email_address
    message["To"] = recipient_email_address
    message.attach(
        MIMEText(TEMPLATE.format(name, body.replace("\n", "<br>")), "html")
    )
    with smtplib.SMTP_SSL("smtp.ionos.de") as server:
        server.connect("smtp.ionos.de", 465)
        server.login(sender_email_address, "D1A,wfWvSdsv#8We!")
        server.sendmail(
            sender_email_address, recipient_email_address, message.as_string()
        )
