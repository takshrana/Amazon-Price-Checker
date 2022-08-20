import requests
from bs4 import BeautifulSoup
import smtplib

gmail = "smtp.gmail.com"
sender_email = "takshrana6@gmail.com"
password = "12345rana"
URL = "https://www.amazon.in/Test-Exclusive_2020_1178-Multi-3GB-Storage/dp/B089MTJVLD/ref=gbph_tit_m-5_d41e_7e9db5d6?smid=A23AODI1X2CEAE&pf_rd_p=cffb77a9-0317-4438-b4f0-6725053dd41e&pf_rd_s=merchandised-search-5&pf_rd_t=101&pf_rd_i=1389401031&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_r=3ATF8W21X612K1F7BC92"
AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"
LANG = "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7"
HEADER = {
    "User-Agent": AGENT,
    "Accept-Language": LANG
}

response = requests.get(url=URL, headers=HEADER)
am_web = response.text

soup = BeautifulSoup(am_web, "html.parser")
price = soup.find(name="span", id="priceblock_dealprice")
item_price = price.getText().split()[1]
item_price = float("".join(item_price.split(",")))
if item_price < 40000:
    with smtplib.SMTP(gmail) as connection:
        connection.starttls()
        connection.login(user=sender_email, password=password)
        connection.sendmail(from_addr=sender_email, to_addrs=sender_email, msg=f"Subject: Deal Found!\n\nYour Amazon Product is on sale rn, grab the product!\n{URL}")
