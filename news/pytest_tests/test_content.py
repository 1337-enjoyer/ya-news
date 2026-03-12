from django.conf import settings
from django.urls import reverse

import pytest


def test_news_count(client, all_news):
    response = client.get(reverse('news:home'))
    object_list = response.context['object_list']
    news_count = object_list.count()
    assert news_count == settings.NEWS_COUNT_ON_HOME_PAGE