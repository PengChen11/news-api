from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import News
# Create your tests here.

class NewsTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(username = 'tester1', password='test123456')
        testuser1.save()

        test_news = News.objects.create(
            title = 'WWDC 2020: What To Expect From Today’s Epic Apple Updates For iPhone, iPad & Apple Watch',
            source = 'Forbes',
            date = '2020-06-22',
            url = 'https://www.forbes.com/sites/davidphelan/2020/06/22/wwdc-2020-what-to-expect-from-todays-epic-apple-updates-for-iphone-ipad--apple-watch/',
            user = testuser1
        )
        test_news.save()


    def test_news_content(self):
        news = News.objects.get(id=1)
        actural_title = str(news.title)
        acutral_source = str(news.source)
        actural_date = str(news.date)
        acutral_url = str(news.url)
        actural_user = str(news.user)

        self.assertEqual(actural_title, 'WWDC 2020: What To Expect From Today’s Epic Apple Updates For iPhone, iPad & Apple Watch')
        self.assertEqual(acutral_source, 'Forbes')
        self.assertEqual(actural_date, '2020-06-22')
        self.assertEqual(acutral_url, 'https://www.forbes.com/sites/davidphelan/2020/06/22/wwdc-2020-what-to-expect-from-todays-epic-apple-updates-for-iphone-ipad--apple-watch/')
        self.assertEqual(actural_user, 'tester1')
