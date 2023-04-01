#extracts price of a small jammi kebab
from requests_html import HTMLSession
import gspread
from datetime import date
url = "https://jammi.lt/sauletekio-vilnius/kebabai-ir-buritai/kebabas-lavase"
s = HTMLSession()
r = s.get(url)
r.html.render(sleep = 1)
kaina = r.html.xpath('''//div[@class="price"]''', first = True )

kaina = kaina.text.strip()
print(kaina)

data = str(date.today())
gc = gspread.service_account(filename="creds.json") #upload a file with your credentials in json
sh = gc.open("KebabuInfliacija").sheet1
sh.append_row([data, kaina])

