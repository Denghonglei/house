from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# option = webdriver.ChromeOptions()
# option.add_argument('--user-data-dir=C:\\Users\Administrator\AppData\Local\Google\Chrome\Application\\User Data') #设置成用户自己的数据目录
driver = webdriver.Chrome()
driver.get("https://qzone.qq.com")
driver.switch_to.frame("login_frame")
new_window = driver.find_element_by_id('switcher_plogin')
new_window.click()
import time

# assert "Python" in driver.title
elem1 = driver.find_element_by_id("u")
elem1.clear()
elem1.send_keys("540188964")
elem2 = driver.find_element_by_class_name('password')
elem2.clear()
elem2.send_keys("DHLxiaolei345999")
elem3 = driver.find_element_by_id('login_button')
elem3.click()
time.sleep(10)
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
driver.get('https://user.qzone.qq.com/1053496681')
time.sleep(10)
# photos =  driver.find_element_by_class_name('menu_item_4')
photos = driver.find_element_by_xpath('//*[@id="menuContainer"]/div/ul/li[3]/a')
photos.click()  #进入相册

pic_index = driver.find_elements_by_class_name('js-album-cover')
for i in pic_index:
    i.click()
    try:
        pic = driver.find_elements_by_class_name('j-pl-photoitem-img')
        for j in pic:
            j.click()
            big_url = driver.find_element_by_xpath('//*[@id="js-img-border"]/img').get_attribute('src')

    except:
        print('error！！')





# driver.close()
