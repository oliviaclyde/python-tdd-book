from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
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
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)
        #User enters to-do item
        inputbox = self.browser.find_element_by_id('id_new_item')

        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to-do item')
        #User types "buy cookies" into text box
        inputbox.send_keys('Buy cookies')
        #User hits enter, pages will update, page will list "1: buy cookies" as an item in a to-do list
        inputbox.send_keys('Keys.ENTER')
        time.sleep(1)
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_element_by_tag_name('tr')
        self.assertTrue(
                any(row.text == '1: Buy cookies' for row in rows)
        )
        #Text box for input remains. User types another item: "Send cookies for class party"
        self.fail('Finish the test!')
        #Page updates again, and both items show on to-do list

        #User tests if site will remember the items entered. Site provides unique URL with some text explanation

        #User visits url - list is there

if __name__ == '__main__':
    unittest.main()