from selenium.webdriver.common.by import By


def enum(**enums):
    return type('Enum', (), enums)

BUTTONS = enum(add_a_new_computer=(By.ID, 'add'),
               create_this_computer=(By.XPATH, '//input[@value="Create this computer"]'),
               save_this_computer=(By.XPATH, '//input[@value="Save this computer"]'),
               delete_this_computer=(By.XPATH, '//input[@value="Delete this computer"]'),
               cancel=(By.LINK_TEXT, 'Cancel'))
COMPUTER_NAME = 'My computer'
HOME_URL = 'http://computer-database.herokuapp.com/computers'
NEW_COMPUTER_URL = 'http://computer-database.herokuapp.com/computers/new'
