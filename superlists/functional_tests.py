from selenium import webdriver
import unittest

class NewVistiorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retreive_it_later(self):

        #User navigates to app homepage
        self.browser.get('http://localhost:8000')
        #User views page title and header as to-do lists
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')
        #User enters to-do item

        #User types "buy cookies" into text box

        #User hits enter, pages will update, page will list "1: buy cookies" as an item in a to-do list

        #Text box for input remains. User types another item: "Send cookies for class party"

        #Page updates again, and both items show on to-do list

        #User tests if site will remember the items entered. Site provides unique URL with some text explanation

        #User visits url - list is there

if __name__ == '__main__':
    unittest.main()