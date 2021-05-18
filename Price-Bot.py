import requests
from selenium import webdriver
import smtplib, ssl
import schedule
import time

def verify():
	req = requests.get('https://www.amazon.com/GTA-Guide-Walkthrough-Tips-Hints/dp/B08RGVMWSK/ref=sr_1_1?dchild=1'
	                   '&keywords=gta+5 '
	                   '&qid=1617218437&s=books&sr=1-1', headers={
	    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
	                  'Chrome/88.0.4324.192 Safari/537.36 OPR/74.0.3911.218',
	    'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8'})
	driver = webdriver.Chrome(r'D:\Applications\Programs\Automation\chromedriver.exe')

	driver.get('https://www.amazon.com/GTA-Guide-Walkthrough-Tips-Hints/dp/B08RGVMWSK/ref=sr_1_1?dchild=1&keywords=gta+5'
	           '&qid=1617218437&s=books&sr=1-1')

	price = driver.find_element_by_id('price').text
	split_text = price.split('$')
	just_number = split_text[1]
	just_number = float(just_number)

	product_name = driver.find_element_by_id('productTitle').text

	driver.quit()

	BUY_PRICE = 50

	port = 587  # For starttls
	smtp_server = "smtp.gmail.com"
	sender_email = "your@email.com"
	receiver_email = "his@email.com"
	password = 'password'
	message = f"""\
	Subject: Buy NOW!

	The price for {product_name} has dropped to {price}."""

	if just_number < BUY_PRICE:
		context = ssl.create_default_context()
		with smtplib.SMTP(smtp_server, port) as server:
			server.ehlo()  # Can be omitted
			server.starttls(context=context)
			server.ehlo()  # Can be omitted
			server.login(sender_email, password)
			server.sendmail(sender_email, receiver_email, message)
			print('All good!')

schedule.every().day.at("22:28").do(verify)

while True:
    schedule.run_pending()
    time.sleep(1)