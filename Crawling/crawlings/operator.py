from apscheduler.schedulers.background import BackgroundScheduler
from .views import naver_news_crawlling
from .views import tistory_review_crawling


def start():
    scheduler=BackgroundScheduler()

    @scheduler.scheduled_job('cron', hour=16, minute=34, id = 'crawling')
    def auto_check():
        naver_news_crawlling()
        tistory_review_crawling()
        
        
    scheduler.start()