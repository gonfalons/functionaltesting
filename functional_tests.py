from selenium import webdriver
import unittest


class NewvisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_start_list_retrieve(self):
        # Edith has heard about a cool online to-do app. She goes to checkout
        # its home page,
        self.browser.get('http://localhost:8000')
        # Notices its right -- page title and header mention to-do lists.
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')
        # She is invited to enter a to-do task straight awa
        # she types buy peacock feathres into text box
        # When she hits enter, page updates, and page lists :
        # #1: Buy peacock feathers as an item in the to-do list
        # There is still a text box inviting her to add another item. She methodically enters:
        # #2: Use peacock feathers as a to-do item
        # Page updates again, now shows both items in list
        # edith wonders whether site will rememebr her list -- but sees it generates a unique URL
        # for her. Site explains that it is remembered. She checks URL -- her to-do
        # list is still there. Assured, she goes to sleep.


if __name__ == '__main__':
    unittest.main()
