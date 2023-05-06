import pywhatkit as pwk
class WhatsappAPI:

    def __init__(self):
        self._phone_number_from = ""

    def send_whatsapp_message (self, message, subject, phone_number, time_in_hours, time_in_minutes):
         self._phone_number = phone_number #include + and country code
         self._message = message
         self._subject = subject
         self._time_in_hours = time_in_hours
         self._time_in_minutes = time_in_minutes
         # using Exception Handling to avoid unexpected errors
         try:
                  # sending message in Whatsapp in India so using Indian dial code (+91)
                  pwk.sendwhatmsg(self._phone_number, self._message, self._time_in_hours, self._time_in_minutes)
                  print("Message Sent!") #Prints success message in console
         except:
                  print("Error in sending the message")  # error message

if __name__ == '__main__':
    objWhatsappAPI = WhatsappAPI()