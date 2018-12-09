# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
from contact import Contact

class AddNewContact(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)


    def test_add_new_contact(self):
        wd = self.wd
        self.go_to_page(wd)
        self.login(wd, username="admin", password="secret")
        self.init_new_contact(wd)
        self.fill_the_form(wd, Contact(notes="happy", first_name="Veaceslav", middle_name="Berkam", last_name="Jirkin",
                           nickname="JirBer", title="CP", company_name="Krown", address_1="5555 kasda str",
                           home_phone="+373 896 986 22", cell_phone="+373 699477 44", work_phone="+646 979755454",
                           fax="+100 5222 6633", email_1="ssdrug1@gmail.com", email_2="asdasd@sdfs.com",
                           email_3="gdfgd@sdfsd.com", home_page="ww.asdasd.com", birth_day="3", birth_month="March",
                           birth_year="1987", anniversay_day="6", anniversay_month="April",
                           anniversay_year="2007", part_of_group="new_group", address_2="9834 jackD str",
                           suit_nr="ap 95"))
        self.submit_new_contact(wd)
        self.return_to_main_page(wd)
        self.logout(wd)


    def test_add_new_contact_2(self):
        wd = self.wd
        self.go_to_page(wd)
        self.login(wd, username="admin", password="secret")
        self.init_new_contact(wd)
        self.fill_the_form(wd, Contact(notes="sad", first_name="Alexey", middle_name="Ivan", last_name="Shishkin",
                           nickname="Shishka", title="", company_name="", address_1="",
                           home_phone="", cell_phone="", work_phone="+646 979755454",
                           fax="+100 5222 6633", email_1="", email_2="asdasd@sdfs.com",
                           email_3="gdfgd@sdfsd.com", home_page="", birth_day="3", birth_month="March",
                           birth_year="1987", anniversay_day="6", anniversay_month="April",
                           anniversay_year="2007", part_of_group="new_group", address_2="",
                           suit_nr="ap 95"))
        self.submit_new_contact(wd)
        self.return_to_main_page(wd)
        self.logout(wd)

    def logout(self, wd):
        # лог-аут
        wd.find_element_by_link_text("Logout").click()

    def return_to_main_page(self, wd):
        # переход на главную страничку со списком контактов
        wd.find_element_by_link_text("home page").click()

    def submit_new_contact(self, wd):
        # сабмит формы
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def fill_the_form(self, wd, contact):
        # заполнение формы
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.first_name)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact.middle_name)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.last_name)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contact.nickname)
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(contact.title)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contact.company_name)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.address_1)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.home_phone)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.cell_phone)
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(contact.work_phone)
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(contact.fax)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email_1)
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(contact.email_2)
        wd.find_element_by_name("email3").click()
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(contact.email_3)
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(contact.home_page)
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text(contact.birth_day)
        wd.find_element_by_name("bday").click()
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(contact.birth_month)
        wd.find_element_by_name("bmonth").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(contact.birth_year)
        wd.find_element_by_name("aday").click()
        Select(wd.find_element_by_name("aday")).select_by_visible_text(contact.anniversay_day)
        wd.find_element_by_name("aday").click()
        wd.find_element_by_name("amonth").click()
        Select(wd.find_element_by_name("amonth")).select_by_visible_text(contact.anniversay_month)
        wd.find_element_by_name("amonth").click()
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys(contact.anniversay_year)
        wd.find_element_by_name("new_group").click()
        Select(wd.find_element_by_name("new_group")).select_by_visible_text(contact.part_of_group)
        wd.find_element_by_name("new_group").click()
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(contact.address_2)
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(contact.suit_nr)
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(contact.notes)

    def init_new_contact(self, wd):
        # переход на сраницу формы добавления нового контакта
        wd.find_element_by_link_text("add new").click()

    def login(self, wd, username, password):
        # авторизация пользователя
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_id("LoginForm").click()
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def go_to_page(self, wd):
        # навигация на страничку
        wd.get("http://localhost/addressbook/")

    def is_element_present(self, how, what):
        try:
            self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.wd.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()

