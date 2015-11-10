from nose_parameterized import parameterized
from selenium.common.exceptions import NoSuchElementException

from constants import *
from utils import BasicTest


class TestCreate(BasicTest):
    def setUp(self):
        super(TestCreate, self).setUp()
        self.created_computers = list()
        self.press_button(BUTTONS.add_a_new_computer)
        self.assertEquals(
                self.driver.current_url, NEW_COMPUTER_URL)

    def tearDown(self):
        for computer in self.created_computers:
            self.delete_computer(computer)
        super(TestCreate, self).tearDown()

    def test_create_empty_computer(self):
        '''BB1: Test create new computer with all fields empty'''
        self.press_button(BUTTONS.create_this_computer)
        # Check for error
        error_field = self.driver.find_element_by_xpath('//div[@class="clearfix error"]')
        self.assertEqual(error_field.text, u'Computer name\nRequired')

    def test_cancel_create(self):
        '''BB2: Test cancel create new computer with all fields empty'''
        self.press_button(BUTTONS.cancel)
        self.assertEquals(
                self.driver.current_url, HOME_URL)
        self.assertRaises(
                NoSuchElementException, self.driver.find_element_by_xpath, '//div[@class="alert-message warning"]')

    @parameterized.expand([('valid', 'valid computer', '2014-11-05', '2015-11-05', 'IBM'),
                           ('invalid', '', '05-11-2014', 'date', 'IBM')])
    def test_cancel_create_with_data(self, _, name, introduced_date, discontinued_date, company):
        '''BB3: Test cancel create new computer with all fields populated with valid/invalid data'''
        self.set_fields([('name', name),
                         ('introduced', introduced_date),
                         ('discontinued', discontinued_date),
                         ('company', company)])
        self.press_button(BUTTONS.cancel)
        self.assertEquals(
                self.driver.current_url, HOME_URL)
        self.assertRaises(
                NoSuchElementException, self.driver.find_element_by_xpath, '//div[@class="alert-message warning"]')

    @parameterized.expand([('happy_path', 'My new computer'),
                           ('long', 'X'*1000),
                           ('number', 123456789.0),
                           ('special_chars', '+_=-)(*&^#@!~`{}[];\',.<>\/')])
    def test_create_field_computer_name(self, _, name):
        '''BB4: Test create new computer with different (computer name) values'''
        self.set_field('name', name)
        self.press_button(BUTTONS.create_this_computer)
        self.assertEquals(
                self.driver.current_url, HOME_URL)
        alert = self.driver.find_element_by_xpath('//div[@class="alert-message warning"]')
        self.assertEqual(alert.text, u'Done! Computer %s has been created' % name)
        self.created_computers.append(name)

    def test_create_field_introduced_date_happy_path(self):
        '''BB5: Test create new computer with valid (introduced date)'''
        self.set_fields([('name', 'My computer'),
                         ('introduced', '2015-11-05')])
        self.press_button(BUTTONS.create_this_computer)
        self.assertEquals(
                self.driver.current_url, HOME_URL)
        alert = self.driver.find_element_by_xpath('//div[@class="alert-message warning"]')
        self.assertEqual(alert.text, u'Done! Computer My computer has been created')
        self.created_computers.append('My computer')

    @parameterized.expand([('text', 'text'),
                           ('number', 123456789.0),
                           ('wrong_format', '05-11-2015'),
                           ('zeros', '0000-00-00'),
                           ('wrong_delimiter', '2015_11_05'),
                           ('chars', 'aaaa-aa-aa')])
    def test_create_field_invalid_introduced_date(self, _, introduced_date):
        '''BB5: Test create new computer with different invalid (introduced date) values'''
        self.set_fields([('name', 'My computer'),
                         ('introduced', introduced_date)])
        self.press_button(BUTTONS.create_this_computer)
        # Check for error
        error_field = self.driver.find_element_by_xpath('//div[@class="clearfix error"]')
        self.assertEqual(error_field.text, u"Introduced date\nDate ('yyyy-MM-dd')")

    def test_create_field_discontinued_date_happy_path(self):
        '''BB6: Test create new computer with valid (discontinued date)'''
        self.set_fields([('name', 'My computer'),
                         ('introduced', '2014-11-05'),
                         ('discontinued', '2015-11-05')])
        self.press_button(BUTTONS.create_this_computer)
        self.assertEquals(
                self.driver.current_url, HOME_URL)
        alert = self.driver.find_element_by_xpath('//div[@class="alert-message warning"]')
        self.assertEqual(alert.text, u'Done! Computer My computer has been created')
        self.created_computers.append('My computer')

    @parameterized.expand([('text', 'text'),
                           ('number', 123456789.0),
                           ('wrong_format', '05-11-2015'),
                           ('zeros', '0000-00-00'),
                           ('wrong_delimiter', '2015_11_05'),
                           ('chars', 'aaaa-aa-aa')])
    def test_create_field_invalid_discontinued_date(self, _, discontinued_date):
        '''BB6: Test create new computer with different invalid (discontinued date) values'''
        self.set_fields([('name', 'My computer'),
                         ('introduced', '2014-11-05'),
                         ('discontinued', discontinued_date)])
        self.press_button(BUTTONS.create_this_computer)
        # Check for error
        error_field = self.driver.find_element_by_xpath('//div[@class="clearfix error"]')
        self.assertEqual(error_field.text, u"Discontinued date\nDate ('yyyy-MM-dd')")

    def test_create_field_company(self):
        '''BB7: Test create new computer with valid (company)'''
        self.set_fields([('name', 'My computer'),
                         ('introduced', '2014-11-05'),
                         ('discontinued', '2015-11-05'),
                         ('company', 'Apple Inc.')])
        self.press_button(BUTTONS.create_this_computer)
        self.assertEquals(
                self.driver.current_url, HOME_URL)
        alert = self.driver.find_element_by_xpath('//div[@class="alert-message warning"]')
        self.assertEqual(alert.text, u'Done! Computer My computer has been created')
        self.created_computers.append('My computer')
