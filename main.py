import os
import smtplib
import logging
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import requests

from dotenv import load_dotenv
from creds import password, email

load_dotenv()
logging.basicConfig(
    filename="daily_bot.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

def get_price():
    try:
        url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd"
        response = requests.get(url)
        data = response.json()
        btc_raw = data["bitcoin"]["usd"]
        eth_raw = data["ethereum"]["usd"]
        
        btc_price = f"{btc_raw:,}"
        eth_price = f"{eth_raw:,}"
        return btc_price, eth_price
    except Exception as e:
        logging.error(f"Failed to find crypto prices: {e}")
        print("Fejl: {e}")



def build_html_body(btc, eth):
    html = f"""
    <html>
    <body style="font-family: Arial, sans-serif; color: #333; line-height: 1.6; max-width: 500px; margin: 0 auto; padding: 20px;">
        <h2 style="color: #2c3e50; border-bottom: 2px solid #ecf0f1; padding-bottom: 10px; text-align: center;">Kryptovaluta Priser</h2>
        
        <table style="border-collapse: collapse; width: 100%; box-shadow: 0 2px 3px rgba(0,0,0,0.1); margin-top: 15px;">
            <thead>
                <tr style="background-color: #f8f9fa; border-bottom: 2px solid #dee2e6;">
                    <th style="border: 1px solid #dee2e6; text-align: left; padding: 12px;">Aktiv</th>
                    <th style="border: 1px solid #dee2e6; text-align: left; padding: 12px;">Pris (USD)</th>
                </tr>
            </thead>
            <tbody>
                <tr style="border-bottom: 1px solid #dee2e6;">
                    <td style="border: 1px solid #dee2e6; padding: 12px; font-weight: bold; color: #f2a900;">Bitcoin (BTC)</td>
                    <td style="border: 1px solid #dee2e6; padding: 12px; font-weight: bold;">${btc}</td>
                </tr>
                <tr>
                    <td style="border: 1px solid #dee2e6; padding: 12px; font-weight: bold; color: #3c3c3d;">Ethereum (ETH)</td>
                    <td style="border: 1px solid #dee2e6; padding: 12px; font-weight: bold;">${eth}</td>
                </tr>
            </tbody>
        </table>
    </body>
    </html>
    """
    return html
  
    
  
    



def send_email():

    btc, eth = get_price()

    afsender = email
    modtager = email
    adgangskode = password

    
    msg = MIMEMultipart("alternative")
    msg['Subject'] = "Crypto prices"
    msg['From'] = afsender
    msg['To'] = modtager

    html_content = build_html_body(btc, eth)
    msg.attach(MIMEText(html_content, "html"))

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(afsender, adgangskode)
            server.sendmail(afsender, modtager, msg.as_string())
        
        logging.info(f"Krypto-mail sendt succesfuldt til {modtager}")
        print("Succes: Emailen er blevet sendt og logget!")
    
    except Exception as e:
        logging.error(f"E-mailen couldnt be send: {str(e)}")
        print(f"There has aquired a mistake: {e}. Check the daily_bot for info")

if __name__ == "__main__":
    send_email()
    

   

  