from django.conf.urls import url
from about.views import AboutListView

app_name = 'about'
urlpatterns = [
    url(r'^$', AboutListView.as_view(), name='about_index')
]

