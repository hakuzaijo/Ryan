# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import unittest, time, random
#import names
'''
i = random.randrange(0,99999999, 20)
i = random.randrange(0,99999999, 20)
man = names.get_first_name(gender='male')
woman = names.get_first_name(gender='female')
child = names.get_first_name()
surname = names.get_last_name()
creditCard = names.get_full_name()
'''
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

'''

webpage = "https://www.ryanair.com/ie/en/"

class Ryanair(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.fromCountry = {'All countries': '1',
                        'Austria': '2',
                        'Belgium': '3',
                        'Bulgaria': '4',
                        'Croatia': '5',
                        'Cyprus': '6',
                        'Czech Republic': '7',
                        'Denmark': '8',
                        'Estonia': '9',
                        'Finland': '10',
                        'France': '11',
                        'Germany': '12',
                        'Greece': '13',
                        'Hungary': '14',
                        'Ireland': '15',
                        'Israel': '16',
                        'Italy': '17',
                        'Latvia': '18',
                        'Lithuania': '19',
                        'Malta': '20',
                        'Montenegro': '21',
                        'Morocco': '22',
                        'Netherlands': '23',
                        'Norway': '24',
                        'Poland': '25',
                        'Portugal': '26',
                        'Romania': '27',
                        'Slovakia': '28',
                        'Spain': '29',
                        'Sweden': '30',
                        'Switzerland': '31',
                        'United Kingdom': '32'}
        self.irelandAirport = {'Cork': '3',
                           'Dublin': '4',
                           'Kerry': '5',
                           'Knock': '6',
                           'Shannon': '7'
                           }
        self.toCountryIfIrelandWasChosen = {'Austria':'2',
                        'Belgium':'3',
                        'Bulgaria':'4',
                        'Croatia':'5',
                        'Czech Republic':'6',
                        'Denmark':'7',
                        'Estonia':'8',
                        'France':'9',
                        'Germany':'10',
                        'Greece':'11',
                        'Hungary':'12',
                        'Italy':'13',
                        'Latvia':'14',
                        'Lithuania':'15',
                        'Malta':'16',
                        'Morocco':'17',
                        'Netherlands':'18',
                        'Norway':'19',
                        'Poland':'20',
                        'Portugal':'21',
                        'Romania':'22',
                        'Slovakia':'23',
                        'Spain':'24',
                        'Switzerland':'25',
                        'United Kingdom':'26'

                        }
        self.germanyAirport = {
            'Berlin(SXF)':'3',
            'Bremen':'4',
            'Cologne':'5',
            'Frankfurt(HHN)':'6',
            'Hamburg':'7',
            'Memmingen':'8'
        }
        self.typeOfFlight = {
            'Return':"1",
            "One way":"2"
        }


    def test_ryanair(self):
        driver = self.driver
        self.driver.get(webpage)
        #driver.maximize_window()
        time.sleep(1)

        self.chooseFrom('Ireland', 'Dublin')
        self.returnOrOneWay()
        self.chooseTo('Germany', 'Berlin (SXF)')



    def chooseFrom(self, countryFrom, airportFrom):
        self.fromField = "html/body/div[2]/main/article/div[2]/div/div[2]/div/div/form/div[1]/div[2]/div/div[1]/div[2]/div[2]/div/div[1]/input"
        self.fromCountryXpath = "html/body/div[2]/main/article/div[2]/div/div[2]/div/div/form/div[1]/div[2]/div/div[1]/div[3]/div/div/div[2]/popup-content/core-linked-list/div[1]/div/div["
        self.fromAirportXpath = "html/body/div[2]/main/article/div[2]/div/div[2]/div/div/form/div[1]/div[2]/div/div[1]/div[3]/div/div/div[2]/popup-content/core-linked-list/div[2]/div/div["

        self.driver.find_element_by_xpath(self.fromField).clear()
        time.sleep(2)
        self.driver.find_element_by_xpath(self.fromField).click()
        time.sleep(1)
        self.driver.find_element_by_xpath(self.fromCountryXpath+str(self.fromCountry[countryFrom])+"]").click()
        time.sleep(1)
        self.driver.find_element_by_xpath(self.fromAirportXpath+str(self.irelandAirport[airportFrom])+"]").click()


    def chooseTo(self, countryTo, airportTo):
        self.toField = "html/body/div[2]/main/article/div[2]/div/div[2]/div/div/form/div[1]/div[2]/div/div[2]/div[2]/div[2]/div/div[1]/input"
        self.toCountryXpath = "html/body/div[2]/main/article/div[2]/div/div[2]/div/div/form/div[1]/div[2]/div/div[2]/div[3]/div/div/div[2]/popup-content/core-linked-list/div[1]/div/div["
        self.toAirportXpath = "html/body/div[2]/main/article/div[2]/div/div[2]/div/div/form/div[1]/div[2]/div/div[2]/div[3]/div/div/div[2]/popup-content/core-linked-list/div[2]/div/div["

        self.driver.find_element_by_xpath(self.toField).click()
        time.sleep(1)
        self.driver.find_element_by_xpath(self.toCountryXpath + str(self.toCountryIfIrelandWasChosen[countryTo])+"]").click()
        time.sleep(1)
        self.driver.find_element_by_xpath(self.toAirportXpath + str(self.germanyAirport[airportTo]) + "]").click()


    def returnOrOneWay(self):
        self.typeOfFlightButton = "html/body/div[2]/main/article/div[2]/div/div[2]/div/div/form/div[1]/div[1]/div["
        self.driver.find_element_by_xpath(self.typeOfFlightButton + str(self.typeOfFlight['One way']) + "]/input").click()
        time.sleep(1)

        '''
        #Fly out
        driver.find_element_by_xpath("//div[@id='search-container']/div/form/div[3]/button").click()
        driver.find_element_by_css_selector("div.select-date.placeholder").click()
        driver.find_element_by_xpath("//div[@id='row-dates-pax']/div/div/div/div/div[3]/div/div/div[2]/core-datepicker/div/ul/li/ul[2]/li[12]/span").click()
        #Passangers
        driver.find_element_by_css_selector("div.dropdown-handle > core-icon.chevron > div > svg").click()
        driver.find_element_by_xpath("(//button[@type='button'])[2]").click()
        driver.find_element_by_xpath("(//button[@type='button'])[6]").click()
        time.sleep(8)
        driver.find_element_by_xpath("//div[@id='search-container']/div/form/div[3]/button[2]").click()
        time.sleep(8)

        #Price
        driver.find_element_by_xpath("html/body/div[2]/main/div[1]/section/div/div[1]/div/div[3]/div/div/div[2]/div[2]/div[1]/div[2]/div[2]/div/span[1]").click()
        time.sleep(8)
        driver.find_element_by_xpath("html/body/div[2]/main/section/div/section[2]/article/div[2]/section/div[2]/button").click()
        time.sleep(8)

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
        '''


    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
