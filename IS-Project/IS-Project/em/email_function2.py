import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import pandas as pd
from tkinter import filedialog


global fob


# def email_send_funct_next(to_, sub_, msg_, from_, pass_):
#     s = smtplib.SMTP("smtp.gmail.com", 587)
#     s.starttls()
#     s.login(from_, pass_)
#     msg = MIMEMultipart()
#     msg['From'] = from_
#     msg['To'] = to_
#     msg['Subject'] = sub_
#     body = msg_
#     msg.attach(MIMEText(body, 'plain'))
#     filename = "test1.xlsx"
#     attachment = open(filename, "rb")
#     data = pd.read_excel(attachment.name)
#     all_emails = data['Email']
#     email2 = all_emails
#     # p = MIMEBase('application', 'octet-stream')
#     # # p.set_payload(attachment.read())
#     # # encoders.encode_base64(p)
#     # p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
#     # msg.attach(p)
#     text = msg.as_string()
#     s.sendmail(from_, email2, text)
#     x = s.ehlo()
#     if x[0] == 250:
#         return "s"
#     else:
#         return "f"
#     s.close()


def attach_single(to_, sub_, msg_, from_, pass_):
    s = smtplib.SMTP("smtp.gmail.com", 587)
    s.starttls()
    s.login(from_, pass_)
    msg = MIMEMultipart()
    msg['From'] = from_
    msg['To'] = to_
    msg['Subject'] = sub_
    body = msg_
    msg.attach(MIMEText(body, 'plain'))
    f_types = [('All Files', '*.*'),
               ('Python Files', '*.py'),
               ('Text Document', '*.txt'),
               ('Excel files', "*.xlsx")]
    file = filedialog.askopenfilename(initialdir='E:',
                                      filetypes=f_types)
    if file:
        fob = open(file, 'rb')
    filename = file
    p = MIMEBase('application', 'octet-stream')
    p.set_payload((fob).read())
    encoders.encode_base64(p)
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    msg.attach(p)
    text = msg.as_string()
    s.sendmail(from_, to_, text)
    x = s.ehlo()
    if x[0] == 250:
        return "s"
    else:
        return "f"
    s.close()

def attach_mul(to_, sub_, msg_, from_, pass_):
    s = smtplib.SMTP("smtp.gmail.com", 587)
    s.starttls()
    s.login(from_, pass_)
    msg = MIMEMultipart()
    msg['From'] = from_
    msg['To'] = to_
    msg['Subject'] = sub_
    body = msg_
    msg.attach(MIMEText(body, 'plain'))
    f_types2 =[('All Files', '*.*'),
              ('Excel Files', '*.xlsx')]
    file2 = filedialog.askopenfilename(initialdir='E:', title = 'Please Select the Excel Sheet',
                                      filetypes=f_types2)
    filename = file2
    attachment = open(filename, "rb")
    data = pd.read_excel(attachment.name)
    all_emails = data['Email']
    email2 = all_emails
    f_types = [('All Files', '*.*'),
               ('Python Files', '*.py'),
               ('Text Document', '*.txt'),
               ('Excel files', "*.xlsx")]
    file = filedialog.askopenfilename(initialdir='E:', title = 'Please Select the attachment',
                                      filetypes=f_types)
    if file:
        fob = open(file, 'rb')
    filename2 = file
    p = MIMEBase('application', 'octet-stream')
    p.set_payload((fob).read())
    encoders.encode_base64(p)
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename2)
    msg.attach(p)
    text = msg.as_string()
    s.sendmail(from_, email2, text)
    x = s.ehlo()
    if x[0] == 250:
        return "s"
    else:
        return "f"
    s.close()