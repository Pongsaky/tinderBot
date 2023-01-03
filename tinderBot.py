from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from time import sleep

class TinderBot:
    def __init__(self, phoneNumber):
        capabilities = DesiredCapabilities().CHROME

        chrome_options = Options()
        chrome_options.add_argument("--incognito")
        chrome_options.add_argument("--disable-infobars")
        chrome_options.add_argument("start-maximized")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--disable-popup-blocking")

        prefs = {
            'profile.default_content_setting_values':
            {
                'notifications': 1,
                'geolocation': 1
            },

            'profile.managed_default_content_settings':
            {
                'geolocation': 1
            },
        }

        chrome_options.add_experimental_option('prefs', prefs)
        capabilities.update(chrome_options.to_capabilities())

        self.driver = webdriver.Chrome(options=chrome_options)
        self.phoneNumber = phoneNumber

    def openTinder(self):
        self.driver.get("https://tinder.com")
        sleep(2)

        # login menu
        login = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a")
        login.click()
        sleep(2)

        self.loginPhoneNumber()

    def loginPhoneNumber(self):
        login = self.driver.find_element(By.XPATH, "/html/body/div[2]/main/div/div[1]/div/div/div[3]/span/div[3]/button")
        login.click()
        sleep(4)

        numberPhoneInput = self.driver.find_element(By.XPATH, '/html/body/div[2]/main/div/div[1]/div/div[2]/div/input')
        btnNumber = self.driver.find_element(By.XPATH, "/html/body/div[2]/main/div/div[1]/div/button")
        numberPhoneInput.send_keys(self.phoneNumber)
        btnNumber.click()
        sleep(2)

        # auth code from phone number
        code_phone = input("Enter your code: ")
        for idx, c in enumerate(code_phone):
            self.driver.find_element(By.XPATH, "/html/body/div[2]/main/div/div[1]/div/div[3]/input[{}]".format(idx+1)).send_keys(c)

        btnCode = self.driver.find_element(By.XPATH, '/html/body/div[2]/main/div/div[1]/div/button')
        btnCode.click()
        sleep(2)

        try:
            # send code to email
            btnSend = self.driver.find_element(By.XPATH, "/html/body/div[2]/main/div/div/div[1]/div/div[2]/button")
            btnSend.click()
            sleep(2)
        except:
            print("Don't have send email button")
        
        #auth code from gmail
        code_gmail = input("Enter your gmail code :")
        for idx, c in enumerate(code_gmail):
            self.driver.find_element(By.XPATH, f"/html/body/div[2]/main/div/div/div[1]/div/div[3]/input[{idx+1}]").send_keys(c)

        btnMail = self.driver.find_element(By.XPATH, "/html/body/div[2]/main/div/div/div[1]/div/button")
        btnMail.click()
        sleep(2)

        self.allowLocation()

    def allowLocation(self):
        try:
            allowBtn = self.driver.find_element(By.XPATH, "/html/body/div[2]/main/div/div/div/div[3]/button[1]")
            allowBtn.click()
            sleep(2)
        except:
            print("no location popup")
    
phoneNumber = "" # input your phone number
tinderBot = TinderBot(phoneNumber)
tinderBot.openTinder()
sleep(10)