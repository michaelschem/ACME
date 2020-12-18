from django.http import HttpResponse


def index(request):
    return HttpResponse('<h1>Welcome to ACME Quotes</h1><ul><li><a href="admin/">Admin Portal</a></li><li><a href="api/">API</a></li></ul>')
