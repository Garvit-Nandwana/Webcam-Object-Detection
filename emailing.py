import smtplib
import imghdr
from email.message import EmailMessage

# The Credentials
PASSWORD = "<your google app-password>"
SENDER = "<sender-email>"
RECEIVER = "<receiver-email>"


def send_email(image_path):
    print("send_email function started")
    try:
        # Creating the email message
        email_message = EmailMessage()

        email_message["Subject"] = "New customer showed up"

        email_message.set_content("Hey we just saw a new customer!")

        with open(image_path, 'rb') as file:
            content = file.read()

        email_message.add_attachment(content, maintype="image", subtype=imghdr.what(None, content))

        # Creating gmail server

        gmail = smtplib.SMTP("smtp.gmail.com", 587)
        gmail.ehlo()
        gmail.starttls()
        gmail.login(SENDER, PASSWORD)
        gmail.sendmail(SENDER, RECEIVER, email_message.as_string())
        gmail.quit()

        print("Email sent successfully!")

    except Exception as e:
        print(f"Error sending email: {e}")

    print("send_email function ended")


if __name__ == "__main__":
    send_email(image_path="images/11.png")
