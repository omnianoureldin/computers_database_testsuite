from utils import BasicTest
from constants import *
from nose_parameterized import parameterized
from selenium.common.exceptions import NoSuchElementException


class TestUpdate(BasicTest):
    def setUp(self):
        super(TestUpdate, self).setUp()
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
        self.computer_name = COMPUTER_NAME

    def tearDown(self):
        self.delete_computer(self.computer_name)
        super(TestUpdate, self).tearDown()

    def test_update_without_changes(self):
        '''BB8: Test update without changes'''
        self.press_button(BUTTONS.save_this_computer)
        self.assertEquals(
                self.driver.current_url, HOME_URL)
        alert = self.driver.find_element_by_xpath('//div[@class="alert-message warning"]')
        self.assertEqual(alert.text, u'Done! Computer %s has been updated' % COMPUTER_NAME)

    def test_cancel_update(self):
        '''BB9: Test cancel update without changes'''
        self.press_button(BUTTONS.cancel)
        self.assertEquals(
                self.driver.current_url, HOME_URL)
        self.assertRaises(
                NoSuchElementException, self.driver.find_element_by_xpath, '//div[@class="alert-message warning"]')

    @parameterized.expand([('valid', 'valid computer', '2014-11-05', '2015-11-05', 'IBM'),
                           ('invalid', '', '05-11-2014', 'date', 'IBM')])
    def test_cancel_update_with_data(self, _, name, introduced_date, discontinued_date, company):
        '''BB10: Test cancel update after populating fields with valid/invalid values'''
        self.set_fields([('name', name),
                         ('introduced', introduced_date),
                         ('discontinued', discontinued_date),
                         ('company', company)])
        self.press_button(BUTTONS.cancel)
        self.assertEquals(
                self.driver.current_url, HOME_URL)
        self.assertRaises(
                NoSuchElementException, self.driver.find_element_by_xpath, '//div[@class="alert-message warning"]')

    def test_update_computer_name_to_empty(self):
        '''BB11: Test update after clearing (computer name)'''
        self.set_field('name', '')
        self.press_button(BUTTONS.save_this_computer)
        # Check for error
        error_field = self.driver.find_element_by_xpath('//div[@class="clearfix error"]')
        self.assertEqual(error_field.text, u'Computer name\nRequired')

    @parameterized.expand([('happy_path', 'My new computer'),
                           ('long', 'X'*1000),
                           ('number', 123456789.0),
                           ('special_chars', '+_=-)(*&^#@!~`{}[];\',.<>\/')])
    def test_update_computer_name(self, _, name):
        '''BB11: Test update (computer name) with different values'''
        self.set_field('name', name)
        self.press_button(BUTTONS.save_this_computer)
        self.assertEquals(
                self.driver.current_url, HOME_URL)
        alert = self.driver.find_element_by_xpath('//div[@class="alert-message warning"]')
        self.assertEqual(alert.text, u'Done! Computer %s has been updated' % name)
        self.computer_name = name

    @parameterized.expand([('empty', ''),
                           ('valid_format', '2015-11-05')])
    def test_update_introduced_date_happy_path(self, _, introduced_date):
        '''BB12: Test update (introduced_date) with different valid values'''
        self.set_fields([('name', COMPUTER_NAME),
                         ('introduced', introduced_date)])
        self.press_button(BUTTONS.save_this_computer)
        self.assertEquals(
                self.driver.current_url, HOME_URL)
        alert = self.driver.find_element_by_xpath('//div[@class="alert-message warning"]')
        self.assertEqual(alert.text, u'Done! Computer %s has been updated' % COMPUTER_NAME)

    @parameterized.expand([('text', 'text'),
                           ('number', 123456789.0),
                           ('wrong_format', '05-11-2015'),
                           ('zeros', '0000-00-00'),
                           ('wrong_delimiter', '2015_11_05'),
                           ('chars', 'aaaa-aa-aa')])
    def test_update_invalid_introduced_date(self, _, introduced_date):
        '''BB12: Test update (introduced_date) with different invalid values'''
        self.set_fields([('name', COMPUTER_NAME),
                         ('introduced', introduced_date)])
        self.press_button(BUTTONS.save_this_computer)
        # Check for error
        error_field = self.driver.find_element_by_xpath('//div[@class="clearfix error"]')
        self.assertEqual(error_field.text, u"Introduced date\nDate ('yyyy-MM-dd')")

    @parameterized.expand([('empty', ''),
                           ('valid_format', '2015-11-05')])
    def test_update_discontinued_date_happy_path(self, _, discontinued_date):
        '''BB13: Test update (discontinued_date) with different valid values'''
        self.set_fields([('name', COMPUTER_NAME),
                         ('introduced', '2014-11-05'),
                         ('discontinued', discontinued_date)])
        self.press_button(BUTTONS.save_this_computer)
        self.assertEquals(
                self.driver.current_url, HOME_URL)
        alert = self.driver.find_element_by_xpath('//div[@class="alert-message warning"]')
        self.assertEqual(alert.text, u'Done! Computer %s has been updated' % COMPUTER_NAME)

    @parameterized.expand([('text', 'text'),
                           ('number', 123456789.0),
                           ('wrong_format', '05-11-2015'),
                           ('zeros', '0000-00-00'),
                           ('wrong_delimiter', '2015_11_05'),
                           ('chars', 'aaaa-aa-aa')])
    def test_update_invalid_discontinued_date(self, _, discontinued_date):
        '''BB13: Test update (discontinued_date) with different invalid values'''
        self.set_fields([('name', COMPUTER_NAME),
                         ('introduced', '2014-11-05'),
                         ('discontinued', discontinued_date)])
        self.press_button(BUTTONS.save_this_computer)
        # Check for error
        error_field = self.driver.find_element_by_xpath('//div[@class="clearfix error"]')
        self.assertEqual(error_field.text, u"Discontinued date\nDate ('yyyy-MM-dd')")

    @parameterized.expand([('empty', '-- Choose a company--'),
                           ('valid', 'IBM')])
    def test_update_company(self, _, company):
        '''BB14: Test update (company) with different values'''
        self.set_fields([('name', COMPUTER_NAME),
                         ('introduced', '2014-11-05'),
                         ('discontinued', '2015-11-05'),
                         ('company', company)])
        self.press_button(BUTTONS.save_this_computer)
        self.assertEquals(
                self.driver.current_url, HOME_URL)
        alert = self.driver.find_element_by_xpath('//div[@class="alert-message warning"]')
        self.assertEqual(alert.text, u'Done! Computer %s has been updated' % COMPUTER_NAME)
