from bs4 import BeautifulSoup
import requests
import openpyxl

excel = openpyxl.Workbook()
sheet = excel.active
sheet.title = "Dungeon Defense (WN)"

StoreAllLinkWithTitle = {}

site_url = 'https://shalvationtranslations.wordpress.com/dungeon-defense-wn-table-of-contents'


try:
    source = requests.get(site_url)
    source.raise_for_status()

    soup = BeautifulSoup(source.text, 'html.parser')
    linkList = soup.find('div', class_='entry-content').find_all('a')

    not_need_link = [
        'https://shalvationtranslations.wordpress.com/early-access-chapters/',
        'https://shalvationtranslations.wordpress.com/dungeon-defense-wn-table-of-contents/?share=twitter',
        'https://shalvationtranslations.wordpress.com/dungeon-defense-wn-table-of-contents/?share=facebook',
        '#'
    ]

    for anchor in linkList:
        if anchor.has_attr('href'):
            link = anchor.get('href')
            if link not in not_need_link:
                title = anchor.text.strip()
                StoreAllLinkWithTitle[title] = link

except Exception as e:
    print(e)


if (len(StoreAllLinkWithTitle) > 0):
    for i in StoreAllLinkWithTitle:
        lnk = StoreAllLinkWithTitle[i]
        print(i)
        print(lnk)
        sheet.append([i, lnk])

    excel.save('Dungeon Defense (WN) Table of Contents.xlsx')
