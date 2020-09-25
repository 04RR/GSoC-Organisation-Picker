# organization__tag organization__tag--technology

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

bot = webdriver.Chrome('D:\\Coding Stuff\\chromedriver.exe')
bot.get('https://summerofcode.withgoogle.com/organizations/?sp-page=5#5052609360035840')
time.sleep(3)

gg = bot.find_elements_by_class_name('org__logo')
button = gg[0]
button.click()
skills_ele = bot.find_elements_by_class_name('organization__tag--technology')
skills = []
print(skills_ele)
for ele in skills_ele:
    skills.append(ele.text)
print(skills)