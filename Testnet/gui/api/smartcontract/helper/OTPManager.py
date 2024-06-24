import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time

generated_otp = None
otp_timestamp = None

def generate_otp():
    global generated_otp, otp_timestamp
    generated_otp = "".join([str(random.randint(0, 9)) for _ in range(6)])
    otp_timestamp = time.time()
    return generated_otp

def send_otp(sender_email, sender_password, recipient_email, subject='Your OTP'):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)

        otp = generate_otp()

        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject

        body = f'Your OTP is: {otp}'
        msg.attach(MIMEText(body, 'plain'))
        msg_string = msg.as_string()

        server.sendmail(sender_email, recipient_email, msg_string)
        server.quit()

        return otp
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def validate_otp(input_otp):
    current_time = time.time()
    if generated_otp is not None and (current_time - otp_timestamp) <= 60:
        if generated_otp == input_otp:
            return True
    return False
