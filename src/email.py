from smtplib import SMTP 
from os import getenv
from typing import List, Optional  
from email.mime.multipart  import MIMEMultipart 
from email.mime.text import MIMEText 


class Email:

    def __init__(self) -> None:
        self.server = SMTP(
            host=getenv('SMTP_HOSTNAME'),
            port=getenv('SMTP_TLS_PORT')
        )

    """
        conn_server permite establecer conexion con el host de gmail
    """

    def connect_server(self):
        self.server.starttls()
        self.server.login( 
            user=getenv('SMTP_USER'),
            password=getenv('SMTP_PASSWORD')
        )

    def send_email(self, emails: List[str], subject: Optional[str], **kwargs): # list is not defined
        self.connect_server()
        print("Sending emal...")
        for email in emails:
            mine = MIMEMultipart()

            mine['From'] = getenv('SMTP_USER')
            mine['To'] = email
            mine['Subject'] = subject
            format = MIMEText(kwargs['message_format'], kwargs['format'])
            mine.attach(format) 
            try:
                self.server.sendmail(getenv('SMTP_USER'), email, mine.as_string())
            except Exception as e:
                raise e
            finally:
                self.disconnect_server()

    def disconnect_server(self):
        self.server.quit()
        self.server.close()