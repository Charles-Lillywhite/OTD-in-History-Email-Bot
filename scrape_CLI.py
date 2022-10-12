# import necessary modules
import requests
from bs4 import BeautifulSoup
from datetime import date

### SCRAPING ###

base_URL = 'https://www.onthisday.com/'

topics = ['', 'sport', 'music', 'film-tv']
months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']

days_30 = [months[3],months[5], months[8], months[10]]
days_31 = [months[0],months[2], months[4], months[6], months[7],  months[9], months[11]]

print('\n')
print('Please select a month from 1 - 12 ( 1 = Jan, ..., 12 = Dec)')
m = int(input('Month = '))

while m not in range(1, 12+1):
    print('Please select a valid month')
    m = int(input('Month = '))
    
month = months[int(m) - 1]
print('\n')
print(f'Month selected = {month.capitalize()}')
print('\n')

maxday = 0
if month in days_30:
    maxday += 30
elif month == 'february':
    maxday += 28
else:
    maxday += 31
#print('maxday = ', maxday)

print(f'Please select a day from 1 - {maxday}')
day = int( input('Day = ') )

while day not in range(1, maxday):
    print('Please select a valid day')
    day = int( input('Day = ') )
print('\n')
print(f'Day selected = {day}')
print('\n')

print('Please select a Topic:  \n 1 = History \n 2 = Sport \n 3 = Music \n 4 = Film & TV')
top = int( input('Topic = '))
while top not in range(1, 4+1):
    print('Please select a valid topic')
    top = int( input('Topic = '))
topic = topics[int(top) - 1 ]

hist_correction = ''
if top == 1:
    hist_correction = 'HISTORY'

print('\n')
print(f'Topic selected = {topics[top-1].capitalize()}' + hist_correction)
print('\n')


URL = base_URL + str(topic) +  '/' + str(month) + '/' + str(day)


body = '\n \n'  +  topic.upper() + hist_correction + ':'  +  '\n \n'
    
    
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
    body += t
    
body += '\n \n'

    
print(body)
    
    
