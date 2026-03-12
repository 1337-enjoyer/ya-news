from django.conf import settings
from django.test.client import Client

import pytest

from datetime import datetime, timedelta

from news.models import Comment, News


@pytest.fixture
def comment_author(django_user_model):
    return django_user_model.objects.create(username='Comment autor')


@pytest.fixture
def comment_not_author(django_user_model):
    return django_user_model.objects.create(username='Comment not autor')


@pytest.fixture
def author_client(comment_author):
    client = Client()
    client.force_login(comment_author)
    return client


@pytest.fixture
def not_author_client(comment_not_author):
    client = Client()
    client.force_login(comment_not_author)
    return client


@pytest.fixture
def news():
    news = News.objects.create(
        title='Заголовок',
        text='Текст новости',
    )
    return news


@pytest.fixture
def comment(news, comment_author):
    comment = Comment.objects.create(
        news=news,
        author=comment_author,
        text='LOL'
    )
    return comment


@pytest.fixture
def all_news(db):
    today = datetime.today()
    all_news = [
        News(
            title=f'Новость {index}',
            text='Просто текст.',
            date=today - timedelta(days=index)
        )
        for index in range(settings.NEWS_COUNT_ON_HOME_PAGE + 1)
    ]
    News.objects.bulk_create(all_news)
    return News.objects.all()