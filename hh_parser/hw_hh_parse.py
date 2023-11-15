from urllib.parse import urljoin
from pprint import pprint as pp
import bs4
import fake_headers
import requests
import re
import json

BASE_URL = 'https://spb.hh.ru/search/vacancy?text=python+django+flask&salary=&ored_clusters=true&area=1&area=2&hhtmFrom=vacancy_search_list'

headers_fake = fake_headers.Headers(os='win', browser='chrome')

response = requests.get(BASE_URL, headers=headers_fake.generate()).text
main_page_soup = bs4.BeautifulSoup(response, 'lxml')

vacancy_list_tag = main_page_soup.find('div',
                                       class_='bloko-column bloko-column_xs-4 bloko-column_s-8 bloko-column_m-9 bloko-column_l-13')
vacancy_tags = vacancy_list_tag.find_all('div', class_='serp-item')
vacancy_data = []

for vacancy_tag in vacancy_tags:
    h3_tag = vacancy_tag.find('h3', class_='bloko-header-section-3')
    span_tag = h3_tag.find('span')

    a_tag = span_tag.find('a')
    link_relative = a_tag['href']

    location_tag = vacancy_tag.find('div', {'data-qa': 'vacancy-serp__vacancy-address'})
    city = location_tag.text.split(',')[0]

    response_link = requests.get(link_relative, headers=headers_fake.generate())
    vacancy_html_data = response_link.text
    vacancy_soup = bs4.BeautifulSoup(vacancy_html_data, 'lxml')

    h1_tag = vacancy_soup.find('div', class_='vacancy-title')
    header_tag = h1_tag.find('h1', class_='bloko-header-section-1')
    header = header_tag.text.strip()

    salary_tag = h1_tag.find('div', {'data-qa': 'vacancy-salary'})
    if salary_tag != None:
        salary_html = salary_tag.text.strip()
        salary = salary_html.replace('\xa0', '').replace('-', '-')
    else:
        salary = 'Зарплата не указана'

    company_tag = vacancy_soup.find('div', class_='vacancy-company-redesigned')
    company_html = company_tag.find('span', class_='vacancy-company-name')
    company = company_html.text.strip()

    vacancy_data.append(
        {
            'header': header,
            'city': city,
            'salary': salary,
            'link': link_relative,
            'company': company
        }
    )
with open('vacancys.json', 'w', encoding='utf-8') as f:
    json.dump(vacancy_data, f, ensure_ascii=False, indent=4)
