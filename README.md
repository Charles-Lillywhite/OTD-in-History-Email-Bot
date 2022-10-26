# OTD-in-History-Email-Bot

These are various scripts I have written for a web scraper, which obtains information about events which occured on this day in history.
The files in this repository are as follows:

 - scrape_CLI.py
  An interactive command-line-interface which lets the user pick a date in history, and a subject, then retrieves the relevant information and displays the results.
  
 - scrape_email.py
  Automated bot to retrieve the information and send it to a list of email addresses. The email format is plain text only. This script is automated to run every morning using Mac's crontab.
  
 - scrape_email_HTML.py
  As above, but the email is formatted nicely using HTML syntax. 
