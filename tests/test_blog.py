import unittest
from app.models import blog 
 blog = blog

class blogTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the blog class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_pitch = Pitch()

    # def test_instance(self):
    #     self.assertTrue(isinstance(self.new_pitch,Pitch))