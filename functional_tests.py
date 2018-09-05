from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.firefox.options import Options
import unittest

# Python 3.7.0; Django 2.1.1; Selenium 3.14.0; Geckodriver 0.21.0

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        # Ran up against an issue trying to run Selenium/Geckodriver on windows; 
        # added Firefox Desired Capabilities and it worked fine; default setting of marionette is true, but I forced it 
        cap = DesiredCapabilities().FIREFOX
        cap["marionette"] = True
        opts = Options()
        opts.log.level = "trace"
        self.browser = webdriver.Firefox(executable_path="./geckodriver.exe", capabilities=cap, options=opts)

    def tearDown(self):
        # automatic quit after tests are complete
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # The Django default page is so cool I want to use it as the home page for my new To-Do app
        self.browser.get('http://localhost:8000')
        # But, I'm only going to use it if it has 'To Do' in the title, otherwise I'll build my own
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

    # More tests here as the application expands

if __name__ == '__main__':
    unittest.main(warnings='ignore')
    # assert 'To-Do' in browser.title, "Browser title was " + browser.title

# browser.quit()