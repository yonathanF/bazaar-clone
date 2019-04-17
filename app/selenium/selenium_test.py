import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class PythonOrgSearch(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Remote(command_executor = "http://selenium-chrome:4444/wd/hub", desired_capabilities = DesiredCapabilities.CHROME)
		print("do you get down to here?")

	def test_visit_site_with_chrome(self):
		self.chrome.get('http://127.0.0.1:8003')
		print("here??")
		self.assertNotEquals(self.chrome.title, 'Django: the Web framework for perfectionists with deadlines.')
	
	def tearDown(self):
   		print("what about here???????")
   		self.driver.close()

if __name__ == "__main__":
    unittest.main()


# RemoteWebDriver driver = chrome.getWebDriver();
# driver.get("http://" + chrome.getTestHostIpAddress() + ":8080/");

# WebDriver driver = new FirefoxDriver();

# driver.get(“http://www.google.com”);


# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--window-size=1420,1080')
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-gpu')
# driver = webdriver.Chrome(chrome_options=chrome_options)