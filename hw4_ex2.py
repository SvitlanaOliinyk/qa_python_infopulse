import smtplib

smtpObj = smtplib.SMTP('smtp.mail.ru', 587)
# smtpObj.ehlo()
smtpObj.starttls()

from_add = 'svetka22.07@mail.ru'
password = 'secret'

smtpObj.login(from_add, password)

mess = '''
I did it!
I'm Sveta Oliinyk. I can't send a mail from 'gmail'. BUT! I'll do it!
And I did other exercises. Can you give me new tasks?
'''
smtpObj.sendmail(from_add, 'el.piankova@gmail.com', mess)

smtpObj.quit()
