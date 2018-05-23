import time, unittest
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

print("========================================")
print("     Coinpepe automation tests")
print("========================================")
print("")
print("")


class Coinpepe(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("/Users/proaccount/Documents/WebDriver/chromedriver") # path to chromedriver
        self.now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

    def test_coin_117(self):
        now = self.now
        driver = self.driver
        driver.get("http://coinpepe-dev.herokuapp.com/")
        time.sleep(3)
        self.assertIn("Coinpepe", driver.title)
        elem = driver.find_elements_by_css_selector("input")[0]
        elem.send_keys("jesus", Keys.ARROW_DOWN)
        time.sleep(1)
        elem.send_keys(Keys.RETURN)
        title = self.driver.title
        url = driver.current_url
        print(url)
        try:
            self.assertIn("jesus-coin", url)
        except AssertionError:
            driver.get_screenshot_as_file('%s -%s.png' % (title, now))
            raise
        time.sleep(1)

    def test_coin_148(self):
        now = self.now
        driver = self.driver
        driver.get("http://coinpepe-dev.herokuapp.com/add-event")
        time.sleep(3)
        self.assertIn("Coinpepe", driver.title)
        title = self.driver.title
        elem = driver.find_elements_by_tag_name('label')[7]
        elem = elem.text
        print(elem)
        try:
            self.assertIn("donations", elem)
        except AssertionError:
            driver.get_screenshot_as_file('%s -%s.png' % (title, now))
            raise
        time.sleep(1)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
