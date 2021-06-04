from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
import time






fio = input('Введите ФИО')
db = input('Введите дату рождения дд.дд.гггг')

webdriver = 'C:/Users/Администратор/PycharmProjects/Ok Parse/my-venv/Scripts/chromedriver_win32/chromedriver.exe'

url ='https://www.fedsfm.ru/documents/terr-list'
driver = Chrome(webdriver)
driver.get(url)

elem = driver.find_element_by_name('TerroristSearchText')
elem.send_keys(fio+" "+db)
driver.find_element_by_name('TerroristSearchButton').click()
time.sleep(5)
try:
    elements = driver.find_element_by_xpath("//tr[@role='row']//td[1]")
    print(elements.text)
except NoSuchElementException:
    print('Лицо отсутствует')


driver.close()