import RPi.GPIO as GPIO
import time
import smtplib

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
GMAIL_USERNAME = 'manmeetmarwahaa@gmail.com'
GMAIL_PASSWORD = 'PERIPERIonpizza'

class Emailer:
    def sendmail(self, recipient, subject, content):
        headers = ["FROM: " + GMAIL_USERNAME, "Subject: " + subject, "To: " + recipient, "MIME-Version: 1.0", "Content-Type: text/html"]
        headers = "\r\n".join(headers)

        session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        session.ehlo()
        session.starttls()
        session.ehlo()

        session.login(GMAIL_USERNAME, GMAIL_PASSWORD)

        session.sendmail(GMAIL_USERNAME, recipient, headers + "\r\n\r\n" + content)
        session.quit

sender = Emailer()

GPIO.setmode(GPIO.BCM)
PIR_PIN = 17
GPIO.setup(PIR_PIN, GPIO.IN)

try:
    print("PIR Module Test (CTRL+C to exit)")
    time.sleep(2)
    print("Ready")
    while True:
        if GPIO.input(PIR_PIN):
            print("Motion Detected!")
            sendTo = 'mtmarwaha@gmail.com'
            emailSubject = "Motion Detected"
            emailContent = "Baby May be Awake"
            sender.sendmail(sendTo, emailSubject, emailContent)
            print("Email sent")
        time.sleep(1)
except KeyboardInterrupt:
    print("Quit")
    GPIO.cleanup()


