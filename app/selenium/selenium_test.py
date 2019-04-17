from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


driver = webdriver.Remote(command_executor = "http://web:4444/wd/hub", desired_capabilities = DesiredCapabilities.CHROME)

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