from django.conf.urls import url

from polls.views import IndexTemplateView

urlpatterns = [
    url(r'^$', IndexTemplateView.as_view()),
]