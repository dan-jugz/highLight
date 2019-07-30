import unittest
from models import article

Article =article.Article


class ArticlesTest(unittest.TestCase):
    '''
    Test class to test the behaviour of the Articles Class
    '''

    def setUp(self):
        '''
        Set up method that will run before evert test
        '''

        self.new_article=Article('Josephus Miller',"Protomolecule",'Not a life-form in itself,a set of free-floating instructions designed to adapt to and guide other replicating systems','https://expanse.fandom.com/wiki/Protomolecule','https://vignette.wikia.nocookie.net/expanse/images/c/c6/Protomolecule_structure_on_Venus.jpg/revision/latest/scale-to-width-down/350?cb=20190624204215')

        def test_instance(self):
            self.assertTrue(isinstance(self.new_article,Article))

if __name__=='__main__':
    unittest.main()  