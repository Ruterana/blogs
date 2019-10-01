import unittest
from app.models import quote
quote= quote

class blogTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the quote class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_quote = quote()