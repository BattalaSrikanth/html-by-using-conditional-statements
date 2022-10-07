from django.shortcuts import render

# Create your views here.
def srikanth1(request):
    d={'a':5,'b':20,'c':30}
    return render(request,'conditional.html',d)
