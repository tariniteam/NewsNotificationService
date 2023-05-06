import smtplib
import ssl

class GmailAPI:

    def __init__(self):
        # Declare port number and server name
        self._smtp_port = 587                   # Standard secure SMTP port
        self._smtp_server = "smtp.gmail.com"    # Google SMTP Server
        self._email_from = "tariniteam@gmail.com"
        self._password = "vrltlgwaasphvjkf"

    #message = "Subject: Test subject\r\n\r\nThis is the body"
    def send_email (self, message, subject, email_to):
       # Create context
       self._subject = subject
       self._message = message
       self._email_to = email_to
       self._simple_email_context = ssl.create_default_context()
       try:
          # Connect to the server
          print("Connecting to server...")
          TIE_server = smtplib.SMTP(self._smtp_server, self._smtp_port)
          TIE_server.starttls(context=self._simple_email_context)
          TIE_server.login(self._email_from, self._password)
          print("Connected to server :-)")
    
          # Send the actual email
          print()
          print(f"Sending email to - {self._email_to}")
          TIE_server.sendmail(self._email_from, self._email_to, self._message)
          print(f"Email successfully sent to - {self._email_to}")

        # If there's an error, print it out
       except Exception as e:
          print(e)

       # Close the port
       finally:
          TIE_server.quit()

if __name__ == '__main__':
    objGmailAPI = GmailAPI()

