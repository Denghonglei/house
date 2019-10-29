from selenium import webdriver
from selenium.webdriver.common.keys import Keys
option = webdriver.ChromeOptions()
option.add_argument('--user-data-dir=C:\\Users\Administrator\AppData\Local\Google\Chrome\Application\\User Data') #设置成用户自己的数据目录
driver = webdriver.Chrome(chrome_options=option)
