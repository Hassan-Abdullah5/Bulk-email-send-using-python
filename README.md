# Execution of this Script

Python Installation:
Ensure Python 3.x is installed on your computer. You can download it from python.org.

SMTP Credentials:
You need a Gmail account and an app password. Generate an app password if you have 2-Step Verification enabled on your Gmail account.

Clone the Repository:
git clone https://github.com/Hassan-Abdullah5/Bulk-email-send-using-python.git

cd Bulk-email-send-using-python

Configure Email Settings:
Open the script file (bulk_email_sender.py).
Replace EMAIL_ADDRESS and EMAIL_PASSWORD with your Gmail address and the generated app password.

Prepare CSV File:
Create a CSV file named test.csv.
The CSV file should have the following columns: first_name, last_name, email.

Run the Script:
Execute the script from the terminal or command prompt:
python bulk_email_sender.py
The script will read the CSV file and send emails to each recipient.

Authentication Issues:
Verify that your app password is correct and that you have enabled access for less secure apps if necessary.

File Not Found:
Ensure the CSV file is correctly named and located in the specified directory.
