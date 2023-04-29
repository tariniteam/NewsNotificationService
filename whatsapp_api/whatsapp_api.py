# import time 
# import pywhatkit
# import pyautogui
# from pynput.keyboard import Key, Controller




import pywhatkit as pwk

# using Exception Handling to avoid unexpected errors
try:
     # sending message in Whatsapp in India so using Indian dial code (+91)
     pwk.sendwhatmsg("+919820663554", "Hi, how are you?", 19, 00)

     print("Message Sent!") #Prints success message in console

     # error message
except: 
     print("Error in sending the message")

# keyboard = Controller()


# def send_whatsapp_message(msg: str):
#     try:
#         pywhatkit.sendwhatmsg_instantly(
#             phone_no="+919820663554", 
#             message=msg,
#             tab_close=True
#         )
#         time.sleep(10)
#         pyautogui.click()
#         time.sleep(2)
#         keyboard.press(Key.enter)
#         keyboard.release(Key.enter)
#         print("Message sent!")
#     except Exception as e:
#         print(str(e))

# send_whatsapp_message("Hello Word")