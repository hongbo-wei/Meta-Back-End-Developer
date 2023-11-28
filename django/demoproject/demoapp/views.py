from django.shortcuts import render
from django.http import HttpResponse
from .forms import BookingForm

# Create your views here.
# def index(request):
#     return HttpResponse("Hello, world. This is the index view of Demoapp.")

def index(request): 
    context={'user':'admin',
             'profession':'Teacher'
            } 
    langs = ['Python', 'Java', 'PHP', 'Ruby', 'Rust']
    dct = {'digits': ['One', 'Two', 'Three'],'tens': ['Ten', 'Twenty', 'Thirty']} 
    amt = 100
    return render(request, 'index.html', context={'context': context,
                                                  'langs': langs,
                                                  'dct': dct,
                                                  'amt': amt,
                                                  }) 

def form_view(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {"form" : form}
    return render(request, "booking.html", context)

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

# Path parameter
# http://127.0.0.1:8000/getuser/John/1
def pathview(request, name, id): 
    return HttpResponse("Name: {} UserID: {}".format(name, id))

# Query parameter
# http://127.0.0.1:8000/getuser/?name=John&id=1
def qryview(request): 
    name = request.GET['name'] 
    id = request.GET['id'] 
    return HttpResponse("Name:{} UserID:{}".format(name, id)) 

# Body parameter
def showform(request): 
    return render(request, "form.html") 

def getform(request): 
    if request.method == "POST":
        id=request.POST['id']
        name=request.POST['name']
    return HttpResponse("Name: {} UserID: {}".format(name, id))