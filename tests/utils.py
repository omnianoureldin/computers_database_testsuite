from selenium import webdriver
from unittest import TestCase

from constants import *


class BasicTest(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()

    @classmethod
    def tearDownClass(cls):
        if cls.driver:
            cls.driver.quit()

    def setUp(self):
        self.driver.get(HOME_URL)

    def set_field(self, field_id, value):
        '''
        Utility method to set a value for a specific field

        :param field_id: id of the field to be filled
        :param value: value to be set in the field
        '''
        field = self.driver.find_element_by_id(field_id)
        if field.tag_name != 'select':  # Dropdowns can't be cleared as it not user-editable
            field.clear()
        field.send_keys(value)

    def set_fields(self, field_value_list):
        '''
        Utility method to set multiple fields with different values

        :param field_value_list: list of tuples (field_id, value)
        '''
        for (field, value) in field_value_list:
            self.set_field(field, value)

    def press_button(self, button):
        '''
        Utility method to perform click action on a specific button

        :param button: tuple (find_element_by, value_of_by_attribute)
        '''
        btn = self.driver.find_element(button[0], button[1])
        btn.click()

    def load_computer(self, name):
        '''
        Utility method to simulate opening computer link

        :param name: computer name
        '''
        search_name = str(name)
        if len(search_name) > 20:
            search_name = search_name[:20]
        self.driver.get(HOME_URL)
        self.set_field('searchbox', search_name)
        self.driver.find_element_by_id('searchbox').submit()
        link = self.driver.find_element_by_partial_link_text(search_name)
        self.driver.get(link.get_attribute('href'))

    def delete_computer(self, name):
        '''
        Utility method to delete computer through UI, used mainly for cleaning up in tearing down

        :param name: computer name
        '''
        self.load_computer(name)
        self.press_button(BUTTONS.delete_this_computer)

    def verify_fields_text(self, field_value_list):
        '''
        Utility method to verify that field(s) are populated with the expected value

        :param field_value_list: list of tuples (field_id, expected_value)
        '''
        for (field_id, expected_value) in field_value_list:
            field = self.driver.find_element_by_id(field_id)
            if field.tag_name == 'select':
                self.assertEqual(
                        field.find_element_by_xpath('//option[@selected=""]').text, expected_value)
            else:
                self.assertEqual(field.get_attribute('value'), expected_value)
