import imaplib
import getpass

# Get username & password

username =  input("Enter the email address: ")
password = getpass.getpass("Enter password: ")
mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login(username, password)
mail.select("INBOX")

# Trashing all unread emails

results, messages = mail.search(None, 'UNSEEN')
messages = messages[0].split()
for x in messages:
  result, message = mail.store(x, '+X-GM-LABELS', '\\Trash')
mail.close()
mail.logout()

# # Trashing all emails with a particular subject

# results, messages = mail.search(None, '(SUBJECT "Title")')
# messages = messages[0].split()
# for x in messages:
#   result, message = mail.store(x, '+X-GM-LABELS', '\\Trash')
# mail.close()
# mail.logout()

# # Trashing all emails from a specific sender

# results, messages = mail.search(None, '(FROM "customerservice@blenderbottle.com")')
# messages = messages[0].split()
# for x in messages:
#   result, message = mail.store(x, '+X-GM-LABELS', '\\Trash')
# mail.close()
# mail.logout()