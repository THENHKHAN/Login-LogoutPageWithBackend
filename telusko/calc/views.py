from django.shortcuts import render

# Create your views here.

# from django.http import HttpRequest

from django.http import HttpResponse

def  home ( request) : # when user request for home then what will display We'll put here.

    # return HttpResponse( " <h1> Hello home page! </h1>")
    return render(request, 'index.html' ,{'first_name': 'John', 'last_name': 'Doe'})
'''
Http Methods: get , post , update,delete etc . We'll see only two here. GET and POST.

POST: when you POST data from Client(frontend) To Server(Backend).
GET: when you get/fetching data from Server(Backend) to Client(frontend).
'''

def  add ( request) :
    # result = int( request.GET["num1"]) +int( request.GET["num2"]) # U can't write [num2] show error/]..... Above also work for get. but for Security USE POST.
        result = int( request.POST["num1"]) +int( request.POST["num2"]) # U can't write [num2] show error

        return render(request , 'result.html' , {'result' : result})

