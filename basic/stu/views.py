from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
# Create your views here.
def hello(request):
    return HttpResponse('hello gopi')
def sample(request):
    return HttpResponse('congratulations')
def details(request):
    h={"name":'gopi','age':21,'address':'namasivaya puram'}
    return JsonResponse(h)
def details1(request):
    l=[1,2,3,4,5]
    return JsonResponse(l,safe=False)
