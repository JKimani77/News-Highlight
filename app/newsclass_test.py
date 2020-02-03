import unittest
from models import newsclass
News = newsclass.News

class NewsclassTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the News class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_news_created = News('cnn', 'CNN', 'business', 'stock trading stuff', 'tradeview','url','usa')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news_created,News))


if __name__ == '__main__':
    unittest.main()