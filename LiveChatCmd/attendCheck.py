import json
import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

import methods as ms
import pandas as pd

id = ''
filename = 'attend.json'
cmd = '!attend'
ms.initJsonData('./%s' % filename, initType={})

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-extensions')

chromedriver_path = './chromedriver.exe'
browser = webdriver.Chrome(executable_path=chromedriver_path,
                           chrome_options=chrome_options)

url = "https://www.youtube.com/live_chat?v=" + id
browser.get(url)
browser.implicitly_wait(1)

# data = ms.getJsonData(path='./%s' % filename)
attends = []

for chat in browser.find_elements_by_css_selector('yt-live-chat-text-message-renderer'):

    author_name = chat.find_element_by_css_selector(
        "#author-name").text

    message = chat.find_element_by_css_selector(
        "#message").text
    if message.startswith(cmd):
        message = message.replace(" ","")
        message = message[message.find(cmd[-1:])+1:]
        attends.append([author_name, message])
        print(attends)
df = pd.DataFrame(data = attends,
                   columns=['작성자','내용'])
df.to_csv("attend.csv",encoding='utf-8-sig')
ms.writeJsonData(path=filename, jsonData=attends)

browser.quit()
