
"""

sandisk media drive

@author: kc@sandisk
"""
import os

from time import sleep


import unittest

from appium import webdriver


# Returns absolute path relative to this file and not cwd
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
        desired_caps['app'] = PATH('Media Drive-com.sandisk.scotti-55-v2.0.3.apk')

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        # end the session
        self.driver.quit()

    def test_images_copy(self):
        self.driver.implicitly_wait(5)
# for swiping through welcome screen
        for i in range(0,4):
            self.driver.find_element_by_id("com.sandisk.scotti:id/txt_Next").click()
            self.driver.implicitly_wait(5)
        self.driver.find_element_by_id("com.sandisk.scotti:id/txt_Close").click()
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_name("OK").click()
        self.driver.implicitly_wait(5)
#Select photos from dislpayed list of items
        self.driver.find_element_by_id("com.sandisk.scotti:id/txt_Photo").click()
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_id("com.sandisk.scotti:id/btn_Switch_Local").click()
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_id("com.sandisk.scotti:id/txt_Name").click()
        self.driver.implicitly_wait(5)
#Select all photos in the open folder
        for i in range(0,2):
            self.driver.find_element_by_id("com.sandisk.scotti:id/imgbtn_Upload").click()
            self.driver.implicitly_wait(5)
# Select drive storage
        self.driver.find_element_by_id("com.sandisk.scotti:id/txt_Name").click()
        self.driver.implicitly_wait(5)
#start uploading files
        self.driver.find_element_by_name("Copying Files")
        sleep(999)
        self.driver.find_element_by_name("OK").click
        self.driver.back()
        self.driver.find_element_by_id("com.sandisk.scotti:id/btn_Switch_Drive").click()
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_id("com.sandisk.scotti:id/txt_Name").click()
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_id("com.sandisk.scotti:id/imgbtn_Upload").click()
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_class_name("android.widget.FrameLayout").click()
        self.driver.implicitly_wait(99)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
