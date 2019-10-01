import unittest
from app.models import comment 
comment =comment

class commentTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the coomment class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_comment = comment()

    