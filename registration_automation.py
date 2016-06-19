# http://www.voidynullness.net/blog/2013/07/25/gmail-email-with-python-via-imap/
import sys
import imaplib
import getpass
import email
import datetime

gmail = imaplib.IMAP4_SSL('imap.gmail.com')

try:
    gmail.login('alicia.fremling@gmail.com', getpass.getpass())
except imaplib.IMAP4.error:
    print "Login Failed"
    
rv, data = gmail.select("Test Label")
# in production, this will be "Connected Health/Happy Fun Time"
if rv == 'OK':
    # if a message has not been read (!= \seen) then get the date, name and email
    
    print "Processing mailbox...\n"
    
# print number of unread emails in folder 
# http://stackoverflow.com/questions/953561/check-unread-count-of-gmail-messages-with-python
print len(gmail.search(None, 'UnSeen')[1][0].split()) 



status, email_subjects = gmail.search(None, '(UNSEEN)')
print email_subjects


# def get_emails(email_ids):
#     data = []
#     for e_id in email_ids:
#         _, response = imap_server.fetch(e_id, '(UID BODY[TEXT])')
#         data.append(response[0][1])
#     return data
# 
# def get_subjects(email_ids):
#     subjects = []
#     for e_id in email_ids:
#         _, response = imap_server.fetch(e_id, '(body[header.fields (subject)])')
#         subjects.append( response[0][1][9:] )
#     return subjects
#     
# firstline = gmail.readline()
# print firstline
# 
print "it worked!"
# 
# 
# msg.get_payload()
# 

gmail.logout()
# rv, mailboxes = gmail.list()
# if rv == 'OK':
#     print "Mailboxes:"
#     print mailboxes

# WRITE INTO SPREADSHEET
# http://james-says.blogspot.com/2007/07/beginners-guide-for-google-spreadsheet.html
# gd_client = gdata.spreadsheet.service.SpreadsheetsService()
# gd_client.email = 'your_username'
# gd_client.password = 'your_password'
# gd_client.ProgrammaticLogin()
