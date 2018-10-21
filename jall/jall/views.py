from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You are in the root")