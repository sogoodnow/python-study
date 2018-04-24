import re
from django.shortcuts  import render,redirect,HttpResponse,reverse
class ShopMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response
        print("init.........")
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        urllist = ['/myadmin/login','/myadmin/dologin','/myadmin/logout']

        print("call........."+request.path)
        path =request.path
        if re.match('/myadmin',path) and (path not in urllist):
            if "adminuser" not in request.session:
                return redirect(reverse("myadmin_login"))
        # Code to be executed for each request/response after
        # the view is called.
        response = self.get_response(request)
        return response