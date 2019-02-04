from django.http import HttpResponse
from django.shortcuts import render


def main(request):
    return render(request, 'index.html', {})

def baqi(request):
    return HttpResponse("i'm not 87, you 87!")
