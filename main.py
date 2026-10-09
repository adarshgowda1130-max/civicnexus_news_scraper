import os
import smtplib
from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
from fake_useragent import UserAgent
import random
ua=UserAgent()
load_dotenv()
email=os.getenv("email")
password=os.getenv("password")
to_address=os.getenv("to_address")
url=os.getenv("website_url")
chrome_options=webdriver.ChromeOptions()

chrome_options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=chrome_options)
driver.get(url=url)
news_title=driver.find_elements(By.CLASS_NAME,value="post-title")
news_list=[news.text for news in news_title if len(news.text)>10]
plain_news_list = "\n\n".join(
    [
        f"{i}.{item}"
        for i, item in enumerate(news_list, start=1)
    ]
)
email_message = f"Subject: Hubballi-Dharwad News!!\n\n{plain_news_list}"
try:
    server=smtplib.SMTP("smtp.gmail.com",port=587)
    
    server.ehlo()
    server.starttls()  # Encrypts connection so login works
    server.ehlo()
    server.login(user=email,password=password)
    server.sendmail(
        from_addr=email,
        to_addrs=to_address,
        msg=email_message.encode("utf-8"),
    )
    print("mail send sucessfully")
except Exception as e:
    print(f"error occured while sending:{e}")
finally:
    driver.quit()





