from django.conf.urls import patterns, url

from polls.views import IndexTemplateView

urlpatterns = patterns('',
    url(r'^$', IndexTemplateView.as_view()),
)