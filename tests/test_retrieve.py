from constants import *
from utils import BasicTest


class TestRetrieve(BasicTest):
    def setUp(self):
        super(TestRetrieve, self).setUp()
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
        self.computer_name = COMPUTER_NAME

    def tearDown(self):
        self.delete_computer(self.computer_name)
        super(TestRetrieve, self).tearDown()

    def test_retrieve_computer(self):
        '''BB15: Test retrieve computer'''
        self.set_field('searchbox', COMPUTER_NAME)
        self.driver.find_element_by_id('searchbox').submit()
        link = self.driver.find_element_by_partial_link_text(COMPUTER_NAME)
        self.driver.get(link.get_attribute('href'))
        self.verify_fields_text([('name', COMPUTER_NAME),
                                 ('introduced', '2014-11-05'),
                                 ('discontinued', '2015-11-05'),
                                 ('company', 'Apple Inc.')])

    def test_retrieve_non_existing_computer(self):
        '''BB16: Test retrieve computer'''
        self.driver.get('http://computer-database.herokuapp.com/computers/9000')
        # Check for error page. P.S:currently it will load an empty page
        self.assertEqual(self.driver.page_source, '')
        self.assertEqual(self.driver.title, '')
