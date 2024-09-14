import smtplib
import pandas as pd
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Load recipients from a CSV file (or you can define a list within the script)
def load_recipients(csv_file):
    return pd.read_csv(csv_file)['Email'].tolist()

# Function to send email
def send_email(sender_email, sender_password, subject, body, recipients):
    # Define SMTP server details
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    
    # Set up the SMTP server connection
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(sender_email, sender_password)

    for recipient in recipients:
        try:
            # Create the email headers and body
            msg = MIMEMultipart()
            msg['From'] = sender_email
            msg['To'] = recipient
            msg['Subject'] = subject
            
            # Attach the email body
            msg.attach(MIMEText(body, 'plain'))
            
            # Send the email
            server.sendmail(sender_email, recipient, msg.as_string())
            print(f"Email sent to {recipient}")
        
        except Exception as e:
            print(f"Failed to send email to {recipient}: {e}")
    
    # Close the SMTP server connection
    server.quit()

if __name__ == "__main__":
    # Sender's credentials
    sender_email = "marouanedbibih.developer@gmail.com"
    sender_password = "ivhk dyml qsum eavv"  # Use an app-specific password for Gmail

    # Email content
    subject = "Important Notice"
    body = "This is a test email sent using Python script."

    # Load recipients from a CSV file (or replace this line with a hardcoded list of emails)
    recipients_file = 'recipients.csv'  # File containing a column 'Email'
    recipients = load_recipients(recipients_file)

    # Send the email to all recipients
    send_email(sender_email, sender_password, subject, body, recipients)
