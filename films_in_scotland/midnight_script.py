#!/usr/bin/env python3

import time
import smtplib
from email.message import EmailMessage
from datetime import datetime
from rsync_scotland import rsync_scotland


def send_email(message):
    """
    Sends an email notification.
    """

    sender_email = "davidjohnjohnston@gmail.com"
    sender_password = "hczgsgfeirkpjcva"  # Use an app password, not your normal password

    recipient = "davidjohnjohnston@gmail.com"

    msg = EmailMessage()
    msg["Subject"] = "Midnight rych_scotland Report"
    msg["From"] = sender_email
    msg["To"] = recipient
    msg.set_content(message)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(sender_email, sender_password)
        smtp.send_message(msg)


def midnight_job():
    result = rsync_scotland()

    message = f"""
Hello David,

The midnight rych_scotland task has completed.

Time:
{datetime.now()}

Result:
{result}

Regards,
Midnight Script
"""

    send_email(message)
    print("Email sent.")

    result = rsync_scotland()


def main():
    midnight_job()

if __name__ == "__main__":
    main()

