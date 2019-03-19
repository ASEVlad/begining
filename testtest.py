import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrapping_of_all_requests():
    def PagesUrl(url_of_n_pages):
        data = requests.get(url_of_n_pages)
        content = data.content
        soup = BeautifulSoup(content, 'lxml')
        result = []
        match = soup.find('table', class_='f-vacancylist-tablewrap')
        for tr_from_match in match.find_all('tr'):
            result.append('https://rabota.ua/' + tr_from_match.find('a').get('href'))
        return result[:-1]

    result = []
    url_of_n_pages = 'https://rabota.ua/jobsearch/vacancy_list?keyWords=Слесарь&regionId=0&pg=1'
    mas_of_request_url = PagesUrl(url_of_n_pages)
    for url_of_request in mas_of_request_url:
        result.append(url_of_request)
    return result

def Parcing_of_page(url_of_page):
    def Finding_of_salary():
        try:
            try:
                return soup.find('span', class_='money').text
            except:
                return soup.find('li', id='d-salary').find('span', class_='d-ph-value').text
        except:
            return None

    def Finding_of_address():
        try:
            return soup.find('span', class_='f-vacancy-city-param').text
        except SyntaxError:
            return soup.find('li', id='d-city').find('span', class_='d-ph-value').text
        except SyntaxWarning:
            return None

    def Finding_of_requirements():
        try:
            pass
            #return soup.find('span', class_='f-vacancy-city-param').text
        except:
            return None

    data = requests.get(url_of_page)
    content = data.content
    soup = BeautifulSoup(content, 'lxml')
    return [Finding_of_salary(), Finding_of_address(), Finding_of_requirements()]

mas_of_requests_url = scrapping_of_all_requests()
df = pd.DataFrame(columns=['salary', 'address', 'requirements'])
for i in range(len(mas_of_requests_url)):
    df.loc[i] = Parcing_of_page(mas_of_requests_url[i])
print(df)