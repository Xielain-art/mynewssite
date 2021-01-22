from django.conf.urls import url
from .views import ViewNews, CreateNews, HomeNews, NewsByCategory, test

urlpatterns = [
    url(r'^$', HomeNews.as_view(), name='index'),
    url(r'^category/(?P<category_id>\d+)$', NewsByCategory.as_view(), name='category'),
    url(r'^news/(?P<pk>\d+)$', ViewNews.as_view(), name='view_news'),
    url(r'^news/add-news/$', CreateNews.as_view(), name='add_news'),
    url(r'news/test/', test, name='test'),

]
