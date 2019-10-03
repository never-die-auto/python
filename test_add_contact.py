# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_add_contact(self):
        driver = self.driver
        self.open_home_page(driver)
        self.login(driver)
        self.add_contact(driver, firstname="Ivan", middlename="Petrovich", lastname="Petrov", nickname="user56", title="have", company="infotecs", address="moscow", home="nogimsk",
                         mobile="4672378235", work="ingener", fax="46464", email="ssdg@bff.ru", email2="edgda@dhf.ru", email3="dhdg@fhf.com", homepage="www.dgf.ru",
                         bday="15", bmonth="August", byear="1999", aday="14", amonth="November", ayear="2019", address2="noginsk pervae", phone2="noginsk", notes="komment")
        self.return_to_home_page(driver)
        self.logout(driver)

    def logout(self, driver):
        driver.find_element_by_link_text("Logout").click()

    def return_to_home_page(self, driver):
        driver.find_element_by_link_text("home").click()

    def add_contact(self, driver, firstname, middlename, lastname, nickname, title, company, address, home, mobile,
                    work, fax, email, email2, email3, homepage, bday, bmonth, byear, aday, amonth, ayear, address2,
                    phone2, notes):
        driver.find_element_by_link_text("add new").click()
        driver.find_element_by_name("firstname").click()
        driver.find_element_by_name("firstname").clear()
        driver.find_element_by_name("firstname").send_keys(firstname)
        driver.find_element_by_name("middlename").clear()
        driver.find_element_by_name("middlename").send_keys(middlename)
        driver.find_element_by_name("lastname").clear()
        driver.find_element_by_name("lastname").send_keys(lastname)
        driver.find_element_by_name("nickname").clear()
        driver.find_element_by_name("nickname").send_keys(nickname)
        driver.find_element_by_name("title").click()
        driver.find_element_by_name("title").clear()
        driver.find_element_by_name("title").send_keys(title)
        driver.find_element_by_name("company").clear()
        driver.find_element_by_name("company").send_keys(company)
        driver.find_element_by_name("address").clear()
        driver.find_element_by_name("address").send_keys(address)
        driver.find_element_by_name("home").clear()
        driver.find_element_by_name("home").send_keys(home)
        driver.find_element_by_name("mobile").clear()
        driver.find_element_by_name("mobile").send_keys(mobile)
        driver.find_element_by_name("work").clear()
        driver.find_element_by_name("work").send_keys(work)
        driver.find_element_by_name("fax").clear()
        driver.find_element_by_name("fax").send_keys(fax)
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys(email)
        driver.find_element_by_name("email2").clear()
        driver.find_element_by_name("email2").send_keys(email2)
        driver.find_element_by_name("email3").clear()
        driver.find_element_by_name("email3").send_keys(email3)
        driver.find_element_by_name("homepage").clear()
        driver.find_element_by_name("homepage").send_keys(homepage)
        driver.find_element_by_name("bday").click()
        Select(driver.find_element_by_name("bday")).select_by_visible_text(bday)
        driver.find_element_by_name("bday").click()
        driver.find_element_by_name("bmonth").click()
        Select(driver.find_element_by_name("bmonth")).select_by_visible_text(bmonth)
        driver.find_element_by_name("bmonth").click()
        driver.find_element_by_name("byear").click()
        driver.find_element_by_name("byear").clear()
        driver.find_element_by_name("byear").send_keys(byear)
        driver.find_element_by_name("aday").click()
        Select(driver.find_element_by_name("aday")).select_by_visible_text(aday)
        driver.find_element_by_name("aday").click()
        driver.find_element_by_name("amonth").click()
        Select(driver.find_element_by_name("amonth")).select_by_visible_text(amonth)
        driver.find_element_by_name("amonth").click()
        driver.find_element_by_name("ayear").click()
        driver.find_element_by_name("ayear").clear()
        driver.find_element_by_name("ayear").send_keys(ayear)
        driver.find_element_by_name("address2").click()
        driver.find_element_by_name("address2").clear()
        driver.find_element_by_name("address2").send_keys(address2)
        driver.find_element_by_name("phone2").click()
        driver.find_element_by_name("phone2").clear()
        driver.find_element_by_name("phone2").send_keys(phone2)
        driver.find_element_by_name("notes").click()
        driver.find_element_by_name("notes").clear()
        driver.find_element_by_name("notes").send_keys(notes)
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Notes:'])[1]/following::input[1]").click()

    def login(self, driver, username="admin", password="secret"):
        driver.find_element_by_name("user").click()
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys(username)
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='User:'])[1]/following::label[1]").click()
        driver.find_element_by_name("pass").click()
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("pass").send_keys(password)
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Password:'])[1]/following::input[2]").click()

    def open_home_page(self, driver):
        driver.get("http://localhost:8080/addressbook/")

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
