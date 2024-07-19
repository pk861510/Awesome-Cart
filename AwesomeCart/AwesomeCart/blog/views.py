from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse('Blog home of prince kumar')
    return render(request,'blog/index.html')