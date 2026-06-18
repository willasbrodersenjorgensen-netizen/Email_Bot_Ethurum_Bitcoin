# Email_Bot_Ethurum_Bitcoin
This is an email bot that sends you the prices of ethurum and bitcoin to you every day 


This repository includes a Crypto email bot from the site= https://api.coingecko.com
Ive scraped the site 18-06-2026

What ive learned
Building this project learned me to apply the modules requests, smtplib, email.mime and the datetime module to build an automated email bot. Ive used a simple API= https://api.coingecko.com/api/v3/simple/price to get the live prices of Bitcoin and Ethereum without needing API keys.
Ive have then learned to format that data into a clean HTML table using Python f-strings.
With smtplib and email.mime ive learned to manage secure SMTP connections over SSL (Port 465) to log into Gmail, handle MIME containers, and send formatted HTML emails gracefully.
Ive also used the logging module to document and log each send attempt to a daily_bot.log file with timestamps.
Over all ive spent time learning the exact modules smtplib, email.mime and finaly build a simple crypto price alerter.

What Could be added?
Adding a color-coded temperature indicator or price trend indicator (green for up, red for down).
Scraping the top 3 headlines from a news RSS feed to add daily context to the email.
Using the schedule module to run the script automatically every day at a specific time.
