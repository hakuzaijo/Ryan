# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import unittest, time, random


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
            'Berlin (SXF)':'3',
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

        #month == 7columns, 6 rows
        self.firstMonth ={
            '1c1r':'1',
            '2c1r':'2',
            '3c1r':'3',
            '4c1r':'4',
            '5c1r':'5',
            '6c1r':'6',
            '7c1r':'7',
            '1c2r':'8',
            '2c2r':'9',
            '3c2r':'10',
            '4c2r':'11',
            '5c2r':'12',
            '6c2r':'13',
            '7c2r':'14',
            '1c3r':'15',
            '2c3r':'16',
            '3c3r':'17',
            '4c3r':'18',
            '5c3r':'19',
            '6c3r':'20',
            '7c3r':'21',
            '1c4r':'22',
            '2c4r':'23',
            '3c4r':'24',
            '4c4r':'25',
            '5c4r':'26',
            '6c4r':'27',
            '7c4r':'28',
            '1c5r':'29',
            '2c5r':'30',
            '3c5r':'31',
            '4c5r':'32',
            '5c5r':'33',
            '6c5r':'34',
            '7c5r':'35',
            '1c6r':'36',
            '2c6r':'37',
            '3c6r':'38',
            '4c6r':'39',
            '5c6r':'40',
            '6c6r':'41',
            '7c6r':'42'
        }
        #month == 7columns, 6 rows
        self.secondMonth ={
            '1c1r':'1',
            '2c1r':'2',
            '3c1r':'3',
            '4c1r':'4',
            '5c1r':'5',
            '6c1r':'6',
            '7c1r':'7',
            '1c2r':'8',
            '2c2r':'9',
            '3c2r':'10',
            '4c2r':'11',
            '5c2r':'12',
            '6c2r':'13',
            '7c2r':'14',
            '1c3r':'15',
            '2c3r':'16',
            '3c3r':'17',
            '4c3r':'18',
            '5c3r':'19',
            '6c3r':'20',
            '7c3r':'21',
            '1c4r':'22',
            '2c4r':'23',
            '3c4r':'24',
            '4c4r':'25',
            '5c4r':'26',
            '6c4r':'27',
            '7c4r':'28',
            '1c5r':'29',
            '2c5r':'30',
            '3c5r':'31',
            '4c5r':'32',
            '5c5r':'33',
            '6c5r':'34',
            '7c5r':'35',
            '1c6r':'36',
            '2c6r':'37',
            '3c6r':'38',
            '4c6r':'39',
            '5c6r':'40',
            '6c6r':'41',
            '7c6r':'42'
        }
        self.passangersType = {
            'Adults':'6',
            'Teens':'7',
            'Children':'8',
            'Infants':'9'
        }
        self.passangersChange = {
            'add':'2',
            'subtract':'1'
        }
        self.fareType = {
            'standard':'2',
            'business':'3'
        }
        self.title = {
            'Mr':'2',
            'Mrs':'3',
            'Ms':'4'
        }
        self.names = {
            'adult1NameXpath':'1',
            'adult2NameXpath':'2',
            'children1NameXpath':'3'
        }
        self.surnames = {
            'adult1SurnameXpath': '1',
            'adult2SurnameXpath': '2',
            'children1SurnameXpath': '3'
        }
        self.i = random.randrange(0,99999999, 20)
        self.countryDropDown = {'Poland':'27'} #add more countries

    def test_ryanair(self):
        driver = self.driver
        self.driver.get(webpage)
        #driver.maximize_window()
        time.sleep(1)

        self.chooseFrom('Ireland', 'Dublin')
        self.returnOrOneWay()
        self.chooseTo('Germany', 'Berlin (SXF)')
        self.flyOut('5c5r')  #5column & 5row = 29(Friday).04.2016
        self.passangerDropDownMenu()
        self.passangerPicker('Adults', 'add')
        self.passangerPicker('Children', 'add')
        self.letsGoButton()
        self.chooseFareType('standard')
        self.continueFromFarePage()
        self.closeExtrasPopUp()
        self.checkOutButton()
        self.adult1DetailsFill('Test', 'Testowy', 'Mr')
        self.adult2DetailsFill('Testa', 'Testowa', 'Mrs')
        self.children1DetailsFill('Tescik', 'Tescikowy')
        self.contactDetailsFill("test","@gmail.com",'Poland',"666444333")

    def chooseFrom(self, countryFrom, airportFrom):
        self.fromField = "html/body/div[2]/main/article/div[2]/div/div[2]/div/div/form/div[1]/div[2]/div/div[1]/div[2]/div[2]/div/div[1]/input"
        self.fromCountryXpath = "html/body/div[2]/main/article/div[2]/div/div[2]/div/div/form/div[1]/div[2]/div/div[1]/div[3]/div/div/div[2]/popup-content/core-linked-list/div[1]/div/div["
        self.fromAirportXpath = "html/body/div[2]/main/article/div[2]/div/div[2]/div/div/form/div[1]/div[2]/div/div[1]/div[3]/div/div/div[2]/popup-content/core-linked-list/div[2]/div/div["

        self.driver.find_element_by_xpath(self.fromField).clear()
        time.sleep(2)
        self.driver.find_element_by_xpath(self.fromField).click()
        time.sleep(2)
        self.driver.find_element_by_xpath(self.fromCountryXpath+str(self.fromCountry[countryFrom])+"]").click()
        time.sleep(2)
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
        time.sleep(1)

    def returnOrOneWay(self):
        self.typeOfFlightButton = "html/body/div[2]/main/article/div[2]/div/div[2]/div/div/form/div[1]/div[1]/div["
        self.driver.find_element_by_xpath(self.typeOfFlightButton + str(self.typeOfFlight['One way']) + "]/input").click()
        time.sleep(1)

    def flyOut(self, dateOfFloutOut):
        self.flyOutField = ".//*[@id='row-dates-pax']/div[1]/div/div[1]/div/div[2]/div[2]/div/input[3]"

        self.firstMonthDate = ".//*[@id='row-dates-pax']/div[1]/div/div[1]/div/div[3]/div/div/div[2]/popup-content/core-datepicker/div[1]/ul/li[1]/ul[2]/li["
        self.secondMonthDate = ".//*[@id='row-dates-pax']/div[1]/div/div[1]/div/div[3]/div/div/div[2]/popup-content/core-datepicker/div[1]/ul/li[2]/ul[2]/li["

        #use only if date picker will be used later
        #self.driver.find_element_by_xpath(self.flyOutField).click()
        time.sleep(1)
        self.driver.find_element_by_xpath(self.firstMonthDate + str(
            self.firstMonth[dateOfFloutOut])+"]/span").click()
        time.sleep(1)

        #use onyly if you want to pick second month date instead of first
        #self.driver.find_element_by_xpath(self.secondMonthDate + str(
        #    self.secondMonth['5c5r'])+"]/span").click()

    def passangerDropDownMenu(self):
        self.passangerChangeButton = ".//*[@id='row-dates-pax']/div[2]/div[" \
                          "3]/div/div/div[2]/popup-content/div["

        self.driver.find_element_by_xpath(".//*[@id='row-dates-pax']/div["
                                          "2]/div[2]/div[2]/div/div[1]").click()
        time.sleep(1)

    def passangerPicker(self, passanger, change):

        self.driver.find_element_by_xpath(self.passangerChangeButton +
                                          str(self.passangersType[passanger])+
                                          ']/div/div[3]/core-inc-dec/button['+
                                          str(self.passangersChange[change])+']').click()

        time.sleep(1)

    def letsGoButton(self):
        self.driver.find_element_by_xpath(".//*["
                                          "@id='search-container']/div/div/form/div[3]/button[2]").click()
        time.sleep(8)

    def chooseFareType(self, fareToChoose):
        time.sleep(1)

        self.fare = ".//*[@id='outbound']/div/div[3]/div/div/div[2]/div[" \
                    "1]/div[1]/div[2]/div["


        self.driver.find_element_by_xpath(self.fare + str(self.fareType[
            fareToChoose])+"]/div/span[1]").click()

        time.sleep(1)

    def continueFromFarePage(self):
        self.driver.find_element_by_xpath(".//*[@id='continue']").click()
        time.sleep(5)

    def closeExtrasPopUp(self):
        self.driver.find_element_by_xpath("html/body/div[8]/div[2]/div[1]/div/div[1]").click()
        time.sleep(1)

    def checkOutButton(self):
        self.checkout = ".//*[@id='booking-selection']/article/div[2]/section/div[2]/button"
        self.driver.find_element_by_xpath(self.checkout)
        time.sleep(5)

    def passangerDetailsXpath(self):
        self.name = "html/body/div[2]/main/div[1]/div[2]/div/form/div[1]/div[1]/div/div[2]/ng-form/div["
        self.surname = "html/body/div[2]/main/div[1]/div[2]/div/form/div[1]/div[1]/div/div[2]/ng-form/div["
        self.titleDropdown = "html/body/div[2]/main/div[1]/div[2]/div/form/div[1]/div[1]/div/div[2]/ng-form/div[1]/div/ng-form/div[1]/div[1]/div/select/option["
        self.emailField = "html/body/div[2]/main/div[1]/div[2]/div/form/div[1]/div[2]/div[2]/div[3]/div/div[1]/div[2]/input"
        self.phoneNumberDropDown = "html/body/div[2]/main/div[1]/div[2]/div/form/div[1]/div[2]/div[2]/div[3]/div/div[1]/div[3]/div/div[1]/div/select/optgroup[1]/option["
        self.phoneNumberField = "html/body/div[2]/main/div[1]/div[2]/div/form/div[1]/div[2]/div[2]/div[3]/div/div[1]/div[3]/div/div[2]/input"

    def adult1DetailsFill(self, adultName1, adultsurname1, title1):

        self.driver.find_element_by_xpath(self.name+str(self.names['adult1NameXpath']+
                                                        "]/div/ng-form/div[1]/div[2]/input")).clear()
        self.driver.find_element_by_xpath(self.name+str(self.names['adult1NameXpath']+
                                                        "]/div/ng-form/div[1]/div[2]/input")).send_keys(adultName1)

        self.driver.find_element_by_xpath(self.surname + str(self.names['adult1SurnameXpath'] +
                                                             "]/div/ng-form/div[1]/div[2]/input")).clear()
        self.driver.find_element_by_xpath(self.surname + str(self.names['adult1SurnameXpath'] +
                                                             "]/div/ng-form/div[1]/div[2]/input")).send_keys(adultsurname1)

        self.driver.find_element_by_xpath(self.titleDropdown+str(self.title[title1])+ "]").click()

    def adult2DetailsFill(self, adultName2, adultsurname2, title2):

        self.driver.find_element_by_xpath(self.name + str(self.names['adult2NameXpath'] +
                                                          "]/div/ng-form/div[1]/div[2]/input")).clear()
        self.driver.find_element_by_xpath(self.name + str(self.names['adult2NameXpath'] +
                                                          "]/div/ng-form/div[1]/div[2]/input")).send_keys(adultName2)

        self.driver.find_element_by_xpath(self.surname + str(self.names['adult2SurnameXpath'] +
                                                             "]/div/ng-form/div[1]/div[2]/input")).clear()
        self.driver.find_element_by_xpath(self.surname + str(self.names['adult2SurnameXpath'] +
                                                             "]/div/ng-form/div[1]/div[2]/input")).send_keys(adultsurname2)

        self.driver.find_element_by_xpath(self.titleDropdown + str(self.title[title2]) + "]").click()

    def children1DetailsFill(self, childrenName1, childrensurname2):
        self.driver.find_element_by_xpath(self.name + str(self.names['children1NameXpath'] +
                                                          "]/div/ng-form/div[1]/div[1]/input")).clear()
        self.driver.find_element_by_xpath(self.name + str(self.names['children1NameXpath'] +
                                                      "]/div/ng-form/div[1]/div[1]/input")).send_keys(childrenName1)

        self.driver.find_element_by_xpath(self.surname + str(self.names['children1SurnameXpath'] +
                                                             "]/div/ng-form/div[1]/div[2]/input")).clear()

        self.driver.find_element_by_xpath(self.surname + str(self.names['children1SurnameXpath'] +
                                                         "]/div/ng-form/div[1]/div[2]/input")).send_keys(childrensurname2)

    def contactDetailsFill(self, mail, domain, country, phonenumber):
        self.driver.find_element_by_xpath(self.emailField).clear()
        self.driver.find_element_by_xpath(self.emailField).clear(mail+str(self.i)+domain)
        self.driver.find_element_by_xpath(self.phoneNumberDropDown+str(self.countryDropDown[country]+"]")).click()
        self.driver.find_element_by_xpath(self.phoneNumberField).clear()
        self.driver.find_element_by_xpath(self.phoneNumberField).send_keys(phonenumber)
    '''


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
