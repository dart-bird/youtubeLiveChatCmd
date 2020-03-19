import json
import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

import methods as ms

id = 'mch4u8DlhGY'
filename = 'data.json'
pollData = ['전상민', '홍석민', '이승훈', '유진웅']
cmd = '!vote'
ms.initJsonData('./%s' % filename, initType={})
data = {}
for i in range(len(pollData)):
    inData = {
        pollData[i]: {
            "count": 0
        }
    }
    data.update(inData)
ms.writeJsonData(path='./%s' % filename, jsonData=data)

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

data = ms.getJsonData(path='./%s' % filename)
attends = []

for chat in browser.find_elements_by_css_selector('yt-live-chat-text-message-renderer'):

    author_name = chat.find_element_by_css_selector(
        "#author-name").text

    message = chat.find_element_by_css_selector(
        "#message").text

    if cmd in message:  # start cmd
        for target_list in pollData:  # get attend from pollData
            if author_name in attends:  # one vote, one Id
                continue
            else:
                if target_list in message:
                    if author_name in attends:
                        continue
                    attends.append(author_name)

                    if target_list in message:
                        if data.get(target_list) != None:  # if pollData index exist
                            data[target_list]["count"] += 1

ms.writeJsonData(path=filename, jsonData=data)

browser.quit()
