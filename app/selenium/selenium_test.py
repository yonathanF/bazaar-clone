import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class PythonOrgSearch(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Remote(command_executor = "http://selenium-chrome:4444/wd/hub", desired_capabilities = DesiredCapabilities.CHROME)

	def test_search_in_python_org(self):
		driver = self.driver
		driver.get("http://www.python.org")
		self.assertIn("Python", driver.title)
		elem = driver.find_element_by_name("q")
		elem.send_keys("pycon")
		elem.send_keys(Keys.RETURN)
		assert "No results found." not in driver.page_source

	def test_connection_works(self):
		driver = self.driver
		driver.get("http://web:4444/")
		assert "No results found." not in driver.page_source

	def test_new_account(self):
		driver = self.driver
		driver.get("http://web:8003/#/login/")

		body = driver.find_element_by_id('pLEASEWORK')
		print("did you find it?" ,body)
		#WebElement formElement = driver.findElement(By.id("loginForm"));
	
	#def test_homepage_fetch_id(self):


	def tearDown(self):
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