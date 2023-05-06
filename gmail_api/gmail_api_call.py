import smtplib
import ssl

class GmailAPI:

    def __init__(self, ):
        # Declare port number and server name
        self.smtp_port = 587   # Standard secure SMTP port
        self.smtp_server = "smtp.gmail.com"  # Google SMTP Server
        self.email_from = "tariniteam@gmail.com"
        self.email_to = "harsha.navalkar@gmail.com"
        self.pswd = "vrltlgwaasphvjkf"
        self.message =  "Testing Email!!!"  # content of message

    def send_email (self):
       # Create context
       simple_email_context = ssl.create_default_context()
       try:
          # Connect to the server
          print("Connecting to server...")
          TIE_server = smtplib.SMTP(smtp_server, smtp_port)
          TIE_server.starttls(context=simple_email_context)
          TIE_server.login(email_from, pswd)
          print("Connected to server :-)")
    
          # Send the actual email
          print()
          print(f"Sending email to - {email_to}")
          TIE_server.sendmail(email_from, email_to, message)
          print(f"Email successfully sent to - {email_to}")

        # If there's an error, print it out
       except Exception as e:
          print(e)

       # Close the port
       finally:
          TIE_server.quit()

if __name__ == '__main__':
    objGmailAPI = GmailAPI()
    objGmailAPI.send_email()
