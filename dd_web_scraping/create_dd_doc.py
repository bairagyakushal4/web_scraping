from bs4 import BeautifulSoup
import requests
import openpyxl
from docx import Document
from docx.shared import Inches, Cm
from docx.shared import Pt


def init_document(doc):
    # style the body text
    style = doc.styles['Normal']
    font = style.font
    font.size = Pt(16)

    # style the heading
    HeadingStyle = doc.styles['Heading 1']
    HeadingFont = HeadingStyle.font
    HeadingFont.size = Pt(24)

    # set margin
    sections = doc.sections
    for section in sections:
        section.top_margin = Cm(2.54)
        section.bottom_margin = Cm(2.54)
        section.left_margin = Cm(1.9)
        section.right_margin = Cm(1.9)


def Scrape_Site(site_url):
    try:

        source = requests.get(site_url)
        source.raise_for_status()
        soup = BeautifulSoup(source.text, 'html.parser')
        storyPart = soup.find('div', class_='entry-content')
        storyPart_text = storyPart.get_text("\n\n", strip=True)
        storyPart_text = storyPart_text.replace("Ο", "\n")

        chapter_text = [
            'PREVIOUS CHAPTER | NEXT CHAPTER',
            'NEXT CHAPTER',
            'PREVIOUS CHAPTER'
        ]

        for chapter in chapter_text:
            if chapter in storyPart_text:
                storyPart_text_btn_split = storyPart_text.split(chapter)
                finalStory = storyPart_text_btn_split[0]

        finalStory = finalStory.replace("\n\n\n", "\n")

        chapter_heading = finalStory.split('\n', 1)[0]
        finalStory = finalStory.split('\n', 1)[1]

        return chapter_heading, finalStory

    except Exception as e:
        print(e)

        return 0


""" def writeText(fileName, txt):
    f = open(fileName, "w", encoding="utf-8")
    f.write(txt)
    f.close() """


excel = openpyxl.load_workbook('Dungeon Defense (WN) Table of Contents.xlsx')
sheet = excel.active

total_rows = sheet.max_row

all_site_url = tuple()


for x in range(1, total_rows + 1):
    col_one = sheet.cell(row=x, column=1).value
    col_two = sheet.cell(row=x, column=2).value
    all_site_url += (col_two,)


count = 0
countGallopGap = 50
countGallop = countGallopGap

i = 0

doc = Document()
init_document(doc)

for u in all_site_url:
    count = count + 1

    # write a specific no fo chapter in multiple files
    if count == countGallop:
        i = i + 1
        countGallop = countGallop + countGallopGap
        fileName = f'Dungeon-Defense-{i}-(WN).docx'
        chapter_heading, finalStory = Scrape_Site(u)

        doc.add_heading(chapter_heading, level=1)
        doc.add_paragraph(finalStory)
        doc.add_page_break()
        doc.save(fileName)

        doc = Document()
        init_document(doc)
        print('if', chapter_heading, count)

        # for testing
        # if count == 10:
        #     break

    else:
        chapter_heading, finalStory = Scrape_Site(u)
        doc.add_heading(chapter_heading, level=1)
        doc.add_paragraph(finalStory)
        doc.add_page_break()

        print('else', chapter_heading, count)

        # save the rest of chapter in another file
        if count == len(all_site_url):
            i = i + 1
            fileName = f'Dungeon-Defense-{i}-(WN).docx'
            doc.save(fileName)
