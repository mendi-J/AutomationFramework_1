# from selenium import  webdriver
import allure
import pytest
import  moment
from pages.loginPage import  LoginPage
from pages.homePage import  HomePage
from utils import  utils as utils

@pytest.mark.usefixtures("test_setup")
class TestLogin():

    def test_login(self):
        driver = self.driver
        driver.get(utils.URL)

        login = LoginPage(driver)
        login.enter_username(utils.USERNAME)
        login.enter_password(utils.PASSWORD)
        login.click_login()

    def test_logout(self):
        try:
            driver = self.driver
            homepage = HomePage(driver)
            homepage.click_welcome()
            homepage.click_logout()
            x = driver.title
            assert  x == "abc"      #This will fail because the driver title is not abc
            # assert x == "OrangeHRM"  # This will pass because the driver title is OrangeHRM
        except AssertionError as error:
            print("Assertion error occurred")
            print(error)
            currTime = moment.now().strftime("%d-%m-%Y_%H:%M:%S")
            testName = utils.whoami()
            screenshotNmae = testName+ "_"+currTime
            allure.attach(self.driver.get_screenshot_as_png(),name=screenshotNmae,
                                    attachment_type=allure.attachment_type.PNG )         #Naming your screenshots attached as "screenshot" is not a good method incase of multiple screenshots.

            driver.get_screenshot_as_file("C:/Users/Ndifreke/PycharmProjects/AutomationFramework/screenshots/" + screenshotNmae + " .PNG")
            raise

        except:
            print("there was an exception")
            currTime = moment.now().strftime("%d-%m-%Y_%H:%M:%S")
            testName = utils.whoami()
            screenshotNmae = testName + "_" + currTime
            allure.attach(self.driver.get_screenshot_as_png(), name=screenshotNmae, attachment_type=allure.attachment_type.PNG)
            raise

        else:
            print("No exceptions occured")

        finally:
            print("I am inside final block")

