from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
user=input('Please enter the username you wish to use: ')
email=input('Please enter your email-id: ')
password=input('Please enter the password you wish to use: ')
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://codeforces.com/register')
id_box = driver.find_element_by_name('handle')
id_box.send_keys(user)
email_box = driver.find_element_by_name('email')
email_box.send_keys(email)
pass_box= driver.find_element_by_name('password')
pass_box.send_keys(password)
pass2= driver.find_element_by_name('passwordConfirmation')
pass2.send_keys(password)
register_button = driver.find_element_by_class_name('submit')
register_button.click()