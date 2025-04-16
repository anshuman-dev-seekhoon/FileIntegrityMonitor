import os
import time
import hashlib
import smtplib
from email.mime.text import MIMEText
from datetime import datetime

# --- CONFIGURATION ---
DIRECTORY_TO_MONITOR = "/home/anshuman/Desktop/tools"  # Change this to the folder you want to monitor
CHECK_INTERVAL = 10  # Check every 10 seconds
EMAIL_ALERTS = True  # Set to False to disable email alerts

# Email Settings
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_ADDRESS = "youremail"         # Your email
EMAIL_PASSWORD = "seeyourpassword "      # App password if 2FA is on
TO_EMAIL = "reciever@gmail.com"          # Who gets the alert


def getfile_hash(filepath):
    try:
        with open(filepath, "rb") as f:  # Open the file in binary mode
            file_data = f.read()
            return hashlib.sha256(file_data).hexdigest()
    except Exception:
        return None


# This function takes the snapshot of the given directory 
def snapshot_directory(directory):
    snapshot = {}
    for root, dirs, files in os.walk(directory):
        for filename in files:  # just hashing the files inside that directory
            full_path = os.path.join(root, filename)  # thus firstly finding the absolute path of the file and then would be adding and hashing that path
            # like for example the above line works in this way: "C:/Users/Sam/Documents" + "report.pdf" → "C:/Users/Sam/Documents/report.pdf"
            file_hash = getfile_hash(full_path)
            if file_hash:  # if the hash of the file is already present
                snapshot[full_path] = file_hash    # Only proceed if hashing succeeded
    return snapshot


# Sending email alert
def send_email_alerts(subject, body):
    msg = MIMEText(body)
    msg["Subject"] = subject 
    msg["From"] = EMAIL_ADDRESS
    msg["TO"] = TO_EMAIL
    
    try: 
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)
            print("EMAIL SENT !!  :)")
    except Exception as e:
        print(f"Failed to send the email: {e} :( ")
    

# Main working of the code begins from here            
print(f"File monitoring on {DIRECTORY_TO_MONITOR} begins")
previous_snapshot = snapshot_directory(DIRECTORY_TO_MONITOR)
while True:
    time.sleep(CHECK_INTERVAL)
    current_snapshot = snapshot_directory(DIRECTORY_TO_MONITOR)
    
    # Checking for the newly added or modified files
    for path in current_snapshot:
        if path not in previous_snapshot:
            msg = f"[{datetime.now()}] New file added : {path}"
            print(msg)
            if EMAIL_ALERTS:
                send_email_alerts("File Added!!", msg)
                
        elif path in previous_snapshot:
            if(current_snapshot[path] != previous_snapshot[path]):
                msg = f"[{datetime.now()}] File modified: {path}"
                print(msg)
                if EMAIL_ALERTS:
                    send_email_alerts("File Modified!!", msg)

    # Now checking for the deleted ones
    for path in previous_snapshot:
        if path not in current_snapshot:
            msg = f"[{datetime.now()}] File Deleted : {path}"
            print(msg)
            if EMAIL_ALERTS:
                send_email_alerts("File Deleted !!", msg)

    previous_snapshot = current_snapshot.copy()
