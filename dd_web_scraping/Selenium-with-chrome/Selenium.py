from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

search_anime = val = input("Enter Anime Name:")
fileName = '-'.join(search_anime.split())

browser = webdriver.Chrome()
browser.implicitly_wait(5)

browser.get("https://anime7.download/")

elem = browser.find_element(By.ID, "s")
elem.clear()
elem.send_keys(search_anime)
elem.send_keys(Keys.RETURN)

assert "We apologize for any inconvenience, please hit back on your browser or use the search form below." not in browser.page_source

xPath_value = f"//a[contains(text(), '{search_anime}')]"
anime = browser.find_element(By.XPATH, xPath_value).click()
content = browser.find_element(By.CLASS_NAME, "thecontent")

allLinks = content.find_elements(By.TAG_NAME, "a")


storLink = []

for l in allLinks:
    link = l.get_attribute('href')
    storLink.append(link)


# Append-adds at last
file1 = open(fileName+".txt", "a")  # append mode

# print(storLink)
for l in storLink:
    # print(l)
    file1.write(f"{l}\n\n")

file1.close()

time.sleep(3)
browser.close()
