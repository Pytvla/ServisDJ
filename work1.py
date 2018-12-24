
import requests
from bs4 import BeautifulSoup as BS
import codecs

session = requests.session()
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; rv:47.0) Gecko/20100101 Firefox/47.0',
           'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
    }
url = 'https://www.work.ua/jobs-kyiv-python/'
req = session.get(url, headers=headers)
domain = 'https://www.work.ua' # для абсолютной ссылки
jobs = []
if req.status_code == 200:
    bsObj = BS(req.content, "html.parser")
    # div = bsObj.find('div', attrs={'class': 'job-link'}) # первого diva
    div_list = bsObj.find_all('div', attrs={'class': 'job-link'}) # парсинг всех
    for div in div_list:
        title = div.find('h2')
        href = title.a['href']
        short = div.p.text
        # Имя компании по логотипу
        company = "No name"
        logo = div.find('img')
        if logo:
            company = logo['alt']
        jobs.append({'href': domain + href,
                    'title': title.text,
                    'descript': short,
                    'company': company})

    # print(div.find('h2').text)
    # title = div.find('h2')
    # href = title.a['href']
    #print(href) #относительная ссылка
    #print('work.ua' + href) # абсолютная ссылка
    # print(div.find('p', attrs={'class': 'overflow'}).text)
#data = bsObj.prettify()#.encode('utf8')

handle = codecs.open('lis_html', "w", 'utf-8')
handle.write(str(jobs))
# handle.write(str(div.contents))
#handle.write(str(div.find('p', attrs={'class': 'overflow'}).text))
handle.close()
