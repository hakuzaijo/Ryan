# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import unittest, time, random
import names

i = random.randrange(0,99999999, 20)
i = random.randrange(0,99999999, 20)
man = names.get_first_name(gender='male')
woman = names.get_first_name(gender='female')
child = names.get_first_name()
surname = names.get_last_name()
creditCard = names.get_full_name()

'''
Created by Marcin Sikorski for Ryanair
--------------------------------------
Requirements: pip install names
-----------------------------------------
Case:

Simple test to validate correct message of an Unauthorized error

----------------
BDD:

Given I make a booking from “DUB” to “SXF” on 11/03/2016 for 2 adults and 1 child
When I pay for booking with card details “5555 5555 5555 5557”, “10/18” and “265”
Then I should get payment declined message

-----------------
Comments:
* Pauses added due to the fact website has a lot of javascript and it is heavy to load properly on slower network connection
* Printscreen of an error message is saved just for safety measure
* Random names used due to the error message "Duplicated booking in"

'''



class Ryanair(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()


    def test_ryanair(self):
        driver = self.driver
        driver.get("https://www.ryanair.com/ie/en/")
        driver.maximize_window()
        time.sleep(1)


        #Dublin
        driver.find_element_by_xpath("(//input[@type='text'])[2]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[2]").send_keys("dublin")
        time.sleep(1)
        #One way
        driver.find_element_by_xpath("html/body/div[2]/main/article/div[2]/div/div[2]/div/form/div[1]/div[1]/div[2]/label/span[2]").click()
        time.sleep(1)
        #Berlin
        driver.find_element_by_xpath("(//input[@type='text'])[4]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[4]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[4]").send_keys("berlin (sxf)")
        #Fly out
        driver.find_element_by_xpath("//div[@id='search-container']/div/form/div[3]/button").click()
        driver.find_element_by_css_selector("div.select-date.placeholder").click()
        driver.find_element_by_xpath("//div[@id='row-dates-pax']/div/div/div/div/div[3]/div/div/div[2]/core-datepicker/div/ul/li/ul[2]/li[12]/span").click()
        #Passangers
        driver.find_element_by_css_selector("div.dropdown-handle > core-icon.chevron > div > svg").click()
        driver.find_element_by_xpath("(//button[@type='button'])[2]").click()
        driver.find_element_by_xpath("(//button[@type='button'])[6]").click()
        time.sleep(1)
        driver.find_element_by_xpath("//div[@id='search-container']/div/form/div[3]/button[2]").click()
        time.sleep(1)

        #Price
        driver.find_element_by_xpath("html/body/div[2]/main/div[1]/section/div/div[1]/div/div[3]/div/div/div[2]/div[2]/div[1]/div[2]/div[2]/div/span[1]").click()
        time.sleep(5)
        driver.find_element_by_xpath("html/body/div[2]/main/section/div/section[2]/article/div[2]/section/div[2]/button").click()
        time.sleep(1)

        #Extras
        driver.find_element_by_xpath("html/body/div[8]/div[2]/div[1]/div/div[1]/h1/div/div/div[1]").click()
        time.sleep(1)
        driver.find_element_by_xpath("html/body/div[2]/main/section/div/section[2]/article/div[2]/section/div[2]/button").click()
        time.sleep(2)

        #Mr
        driver.find_element_by_xpath("html/body/div[2]/main/div[1]/div[2]/div/form/div[1]/div[1]/div/div[2]/ng-form/div[1]/div/ng-form/div[1]/div[2]/input").clear()
        driver.find_element_by_xpath("html/body/div[2]/main/div[1]/div[2]/div/form/div[1]/div[1]/div/div[2]/ng-form/div[1]/div/ng-form/div[1]/div[2]/input").send_keys(man)
        driver.find_element_by_xpath("html/body/div[2]/main/div[1]/div[2]/div/form/div[1]/div[1]/div/div[2]/ng-form/div[1]/div/ng-form/div[1]/div[1]/div/select/option[2]").click()
        driver.find_element_by_xpath("html/body/div[2]/main/div[1]/div[2]/div/form/div[1]/div[1]/div/div[2]/ng-form/div[1]/div/ng-form/div[1]/div[3]/input").clear()
        driver.find_element_by_xpath("html/body/div[2]/main/div[1]/div[2]/div/form/div[1]/div[1]/div/div[2]/ng-form/div[1]/div/ng-form/div[1]/div[3]/input").send_keys(surname)

        #Mrs
        driver.find_element_by_xpath("html/body/div[2]/main/div[1]/div[2]/div/form/div[1]/div[1]/div/div[2]/ng-form/div[2]/div/ng-form/div[1]/div[2]/input").clear()
        driver.find_element_by_xpath("html/body/div[2]/main/div[1]/div[2]/div/form/div[1]/div[1]/div/div[2]/ng-form/div[2]/div/ng-form/div[1]/div[2]/input").send_keys(woman)
        driver.find_element_by_xpath("html/body/div[2]/main/div[1]/div[2]/div/form/div[1]/div[1]/div/div[2]/ng-form/div[2]/div/ng-form/div[1]/div[3]/input").clear()
        driver.find_element_by_xpath("html/body/div[2]/main/div[1]/div[2]/div/form/div[1]/div[1]/div/div[2]/ng-form/div[2]/div/ng-form/div[1]/div[3]/input").send_keys(surname)
        driver.find_element_by_xpath("html/body/div[2]/main/div[1]/div[2]/div/form/div[1]/div[1]/div/div[2]/ng-form/div[2]/div/ng-form/div[1]/div[1]/div/select/option[3]").click()

        #Child
        driver.find_element_by_xpath("html/body/div[2]/main/div[1]/div[2]/div/form/div[1]/div[1]/div/div[2]/ng-form/div[3]/div/ng-form/div[1]/div[1]/input").clear()
        driver.find_element_by_xpath("html/body/div[2]/main/div[1]/div[2]/div/form/div[1]/div[1]/div/div[2]/ng-form/div[3]/div/ng-form/div[1]/div[1]/input").send_keys(child)
        driver.find_element_by_xpath("html/body/div[2]/main/div[1]/div[2]/div/form/div[1]/div[1]/div/div[2]/ng-form/div[3]/div/ng-form/div[1]/div[2]/input").clear()
        driver.find_element_by_xpath("html/body/div[2]/main/div[1]/div[2]/div/form/div[1]/div[1]/div/div[2]/ng-form/div[3]/div/ng-form/div[1]/div[2]/input").send_keys(surname)

        #Contact
        driver.find_element_by_xpath("html/body/div[2]/main/div[1]/div[2]/div/form/div[1]/div[2]/div[2]/div[3]/div/div[1]/div[2]/input").clear()
        driver.find_element_by_xpath("html/body/div[2]/main/div[1]/div[2]/div/form/div[1]/div[2]/div[2]/div[3]/div/div[1]/div[2]/input").send_keys("test"+str(i)+"@gmail.com")
        driver.find_element_by_xpath("html/body/div[2]/main/div[1]/div[2]/div/form/div[1]/div[2]/div[2]/div[3]/div/div[1]/div[3]/div/div[1]/div/select/optgroup[1]/option[27]").click()
        driver.find_element_by_xpath("html/body/div[2]/main/div[1]/div[2]/div/form/div[1]/div[2]/div[2]/div[3]/div/div[1]/div[3]/div/div[2]/input").clear()
        driver.find_element_by_xpath("html/body/div[2]/main/div[1]/div[2]/div/form/div[1]/div[2]/div[2]/div[3]/div/div[1]/div[3]/div/div[2]/input").send_keys("666444333")

        #Card
        driver.find_element_by_xpath("html/body/div[2]/main/div[1]/div[2]/div/form/div[1]/div[2]/div[2]/div[5]/div/div[2]/div[1]/div/div/payment-method-card/div[1]/input").clear()
        driver.find_element_by_xpath("html/body/div[2]/main/div[1]/div[2]/div/form/div[1]/div[2]/div[2]/div[5]/div/div[2]/div[1]/div/div/payment-method-card/div[1]/input").send_keys("5555555555555557")
        driver.find_element_by_xpath("html/body/div[2]/main/div[1]/div[2]/div/form/div[1]/div[2]/div[2]/div[5]/div/div[2]/div[1]/div/div/payment-method-card/div[2]/div/div/select/option[3]").click()

        driver.find_element_by_xpath("html/body/div[2]/main/div[1]/div[2]/div/form/div[1]/div[2]/div[2]/div[5]/div/div[2]/div[1]/div/div/payment-method-card/div[3]/div[1]/div[1]/div/select/option[11]").click()
        driver.find_element_by_xpath("html/body/div[2]/main/div[1]/div[2]/div/form/div[1]/div[2]/div[2]/div[5]/div/div[2]/div[1]/div/div/payment-method-card/div[3]/div[1]/div[2]/div/div/select/option[4]").click()

        driver.find_element_by_xpath("html/body/div[2]/main/div[1]/div[2]/div/form/div[1]/div[2]/div[2]/div[5]/div/div[2]/div[1]/div/div/payment-method-card/div[3]/div[2]/div[2]/input").clear()
        driver.find_element_by_xpath("html/body/div[2]/main/div[1]/div[2]/div/form/div[1]/div[2]/div[2]/div[5]/div/div[2]/div[1]/div/div/payment-method-card/div[3]/div[2]/div[2]/input").send_keys("265")

        driver.find_element_by_xpath("html/body/div[2]/main/div[1]/div[2]/div/form/div[1]/div[2]/div[2]/div[5]/div/div[2]/div[1]/div/div/payment-method-card/div[4]/div/input").clear()
        driver.find_element_by_xpath("html/body/div[2]/main/div[1]/div[2]/div/form/div[1]/div[2]/div[2]/div[5]/div/div[2]/div[1]/div/div/payment-method-card/div[4]/div/input").send_keys(creditCard)

        #Billing address
        driver.find_element_by_xpath("html/body/div[2]/main/div[1]/div[2]/div/form/div[1]/div[2]/div[2]/div[5]/div/div[2]/div[2]/div[2]/div[1]/input").clear()
        driver.find_element_by_xpath("html/body/div[2]/main/div[1]/div[2]/div/form/div[1]/div[2]/div[2]/div[5]/div/div[2]/div[2]/div[2]/div[1]/input").send_keys("Testowa 1")
        driver.find_element_by_xpath("html/body/div[2]/main/div[1]/div[2]/div/form/div[1]/div[2]/div[2]/div[5]/div/div[2]/div[2]/div[2]/div[3]/div[1]/input").clear()
        driver.find_element_by_xpath("html/body/div[2]/main/div[1]/div[2]/div/form/div[1]/div[2]/div[2]/div[5]/div/div[2]/div[2]/div[2]/div[3]/div[1]/input").send_keys("Wroclaw")
        driver.find_element_by_xpath("html/body/div[2]/main/div[1]/div[2]/div/form/div[1]/div[2]/div[2]/div[5]/div/div[2]/div[2]/div[2]/div[3]/div[2]/input").clear()
        driver.find_element_by_xpath("html/body/div[2]/main/div[1]/div[2]/div/form/div[1]/div[2]/div[2]/div[5]/div/div[2]/div[2]/div[2]/div[3]/div[2]/input").send_keys("50-088")
        driver.find_element_by_xpath("html/body/div[2]/main/div[1]/div[2]/div/form/div[1]/div[2]/div[2]/div[5]/div/div[2]/div[2]/div[2]/div[3]/div[3]/div/select/optgroup[1]/option[27]").click()

        #Terms and services
        driver.find_element_by_xpath("html/body/div[2]/main/div[1]/div[2]/div/form/div[1]/div[2]/div[2]/div[7]/div[1]/input").click()
        driver.find_element_by_xpath("html/body/div[2]/main/div[1]/div[2]/div/form/div[1]/div[2]/div[2]/div[7]/div[2]/button").click()

        #Assert
        time.sleep(10)
        assert "As your payment was not authorised we could not complete your reservation. Please ensure that the information was correct or use a new payment to try again" in self.driver.find_element_by_xpath("html/body/div[2]/main/div[1]/div[2]/div/form/div[1]/div[2]/div[2]/div[5]/div/div[2]/prompt/div[2]").text
        print ("Correct Unauthorised message")

        #Take screenshoot
        driver.get_screenshot_as_file('errorUnauthorized.png')
        print ("Screenshoot saved")
        driver.quit()

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
