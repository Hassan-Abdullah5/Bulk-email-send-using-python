import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import csv
import time

# Email configuration
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587  # Gmail's TLS port
EMAIL_ADDRESS = 'hassanabdullah5353@gmail.com'
EMAIL_PASSWORD = 'xnfpppdqmgbqulns'  # Replace with your generated app password

# CSV file path
CSV_FILE = 'chapter_1/test.csv'

# Email content template
subject = 'Transform Your Business with ARF Services'
message_template = """
Dear {first_name} {last_name},

I hope you're doing well. I wanted to reach out and introduce ARF Services to you. We specialize in creating digital solutions that can help your business grow and succeed.

At ARF Services, we're passionate about turning ideas into reality. Whether you need to improve your online presence, streamline operations, or create eye-catching designs, our team is here to help.

We understand the challenges businesses face today and are committed to delivering solutions that go beyond expectations. I would love to discuss how we can specifically help your business.

Could we set up a quick call?

Best regards,

ARF Services Team
[Website: https://arfservices.com/]
"""

def send_email(first_name, last_name, email):
    msg = MIMEMultipart()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = email
    msg['Subject'] = subject

    # Customize message with recipient's first and last name
    message_text = message_template.format(first_name=first_name, last_name=last_name)
    msg.attach(MIMEText(message_text, 'plain'))

    try:
        # Connect to SMTP server
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()  # Upgrade the connection to a secure, encrypted connection
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        
        # Send email
        server.sendmail(EMAIL_ADDRESS, email, msg.as_string())
        print(f'Email sent to {email} successfully!')
    
    except smtplib.SMTPAuthenticationError as e:
        print(f'Failed to authenticate. Check your credentials. Error: {str(e)}')
    
    except smtplib.SMTPException as e:
        print(f'Failed to send email to {email}. SMTP error occurred: {str(e)}')
    
    except Exception as e:
        print(f'Failed to send email to {email}. Error: {str(e)}')
    
    finally:
        # Disconnect from the server
        if 'server' in locals():
            server.quit()

# Read CSV file and send emails
try:
    with open(CSV_FILE, 'r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            first_name = row['first_name']
            last_name = row['last_name']
            email = row['email']

            # Send email to each recipient
            send_email(first_name, last_name, email)
            time.sleep(1)  # Add a delay to avoid overwhelming the SMTP server

except FileNotFoundError:
    print(f'CSV file "{CSV_FILE}" not found.')

except Exception as e:
    print(f'Error processing CSV file: {str(e)}')
