from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.firefox.options import Options
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        cap = DesiredCapabilities().FIREFOX
        cap["marionette"] = True
        opts = Options()
        opts.log.level = "trace"
        self.browser = webdriver.Firefox( executable_path="./geckodriver.exe", capabilities=cap, options=opts)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

if __name__ == '__main__':
    unittest.main(warnings='ignore')
    # assert 'To-Do' in browser.title, "Browser title was " + browser.title

# browser.quit()