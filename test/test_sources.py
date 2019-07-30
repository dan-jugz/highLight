import unittest
from app.models import Source


class SourcesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Sources Class
    '''

    def setUp(self):

        self.new_source=Source('123movies','123 Movies','lorem picsum','https://blahblahblah','madtings','patois','jm')


    def test_instance(self):

        self.assertTrue(isinstance(self.new_source,Source))

if __name__=='__main__':
    unittest.main()