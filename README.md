🛡️ File Integrity Monitoring (FIM) Tool
Overview

This Python-based File Integrity Monitoring (FIM) tool is designed to monitor a specified directory for any unauthorized changes, additions, or deletions of files. By computing and comparing SHA-256 hashes of files at regular intervals, the tool ensures the integrity of your files and alerts you to any unexpected modifications.
Features

    Real-time Monitoring: Continuously observes a specified directory for file changes.

    Hash Verification: Utilizes SHA-256 hashing to detect alterations in file content.

    Email Notifications: Sends alerts via email upon detecting any file changes.

    Customizable Settings: Allows users to configure monitoring intervals and email settings.

Getting Started
Prerequisites

    Python 3.x installed on your system.

    Access to a Gmail account with App Passwords enabled if 2-Step Verification is active.

Installation

    Clone the Repository:

git clone https://github.com/anshuman-dev-seekhoon/FileIntegrityMonitor/
cd FileIntegrityMonitor

Configure Settings:

    Open the fim.py file.

    Set the DIRECTORY_TO_MONITOR variable to the path of the directory you wish to monitor.

    Update the email configuration section with your Gmail credentials and the recipient's email address.

Run the Tool:

    python3 fim.py

Configuration

In the fim.py script, you'll find the following configuration section:

# --- CONFIGURATION ---
DIRECTORY_TO_MONITOR = "./fim_test"  # Directory to monitor
CHECK_INTERVAL = 10  # Interval in seconds between checks
EMAIL_ALERTS = True  # Enable or disable email alerts

# Email Settings
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_ADDRESS = "your_email@gmail.com"         # Your Gmail address
EMAIL_PASSWORD = "your_app_password_here"      # App password if 2FA is enabled
TO_EMAIL = "receiver_email@gmail.com"          # Recipient's email address

Ensure that:

    EMAIL_ADDRESS is your Gmail address.

    EMAIL_PASSWORD is an App Password generated from your Google Account.

    TO_EMAIL is the email address where you want to receive alerts.

How It Works

    Initial Snapshot: The tool takes an initial snapshot of the specified directory, recording the SHA-256 hash of each file.

    Continuous Monitoring: At intervals defined by CHECK_INTERVAL, the tool rescans the directory and computes the current hashes.

    Comparison: The new hashes are compared with the initial snapshot to detect:

        New files added.

        Existing files modified.

        Files deleted.

    Alerting: If EMAIL_ALERTS is set to True, the tool sends an email notification detailing the change.

Use Cases

    Security Monitoring: Detect unauthorized changes to critical system files.

    Compliance: Ensure file integrity for compliance with standards like PCI DSS, HIPAA, etc.

    Data Protection: Monitor sensitive directories to prevent data tampering.

Contributing

Contributions are welcome! If you have suggestions for improvements or new features, feel free to fork the repository and submit a pull request.
