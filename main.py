import random
import datetime as dt
import smtplib
import pandas

EMAIL_SMTP = 'smtp.gmail.com'
GMAIL = 'sample_sender@gmail.com'
PASSWORD = 'sample_password'
SUBJECT = 'Subject:It\'s your Birthday'


date_now = dt.datetime.now()
month = date_now.month
day = date_now.day
df = pandas.read_csv('birthdays.csv')

for (index, rows) in df.iterrows():
    if rows['month'] == month and rows['day'] == day:
        name = rows['name']
        email = rows['email']
        with open(f'letter_templates/letter_{random.randint(1,3)}.txt') as file:
            letter = file.read().replace('[NAME]', name)

        with smtplib.SMTP(EMAIL_SMTP) as connection:
            connection.starttls()
            connection.login(user=GMAIL, password=PASSWORD)
            connection.sendmail(from_addr=GMAIL, to_addrs=email, msg=f'{SUBJECT}\n\n{letter}')
