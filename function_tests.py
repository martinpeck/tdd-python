from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

  def setUp(self):
    self.browser = webdriver.Firefox()
    self.browser.implicitly_wait(3)

  def tearDown(self):
    self.browser.quit()

  def test_can_start_a_list_and_retrieve_it_later(self):

    # Bob goes to the home page
    self.browser.get('http://localhost:8000')

    # He notices that hte page title and header mention to-do lists
    self.assertIn('To-Do', self.browser.title)
    self.fail('Finish the test!')

    # He is invited to enter a to-do item straight away

    # He types "Buy cake ingredients" into a text box

    # He hits Enter, the page updates, and now the page lists "1: Buy cake ingredients" as an item in the to-do list

    # There is siltl a text box inviting him to add another item. He enters "Make a cake"

    # The page updates again, and now shows both items on his list

    # Bob sees that the site has generated a unique URL for his list - there is some explanatory text to that effect

    # He visits that URL - his to-do list is still there

if __name__ == '__main__':
  unittest.main()
