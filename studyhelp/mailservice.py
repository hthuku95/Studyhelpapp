import smtplib

GMAIL_USER = 'studyhelp312@gmail.com'
GMAIL_PASSWORD = '$6085hto'
SENT_FROM = 'studyhelp312@gmil.com'
TO = ['studyhelp312@gmail.com']
SUBJECT = 'Good morning'
BODY = 'consectetur adipiscing elit'
EMAIL_TEXT = """\
From: %s
To: %s
Subject: %s

%s
""" % (SENT_FROM, ", ".join(TO), SUBJECT, BODY)

class SendMail:
    def __init__(self,gmail_user,gmail_password,email_text,sent_from,to,subject,body):
        self.gmail_user = gmail_user
        self.gmail_password = gmail_password

        self.email_text = email_text

        self.sent_from = sent_from
        self.to = to
        self.subject = subject
        self.body = body

    def send_mail(self):
        try:
            smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            smtp_server.ehlo()
            smtp_server.login(self.gmail_user, self.gmail_password)
            smtp_server.sendmail(self.sent_from, self.to, self.email_text)
            smtp_server.close()
            print ("Email sent successfully!")
        except Exception as ex:
            print ("Something went wrong….",ex)

my_mail = SendMail(GMAIL_USER, GMAIL_PASSWORD, EMAIL_TEXT, SENT_FROM, TO, SUBJECT, BODY)

my_mail.send_mail()







