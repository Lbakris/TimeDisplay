from django.shortcuts import render, HttpResponse
from datetime import datetime
def timedisplay(request):
    context = {
    "date": datetime.now(),
    "someKey":"somevalue"
    }
    return render(request, 'timedisplay/page.html',context)
