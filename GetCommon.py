from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

name_2019 = []
name_2018 = []
name_2017 = []
name_2020 = []

bot = webdriver.Chrome('D:\\Coding Stuff\\chromedriver.exe')
bot.get('https://summerofcode.withgoogle.com/archive/2019/organizations/')
time.sleep(5)
names_2019 = bot.find_elements_by_class_name(
    'organization-card__name')
for name1 in names_2019:
    name_2019.append(name1.text)

bot.get('https://summerofcode.withgoogle.com/organizations/?sp-page=5#5052609360035840')
time.sleep(5)
names_2020 = bot.find_elements_by_class_name(
    'organization-card__name')
for name2 in names_2020:
    name_2020.append(name2.text)

bot.get('https://summerofcode.withgoogle.com/archive/2018/organizations/')
time.sleep(5)
names_2018 = bot.find_elements_by_class_name(
    'organization-card__name')
for name3 in names_2018:
    name_2018.append(name3.text)

bot.get('https://summerofcode.withgoogle.com/organizations/?sp-page=5#5052609360035840')
time.sleep(5)
names_2017 = bot.find_elements_by_class_name(
    'organization-card__name')
for name4 in names_2017:
    name_2017.append(name4.text)

total = []
for name in name_2020:
    if name in name_2019 and name in name_2017 and name in name_2018:
        total.append(name)


print(len(total))

with open('GSoC.txt', 'w') as f:
    for i in total:
        f.write(f'{i}\n')
