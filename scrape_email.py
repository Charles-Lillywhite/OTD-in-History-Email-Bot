# import necessary modules
import requests
from bs4 import BeautifulSoup
import smtplib
import ssl
from email.message import EmailMessage
from datetime import date

# Get today's date for the email intro
today = date.today().strftime("%b-%d-%Y")


### SCRAPING ###

# topics to identify which pages to scrape
topics = ['', 'sport', 'music', 'film-tv']

base_URL = 'https://www.onthisday.com/'

body = f'ON THIS DAY IN HISTORY \n \n Another day on planet Earth! Here is your summary of {today} in the history of our pale blue dot. \n \n HISTORY'

for topic in topics:
    
    body += topic.upper() + ':'
    body += '\n \n'
    
    
    page = requests.get(base_URL+topic)                    # specific URL
    soup = BeautifulSoup(page.content, 'html.parser')      # make soup
    results = soup.find('div', class_ = 'section no-padding-top no-padding-bottom').find_all('ul', class_ = "event-list event-list--with-advert")  # events only, no other html elements


    all_events = []

    for r in range(len(results)):
        events = results[r].find_all('li', class_='event') # find events within soup
        events = [e.text for e in events] # only interested in the string
        all_events += events

    for e in all_events:
        yr = str(e[0:4])+ ':'
        desc = str(e[4:]) + '.'
        t = yr + '\t' + desc + '\n'
        body += t
    
    body += '\n \n'

body += " That's all for today, I'll be back tomorrow with more great historical facts!"
    

### EMAILING ###

# email sender/recipient
email_sender = # retracted for privacy
email_password = # retracted for privacy
email_receiver = # retracted for privacy

# email subject
subject = 'OTD In History'

# email class
em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

# security
context = ssl.create_default_context() 

# send emails using smtp
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
    
# then automate the script on MacOS using crontab!
