

import os

import unittest
from appium import webdriver


# Returns absoute path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
class SimpleAndroidTests(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
#Specify platform below(Android, iOS)
        desired_caps['platformName'] = 'Android'
#Specify OS version(Settings->About phone -> android version)
        desired_caps['platformVersion'] = '5.0.1'
#Obtain the Device name from Adb[For Android](Terminal Command: "adb devices")
        desired_caps['deviceName'] = 'TA93400A78'
#Specify the path to Application
        desired_caps['app'] = PATH('Chrome-com.android.chrome-2171093-v39.0.2171.93.apk')

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        # end the session
        self.driver.quit()


    def test_open_chrome(self):
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_id("com.android.chrome:id/terms_accept").click()
        self.driver.implicitly_wait(5)
        for i in range(0,3):
            self.driver.find_element_by_id("com.android.chrome:id/positive_button").click()
            self.driver.implicitly_wait(5)
        self.driver.find_element_by_id("com.android.chrome:id/menu_button").click()
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_name("New incognito tab").click()
        self.driver.implicitly_wait(5)
        self.driver.back()
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_name("Bookmarks").click()
        self.driver.implicitly_wait(5)
        self.driver.back()
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_name("Recent tabs").click()
        self.driver.implicitly_wait(5)
        self.driver.back()
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_name("History").click()
        self.driver.implicitly_wait(5)
        self.driver.back()
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_name("Bookmarks").click()
        self.driver.implicitly_wait(5)
        self.driver.back() 
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_name("Settings").click()
        self.driver.implicitly_wait(5)
        self.driver.find_elements_by_name("com.android.chrome:id/header_title").click()
        self.driver.implicitly_wait(5)
        self.driver.back()
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_name("Help & feedback").click()
        self.driver.implicitly_wait(5)
        self.driver.back()
        self.driver.implicitly_wait(5)
        
        
         
               
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
