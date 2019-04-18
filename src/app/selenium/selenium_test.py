import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import NoSuchElementException        

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
		driver.get("http://web:80/#/login/")

		try:
			driver.find_element_by_id('signUp')
		except NoSuchElementException:
			return False
		return True

	def test_email_field(self):
		driver = self.driver
		driver.get("http://web:80/#/login/")
		try:
			driver.find_element_by_id('email')
		except NoSuchElementException:
			return False
		return True

	def test_name_register(self):
		driver = self.driver
		driver.get("http://web:80/#/register/")

		name = driver.find_element_by_id("name")

		try:
			name.send_keys("Simmy", Keys.RETURN)
		except NoSuchElementException:
			return False
		return True

	def test_login_flow(self):
		driver = self.driver
		driver.get("http://web:80/#/register/")

		name = driver.find_element_by_id("name")
		last_name = driver.find_element_by_id("last_name")
		email = driver.find_element_by_id("email")
		password = driver.find_element_by_id("password")

		name.send_keys("Simmy", Keys.RETURN)
		name.send_keys("Yonathan", Keys.RETURN)
		name.send_keys("branden@gmail.com", Keys.RETURN)
		name.send_keys("hellothere", Keys.RETURN)

		time.sleep(5)

		driver.find_element_by_id("register").click()
		self.assertTrue("login" in driver.page_source)


	def test_logout_flow(self):
		driver = self.driver
		driver.get("http://web:80/#/register/")

		name = driver.find_element_by_id("name")
		last_name = driver.find_element_by_id("last_name")
		email = driver.find_element_by_id("email")
		password = driver.find_element_by_id("password")

		name.send_keys("Simmy", Keys.RETURN)
		name.send_keys("Yonathan", Keys.RETURN)
		name.send_keys("branden@gmail.com", Keys.RETURN)
		name.send_keys("hellothere", Keys.RETURN)

		time.sleep(5)
		driver.find_element_by_id("register").click()
		time.sleep(5)
		self.assertFalse("logout" in driver.page_source)

	def test_post_creation(self):
		driver = self.driver
		driver.get("http://web:80/#/")

		detail = driver.find_element_by_id("details").click()
		time.sleep(5)

		assert "postDetail" in driver.current_url

		assert asdfadf



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