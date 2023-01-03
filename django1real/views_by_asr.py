from django.http import HttpResponse



def index(request):
    return HttpResponse("hrllo world, This is our fist project not a app")
