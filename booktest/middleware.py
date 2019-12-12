from django.http import HttpResponse

class BlockeSMiddleware(object):
    '''中间件类'''
    EXCLUDE_IPS = ['192.168.223.2']
    def process_view(self, request, view_func, *view_args, **view_kwargs):
        '''视图函数调用之前会被调用'''
        user_ip = request.META['REMOTE_ADDR']
        if user_ip in BlockeSMiddleware.EXCLUDE_IPS:
            return HttpResponse('<h1>Forbidden</h1>')