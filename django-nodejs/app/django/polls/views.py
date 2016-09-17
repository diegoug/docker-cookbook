import os
import json
import redis as Redis

from django.views.generic import TemplateView
from django.utils.crypto import get_random_string

redis = Redis.StrictRedis(host=os.environ.get('REDIS_HOST', ''), password='', port=os.environ.get('REDIS_PORT', ''), db=1)


class IndexTemplateView(TemplateView):
    template_name = 'base.html'

    def get_context_data(self, **kwargs):
        context = super(IndexTemplateView, self).get_context_data(**kwargs)

        self.set_access_token()

        data = {
            'title': 'Connect nodejs with your app'
        }

        context.update(data)
        return context

    def set_access_token(self):
        self.token = get_random_string(32)
        key = 'session:%s' % str(self.token)
        data = {
            'user': 'diegoug'
        }
        value = json.dumps(data)
        redis.setex(key, 86400, value)

    def render_to_response(self, context, **response_kwargs):
        response = super(IndexTemplateView, self).render_to_response(context, **response_kwargs)
        response.set_cookie(key='nodejskey', value=self.token, max_age=86400, domain='127.0.0.1', secure=None)
        return response
