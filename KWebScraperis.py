#extracts price of a small jammi kebab
from requests_html import HTMLSession
import gspread
from datetime import date
url = "https://jammi.lt/sauletekio-al-17-vilnius/top/kebabas-lavase"
s = HTMLSession()
r = s.get(url)
r.html.render(sleep = 1)
kaina = r.html.xpath('''//*[@id="app"]/div[2]/div/div/div/div/div[2]/form/div[8]/div[1]/div''', first = True )

kaina = str(kaina.text)
data = str(date.today())
gc = gspread.service_account(filename="creds.json") #upload a file with your credentials in json
sh = gc.open("KebabuInfliacija").sheet1
sh.append_row([data, kaina])

