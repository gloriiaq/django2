from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home2.html',{"info":"my name is Gloria and I am 13 years old,})
