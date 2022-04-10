from dotenv import load_dotenv

from src.email import Email

html_format = """
    <p>Enviando email </p>
    <p>Buenas noches {0}, este es un segundo mensaje. </p>

"""


def main():
    name = input('What your name? ')
    email = Email()
    email.send_email(['helpdesk.rayner@gmail.com'], 'Testing sending emails', message_format=html_format.format(name), format='html')

if __name__ == '__main__':
    load_dotenv()
    main()