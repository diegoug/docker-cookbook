# -*- coding: utf-8 -*-
from django.conf import settings

class SocketMiddleware(object):
    def process_request(self, request):

        request.socketio = settings.SOCKETIO_PORT
        return
