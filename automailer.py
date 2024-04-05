import os
import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders

# Customizable fields
subject = "Automated Multimail"
footer_text = "This is an automated message. Please do not reply."
setRemove = True
fullSend = False
singleMail = True
pdfRename = True
pdfRenameCustom = True
filename = "Renamed PDF"

# Read the config file
try:
    with open('config.json', 'r') as f:
        data = json.load(f)
except FileNotFoundError:
    print("Config file not found. Please check the file path.")
    exit(1)

# Extract the contacts and email credentials from the json data
config = data.get('contacts', {})
host = data.get('host', {})

# Directory containing the PDF files
pdf_folder = './documents'

# Email settings
smtp_server = 'smtp-mail.outlook.com'
smtp_port = 587

# Establish a secure session with outlook's outgoing SMTP server using your outlook account
try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(host['email'], host['passw'])
except Exception as e:
    print(f"Failed to connect to the email server: {e}")
    exit(1)

# Loop through each person in the config
for person in config.values():
    # Set up the email
    msg = MIMEMultipart()
    msg['From'] = host['email']
    msg['To'] = person
    msg['Subject'] = subject

    # Loop through each pdf for the current person
    for pdf in config.keys():
        pdf_path = os.path.join(pdf_folder, f'{pdf}.pdf')
        if not os.path.exists(pdf_path):
            print(f"File {pdf_path} does not exist, skipping.")
            continue

        # If fullSend is False, only attach the document if the pdf name matches the person's name
        if not fullSend and pdf.lower() != person.lower():
            continue

        # If pdfRename is True, rename the pdf file
        if pdfRename:
            if pdfRenameCustom:
                # If pdfRenameCustom is True, rename the pdf file by adding the name of the receiver
                msg['Filename'] = f"{person} {filename}"
            else:
                msg['Filename'] = filename
        else:
            msg['Filename'] = pdf

        # Attach the pdf
        try:
            with open(pdf_path, 'rb') as f:
                attach = MIMEBase('application', 'octet-stream')
                attach.set_payload(f.read())
        except FileNotFoundError:
            print(f"File {pdf_path} not found, skipping.")
            continue

        encoders.encode_base64(attach)
        attach.add_header('Content-Disposition', 'attachment', filename=f"{msg['Filename']}.pdf")
        msg.attach(attach)

        # Remove the file from the directory
        if setRemove:
            try:
                os.remove(pdf_path)
                print(f"Removed {pdf_path}\n")
            except Exception as e:
                print(f"Failed to remove {pdf_path}: {e}")

        # If singleMail is False, send the email after attaching each document
        if not singleMail:
            try:
                # Send the email
                server.send_message(msg)
                # Print the success message
                print(f"Successfully sent {pdf} to {person}")
            except Exception as e:
                print(f"Failed to send email: {e}")

            # Set up a new email for the next document
            msg = MIMEMultipart()
            msg['From'] = host['email']
            msg['To'] = person
            msg['Subject'] = subject

    # If singleMail is True, send the email after attaching all documents
    if singleMail:
        # Add footer text
        msg.attach(MIMEText(footer_text, 'plain'))

        try:
            # Send the email
            server.send_message(msg)
            # Print the success message
            print(f"Successfully sent emails to {person}")
        except Exception as e:
            print(f"Failed to send email: {e}")

# Close the connection to the server
server.quit()