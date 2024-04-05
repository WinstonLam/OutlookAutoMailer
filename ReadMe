# Automated Email Sender with Attachments 📧🚀

This Python script allows you to send automated emails with PDF attachments to multiple recipients. It's perfect for sending out newsletters, reports, or any other documents via email.

## Setup 🛠️

1. Clone this repository to your local machine.
2. Install the required Python libraries by running `pip install smtplib json email os`.

## Configuration 📝

You need to configure the script to your needs by editing the following fields:

- `subject`: The subject line of the email.
- `footer_text`: The footer text of the email.
- `setRemove`: If set to `True`, the script will remove the PDF file from the directory after sending it.
- `fullSend`: If set to `True`, the script will send all PDFs to all contacts. If `False`, it will only send the PDFs that match the contact's name.
- `singleMail`: If set to `True`, the script will send a single email with all PDFs attached. If `False`, it will send an email for each PDF.
- `pdfRename`: If set to `True`, the script will rename the PDF file before sending it.
- `pdfRenameCustom`: If set to `True`, the script will rename the PDF file by adding the name of the receiver.
- `filename`: The new filename for the PDF if `pdfRename` is `True`.

## Configuring the Contacts and Host 📇

The script reads the contacts and the host email from a `config.json` file. An example file `example-config.json` is provided.

The `config.json` file should have the following structure:

```json
{
  "contacts": {
    "john": "John@hotmail.com",
    "lisa": "Lisa@outlook.com"
  },
  "host": {
    "email": "lisadoe@hotmail.com",
    "passw": "password1234"
  }
}
```

- `contacts`: An object where each key is the name of a contact and the corresponding value is their email address.
- `host`: An object representing the host email. It should have an email and a passw (password).

Important: Don't forget to remove the example- part before the config.json filename before running the script.

## Running the Script 🏃‍♂️

To run the script, navigate to the directory containing the script in your terminal and run python script_name.py.

## Enjoy your automated emails! 🎉💌
