from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. This is the index view of Demoapp.")

def home(request):
    path = request.path
    address = request.META['REMOTE_ADDR']
    scheme = request.scheme
    method = request.method
    user_agent = request.META['HTTP_USER_AGENT']
    path_info = request.path_info

    response = HttpResponse()
    response.headers["Age"] = 20

    msg = f"""<br>
        <br>Path: {path}
        <br>Scheme: {scheme}
        <br>Method: {method}
        <br>User agent: {user_agent}
        <br>Path info: {path_info}
        <br>Response header: {response.headers}
    """

    return HttpResponse(msg, content_type=' text/html', charset='utf-8')

