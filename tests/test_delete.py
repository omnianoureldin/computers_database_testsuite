from constants import *
from utils import BasicTest


class TestDelete(BasicTest):
    def setUp(self):
        super(TestDelete, self).setUp()
        self.driver.get(NEW_COMPUTER_URL)
        self.set_fields([('name', COMPUTER_NAME),
                         ('introduced', '2014-11-05'),
                         ('discontinued', '2015-11-05'),
                         ('company', 'Apple Inc.')])
        self.press_button(BUTTONS.create_this_computer)
        self.assertEquals(
                self.driver.current_url, HOME_URL)
        alert = self.driver.find_element_by_xpath('//div[@class="alert-message warning"]')
        self.assertEqual(alert.text, u'Done! Computer %s has been created' % COMPUTER_NAME)
        self.load_computer(COMPUTER_NAME)

    def test_delete_computer(self):
        '''BB17: Test delete computer'''
        computer_url = self.driver.current_url
        self.press_button(BUTTONS.delete_this_computer)
        self.assertEquals(
                self.driver.current_url, HOME_URL)
        alert = self.driver.find_element_by_xpath('//div[@class="alert-message warning"]')
        self.assertEqual(alert.text, u'Done! Computer has been deleted')

        # Try to retrieve the computer after deletion
        self.driver.get(computer_url)
        # Check for error page. P.S:currently it will load an empty page
        self.assertEqual(self.driver.page_source, '')
        self.assertEqual(self.driver.title, '')
