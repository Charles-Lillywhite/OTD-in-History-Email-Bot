import requests
from bs4 import BeautifulSoup
import smtplib
import ssl
from email.message import EmailMessage
from datetime import date


today = date.today().strftime("%b-%d-%Y")
base_URL = 'https://www.onthisday.com/'
topics = ['', 'sport', 'music', 'film-tv']

body = '''
<!DOCTYPE html>
<html>

    <body style = "font-family: Times New Roman, Times, serif; color: white; background-image: url(https://images.unsplash.com/photo-1601887389937-0b02c26b602c?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=627&q=80); background-repeat: no-repeat; background-size: 100% ; background-position: center">
    <div>
    <h1 style = "background-color: #FFFFFF; text-align: center; color: black"> On This Day In History </h1>
    </div>
    <div>
    <p style = "text-align: center; font-size: 175%; margin-top: 20px; margin-bottom: 20px; margin-left: 75px; margin-right: 75px;"> Welcome to another day on planet Earth! Here is your summary of this day in the history of our pale blue dot. </p>
    </div>
    
'''

topic_heads = {'': '  History', 'sport': '  Sport', 'music':'  Music', 'film-tv':'  Film & TV'}
topic_BGCol = {'': '#FBEEE6', 'sport': '#FBEEE6', 'music':'#FBEEE6', 'film-tv':'#FBEEE6'}
topic_headCol = {'': '#F6DDCC', 'sport': '#F6DDCC', 'music':'#F6DDCC', 'film-tv':'#F6DDCC'}
topic_imgs = {'': 'https://images.unsplash.com/flagged/photo-1572392640988-ba48d1a74457?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=764&q=80', 'sport': 'https://images.unsplash.com/photo-1506813561347-cbbdf7b3f520?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=702&q=80', 'music':'https://images.unsplash.com/photo-1518893883800-45cd0954574b?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=734&q=80', 'film-tv':'https://images.unsplash.com/photo-1511721511189-ca0a98b3229e?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=687&q=80'}



for topic in topics:
    
    add = f'''
    <div>
        <h2 style = " margin-left: 75px;margin-right: 75px; margin-bottom: 0px; text-align: center; background-color: #5D6D7E; padding-bottom:3px; padding-top:3px;" > {topic_heads[topic]} </h2> 
        <ul style = "margin-top: 10px; margin-bottom: 110px;margin-left: 60px; margin-right: 60px; background-color: #34495E; padding-left: 0;"> 
        '''
    
    
    page = requests.get(base_URL+topic)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find('div', class_ = 'section no-padding-top no-padding-bottom').find_all('ul', class_ = "event-list event-list--with-advert")
    all_events = []
    for r in range(len(results)):
        events = results[r].find_all('li', class_='event')
        events = [e.text for e in events]
        all_events += events

    for e in all_events:
        yr = str(e[0:4])+ ':'
        desc = str(e[4:]) + '.'
        t = yr + '\t' + desc + '\n'
        add += f'''
            <li> <b> {yr} </b> {desc} </li>
            '''
    add += '''
    </ul>
    </div>
    
    
    '''
    body += add

body += '''
<div>
<p style = "color: White; font-size: 150%; text-align: center; margin-top: 160px; margin-bottom: 30px; marigin-left: 30px" > That's all for today, I'll be back again tomorrow! </p>
</div>
</body>
</html>

'''
#print(body)


    
email_sender = # removed for security
email_password = # removed for security
email_receiver = # removed for security


subject = 'OTD In History'
    
em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body, subtype = 'html')

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
   smtp.login(email_sender, email_password)
   smtp.sendmail(email_sender, email_receiver, em.as_string())
    
    
