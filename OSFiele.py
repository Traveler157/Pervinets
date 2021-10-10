import os
import time

from selenium import webdriver

link = " http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_tag_name('input ')
    input1.send_keys("Ivan")
    # <input type="text" name="lastname" class="form-control" placeholder="Enter last name" required="" maxlength="32">
    input2 = browser.find_element_by_name("lastname")
    input2.send_keys("Petrov")
    # <input type="text" name="email" class="form-control" placeholder="Enter email" maxlength="32" required="">
    input3 = browser.find_element_by_name("email")
    input3.send_keys("ase_ws@mail.ru")
    # <input type="file" id="file" name="file" accept=".txt" required="">
    element = browser.find_element_by_name("file")

    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
    os.mkdir(r'file.txt')
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла
    #print(file_path)
    #print(current_dir)
    element.send_keys(file_path)
    button = browser.find_element_by_css_selector('button')
    button.click()
    alert = browser.switch_to.alert
    alert_text = alert.text
    print(alert_text)

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
    os.rmdir(r"C:\Users\home\PycharmProjects\Selenium\file.txt")

# не забываем оставить пустую строку в конце файла






