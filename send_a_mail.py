import smtplib
smtobj=smtplib.SMTP('smtp.gmail.com',750)
smtobj.ehlo()
smtobj.starttls()
smtobj.login('opencvproject8090@gmail.com','balKUMAR8090')
smtobj.sendmail("balkumarunivision@gmail.com","balkumarvishwakarma@gmail.com",'subject:Daily Report.\n Hi this is balkumar here')
smtobj.quit()
print(smtobj)

