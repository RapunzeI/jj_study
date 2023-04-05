from django.shortcuts import render, HttpResponse

def default(req):
    return HttpResponse("<h1>공백<h1>")

def index(req):
    return HttpResponse('Welcome!')

def create(req):
    return HttpResponse("Create")

def read(req):
    return HttpResponse("read")