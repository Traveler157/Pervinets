import math
from selenium import webdriver
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    time.sleep(1)
    x_element = browser.find_element_by_xpath('//*[@id="price"]')
    x_elemen = x_element.text
    if x_element.text == '$100':
        option1 = browser.find_element_by_id("book")
        option1.click()
        browser.execute_script("window.scrollBy(0, 300);")
        option2 = browser.find_element_by_id("answer")
        option2.click()
        x_element = browser.find_element_by_css_selector('#input_value').text
        azx = x_element  #####@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@###################################
        print(azx)
        x = azx
        x = int(x)
        y = calc(x)
        #y = str(y)
        print(x,y)
        input1 = browser.find_element_by_id("answer")
        input1.send_keys(y)
        # <button id="solve" type="submit" class="btn btn-primary" disabled="disabled">Submit</button>
        option1 = browser.find_element_by_id("solve")
        option1.click()
        alert = browser.switch_to.alert
        alert_text = alert.text
        print(alert_text)

        # print(x_elemen, '@@@@@@@@@@@@@@@@@@@@@')

    time.sleep(1)
    x_element1 = browser.find_element_by_id('price')
    x_elemen1 = x_element1.text
    if x_element1.text == '$100':
        option1 = browser.find_element_by_id("book")
        option1.click()
        browser.execute_script("window.scrollBy(0, 300);")
        option2 = browser.find_element_by_id("answer")
        option2.click()
        x_element = browser.find_element_by_css_selector('#input_value').text
        azx = x_element  #####@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@###################################
        print(azx)
        x = azx
        x = int(x)
        y = calc(x)
        #y = str(y)
        print(x,y)
        input1 = browser.find_element_by_id("answer")
        input1.send_keys(y)
        # <input class="form-check-input" type="checkbox" id="robotCheckbox" required="">
        option1 = browser.find_element_by_id("solve")
        option1.click()
        alert = browser.switch_to.alert
        alert_text = alert.text
        print(alert_text)
        # preis_100 = 1
        # print(x_elemen1, '!!!!!!!!!!')
    time.sleep(1)
    x_element2 = browser.find_element_by_id('price')
    x_elemen2 = x_element2.text
    if x_element2.text == '$100':
        option1 = browser.find_element_by_id("book")
        option1.click()
        browser.execute_script("window.scrollBy(0, 300);")
        option2 = browser.find_element_by_id("answer")
        option2.click()
        x_element = browser.find_element_by_css_selector('#input_value').text
        azx = x_element  #####@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@###################################
        print(azx)
        x = azx
        x = int(x)
        y = calc(x)
        #y = str(y)
        print(x,y)
        input1 = browser.find_element_by_id("answer")
        input1.send_keys(y)
        # <input class="form-check-input" type="checkbox" id="robotCheckbox" required="">
        option1 = browser.find_element_by_id("solve")
        option1.click()
        alert = browser.switch_to.alert
        alert_text = alert.text
        print(alert_text)
        # preis_100 = 1
    # print(x_elemen2.text, 2222222222)
    time.sleep(1)
    x_element3 = browser.find_element_by_id('price')
    x_elemen3 = x_element3.text
    if x_element3.text == '$100':
        option1 = browser.find_element_by_id("book")
        option1.click()
        browser.execute_script("window.scrollBy(0, 300);")
        option2 = browser.find_element_by_id("answer")
        option2.click()
        x_element = browser.find_element_by_css_selector('#input_value').text
        azx = x_element  #####@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@###################################
        print(azx)
        x = azx
        x = int(x)
        y = calc(x)
        #y = str(y)
        print(x,y)
        input1 = browser.find_element_by_id("answer")
        input1.send_keys(y)
        # <input class="form-check-input" type="checkbox" id="robotCheckbox" required="">
        option1 = browser.find_element_by_id("solve")
        option1.click()
        alert = browser.switch_to.alert
        alert_text = alert.text
        print(alert_text)
    # preis_100 = 1
    # print(x_elemen3, 000000000000)
    time.sleep(1)
    x_element4 = browser.find_element_by_id('price')
    x_elemen4 = x_element4.text
    if x_element4.text == '$100':
        option1 = browser.find_element_by_id("book")
        option1.click()
        browser.execute_script("window.scrollBy(0, 300);")
        option2 = browser.find_element_by_id("answer")
        option2.click()
        x_element = browser.find_element_by_css_selector('#input_value').text
        azx = x_element  #####@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@###################################
        print(azx)
        x = azx
        x = int(x)
        y = calc(x)
        #y = str(y)
        print(x,y)
        input1 = browser.find_element_by_id("answer")
        input1.send_keys(y)
        # <input class="form-check-input" type="checkbox" id="robotCheckbox" required="">
        option1 = browser.find_element_by_id("solve")
        option1.click()
        alert = browser.switch_to.alert
        alert_text = alert.text
        print(alert_text)
    # preis_100 = 1
    # print(x_elemen4, 444444)
    time.sleep(1)
    x_element5 = browser.find_element_by_id('price')
    x_elemen5 = x_element5.text
    if x_element5.text == '$100':
        option1 = browser.find_element_by_id("book")
        option1.click()
        browser.execute_script("window.scrollBy(0, 300);")
        option2 = browser.find_element_by_id("answer")
        option2.click()
        x_element = browser.find_element_by_css_selector('#input_value').text
        azx = x_element  #####@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@###################################
        print(azx)
        x = azx
        x = int(x)
        y = calc(x)
        #y = str(y)
        print(x,y)
        input1 = browser.find_element_by_id("answer")
        input1.send_keys(y)
        # <input class="form-check-input" type="checkbox" id="robotCheckbox" required="">
        option1 = browser.find_element_by_id("solve")
        option1.click()
        alert = browser.switch_to.alert
        alert_text = alert.text
        print(alert_text)
    # preis_100 = 1
    # print(x_elemen5, 555555)
    time.sleep(1)
    x_element9 = browser.find_element_by_id('price')
    x_elemen9 = x_element9.text
    if x_element9.text == '$100':
        option1 = browser.find_element_by_id("book")
        option1.click()
        browser.execute_script("window.scrollBy(0, 300);")
        option2 = browser.find_element_by_id("answer")
        option2.click()
        x_element = browser.find_element_by_css_selector('#input_value').text
        azx = x_element  #####@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@###################################
        print(azx)
        x = azx
        x = int(x)
        y = calc(x)
        #y = str(y)
        print(x,y)
        input1 = browser.find_element_by_id("answer")
        input1.send_keys(y)
        # <input class="form-check-input" type="checkbox" id="robotCheckbox" required="">
        option1 = browser.find_element_by_id("solve")
        option1.click()
        alert = browser.switch_to.alert
        alert_text = alert.text
        print(alert_text)
        # preis_100 = 1
        # print(x_elemen9, 9999999)
    time.sleep(1)
    x_element10 = browser.find_element_by_id('price')
    x_elemen10 = x_element10.text
    if x_element10.text == '$100':
        option1 = browser.find_element_by_id("book")
        option1.click()
        browser.execute_script("window.scrollBy(0, 300);")
        option2 = browser.find_element_by_id("answer")
        option2.click()
        x_element = browser.find_element_by_css_selector('#input_value').text
        azx = x_element  #####@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@###################################
        print(azx)
        x = azx
        x = int(x)
        y = calc(x)
        #y = str(y)
        print(x,y)
        input1 = browser.find_element_by_id("answer")
        input1.send_keys(y)
        # <input class="form-check-input" type="checkbox" id="robotCheckbox" required="">
        option1 = browser.find_element_by_id("solve")
        option1.click()
        alert = browser.switch_to.alert
        alert_text = alert.text
        print(alert_text)
    # preis_100 = 1
    # print(x_elemen10, 10101010)
    time.sleep(1)

    x_element11 = browser.find_element_by_id('price')
    x_elemen11 = x_element11.text
    if x_element11.text == '$100':
        option1 = browser.find_element_by_id("book")
        option1.click()
        browser.execute_script("window.scrollBy(0, 300);")
        option2 = browser.find_element_by_id("answer")
        option2.click()
        x_element = browser.find_element_by_css_selector('#input_value').text
        azx = x_element  #####@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@###################################
        print(azx)
        x = azx
        x = int(x)
        y = calc(x)
        #y = str(y)
        print(x,y)
        input1 = browser.find_element_by_id("answer")
        input1.send_keys(y)
        # <input class="form-check-input" type="checkbox" id="robotCheckbox" required="">
        option1 = browser.find_element_by_id("solve")
        option1.click()
        alert = browser.switch_to.alert
        alert_text = alert.text
        print(alert_text)
    # preis_100 = 1
    # print(x_elemen11, 111111111)
    time.sleep(1)
    x_element6 = browser.find_element_by_id('price')
    x_elemen6 = x_element6.text
    if x_element6.text == '$100':
        option1 = browser.find_element_by_id("book")
        option1.click()
        browser.execute_script("window.scrollBy(0, 300);")
        option2 = browser.find_element_by_id("answer")
        option2.click()
        x_element = browser.find_element_by_css_selector('#input_value').text
        azx = x_element  #####@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@###################################
        print(azx)
        x = azx
        x = int(x)
        y = calc(x)
        #y = str(y)
        print(x,y)
        input1 = browser.find_element_by_id("answer")
        input1.send_keys(y)
        # <input class="form-check-input" type="checkbox" id="robotCheckbox" required="">
        option1 = browser.find_element_by_id("solve")
        option1.click()
        alert = browser.switch_to.alert
        alert_text = alert.text
        print(alert_text)
    # preis_100 = 1
    # print(x_elemen6, 6666666666)
    time.sleep(1)
    x_element7 = browser.find_element_by_id('price')
    x_elemen7 = x_element7.text
    if x_element7.text == '$100':
        option1 = browser.find_element_by_id("book")
        option1.click()
        browser.execute_script("window.scrollBy(0, 300);")
        option2 = browser.find_element_by_id("answer")
        option2.click()
        x_element = browser.find_element_by_css_selector('#input_value').text
        azx = x_element  #####@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@###################################
        print(azx)
        x = azx
        x = int(x)
        y = calc(x)
        #y = str(y)
        print(x,y)
        input1 = browser.find_element_by_id("answer")
        input1.send_keys(y)
        # <input class="form-check-input" type="checkbox" id="robotCheckbox" required="">
        option1 = browser.find_element_by_id("solve")
        option1.click()
        alert = browser.switch_to.alert
        alert_text = alert.text
        print(alert_text)
    # preis_100 = 1
    # print(x_elemen7, 777777777777777)
    time.sleep(1)
    x_element8 = browser.find_element_by_id('price')
    x_elemen8 = x_element8.text
    if x_element8.text == '$100':
        option1 = browser.find_element_by_id("book")
        option1.click()
        browser.execute_script("window.scrollBy(0, 300);")
        option2 = browser.find_element_by_id("answer")
        option2.click()
        x_element = browser.find_element_by_css_selector('#input_value').text
        azx = x_element  #####@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@###################################
        print(azx)
        x = azx
        x = int(x)
        y = calc(x)
        #y = str(y)
        print(x,y)
        input1 = browser.find_element_by_id("answer")
        input1.send_keys(y)
        # <input class="form-check-input" type="checkbox" id="robotCheckbox" required="">
        option1 = browser.find_element_by_id("solve")
        option1.click()
        alert = browser.switch_to.alert
        alert_text = alert.text
        print(alert_text)
    # <span class="nowrap" id="input_value">287</span>
# <input class="form-control" name="text" id="answer" type="text" required="">
#
        x_element = browser.find_element_by_css_selector('#input_value').text
        azx = x_element  #####@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@###################################
        print(azx)
        x = azx
        x = int(x)
        y = calc(x)
        #y = str(y)
        print(x,y)
        input1 = browser.find_element_by_id("answer")
        input1.send_keys(y)
        # <input class="form-check-input" type="checkbox" id="robotCheckbox" required="">
        option1 = browser.find_element_by_id("solve")
        option1.click()
        alert = browser.switch_to.alert
        alert_text = alert.text
        print(alert_text)
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(0)
    # закрываем браузер после всех манипуляций
    browser.quit()

# def calc(x):
#   return str(math.log(abs(12 * math.sin(int(x)))))
