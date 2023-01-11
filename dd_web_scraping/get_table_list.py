from bs4 import BeautifulSoup
import requests
import openpyxl

excel = openpyxl.Workbook()
sheet = excel.active
sheet.title = "Dungeon Defense (WN)"
# sheet.append(['Title', 'Link'])

site_url = 'https://shalvationtranslations.wordpress.com/dungeon-defense-wn-table-of-contents'


try:
    source = requests.get(site_url)
    source.raise_for_status()

    soup = BeautifulSoup(source.text, 'html.parser')
    # soup = soup.prettify()
    linkList = soup.find('div', class_='entry-content').find_all('a')

    not_need_link = [
        'https://shalvationtranslations.wordpress.com/early-access-chapters/',
        'https://shalvationtranslations.wordpress.com/dungeon-defense-wn-table-of-contents/?share=twitter',
        'https://shalvationtranslations.wordpress.com/dungeon-defense-wn-table-of-contents/?share=facebook',
        '#'
    ]

    for list in linkList:
        if list.has_attr('href'):
            link = list.get('href')
            if link not in not_need_link:
                title = list.text.strip()
                print(title, link)
                sheet.append([title, link])


except Exception as e:
    print(e)


excel.save('Dungeon Defense (WN) Table of Contents.xlsx')
