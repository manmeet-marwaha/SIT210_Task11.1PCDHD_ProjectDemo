from time import daylight
import Adafruit_DHT
import time
import smtplib
import RPi.GPIO as GPIO

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

DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 2

while True:
    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
    if humidity is not None and temperature is not None:
        print("Temp={0:0.1f}C Humidity={1:0.1f}%".format(temperature, humidity))
        sendTo = 'mtmarwaha@gmail.com'
        emailSubject = "Readings for Temperature and Humidity"
        emailContent = "Temp={0:0.1f}C Humidity={1:0.1f}%".format(temperature, humidity)
        sender.sendmail(sendTo, emailSubject, emailContent)
        print("Email sent")
    else:
        print("Sensor failure. Check wiring")
    time.sleep(3)