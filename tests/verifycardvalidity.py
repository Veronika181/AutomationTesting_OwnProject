from selenium import webdriver
from pages.LoginPage import LoginPage
from pages.MainPage import MainPage

driver = webdriver.Chrome()
login_page = LoginPage(driver)
main_page = MainPage(driver)

login_page.navigate_to_verifycard()
login_page.enter_license_plate("5P35010")
login_page.verify_validity()










