import os
from email.message import EmailMessage
import ssl
import smtplib
import mimetypes
import csv


body= """
body  
"""

email_sender = 'youremail@gmail.com'
email_password = 'yourpassword'
subject = 'Subject'

csv_list_of_recipients = r"C:\Users\jerem\OneDrive\Documents\Family_medicine_residencies.csv"

first_path = r"C:\Users\jerem\OneDrive\Documents\Important_Documents\Email_Docs"
second_path_1 = 'Deans_Statement_SGU.pdf'
second_path_2="eras_application_2022.pdf"
second_path_3="MD_Diploma.pdf"
second_path_4="MSPE.pdf"
second_path_5="sgu_basic_science.pdf"

all_attachments = [second_path_1,second_path_2, second_path_3, second_path_4, second_path_5]

context = ssl.create_default_context()

with smtplib.SMTP_SSL('SMTP.GMAIL.COM', 465, context=context ) as smtp:
    smtp.login(email_sender, email_password)
    with open (csv_list_of_recipients, newline='') as csvfile:
        content = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in content:
            email_receiver = row
            em = EmailMessage()
            em.set_content(body)
            em['From'] = email_sender
            em['To']= email_receiver
            em['Subject']= subject

            for item in all_attachments:
                attachment_path = first_path+"/" + item
                with open(attachment_path, 'rb') as content_file:
                    content = content_file.read()
                    em.add_attachment(content, maintype='application', subtype='pdf', filename=item)


            smtp.sendmail(email_sender, email_receiver, em.as_string())









