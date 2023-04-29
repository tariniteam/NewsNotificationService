#import pywhatkit
#import bs4
#import smtplib
#import requests
import pywhatkit as pwk

# using Exception Handling to avoid unexpected errors
try:
    # sending message in Whatsapp in India so using Indian dial code (+91)
    pwk.sendwhatmsg("+48724857234", "Hello, World", 16, 38)

    print("Message Sent!")  # Prints success message in console

    # error message
except:
    print("Error in sending the message")