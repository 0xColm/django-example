import datetime
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.template import loader
from polls.form import EmpForm

def index(request):
    now = datetime.datetime.now()
    html = "<html><body><h3>Now time is %s.</h3></body></html>"% now
    return HttpResponse(html)

@require_http_methods(["GET"])
def show(request):
    return HttpResponse("<h1>This is Http GET request.</h1>")

def template(request):
    return render(request, 'index.html')

def form(request):
    stu = EmpForm()
    return render(request, "form.html", {'form':stu})