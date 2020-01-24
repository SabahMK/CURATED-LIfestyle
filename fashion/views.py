from django.shortcuts import render
from .models import Fashion, Message

# Create your views here.
def home(request):
    caption = Fashion.objects.all()
    context = {
        "caption" : caption
    }
    return render(request,'main/index.html', context)

def content(request):
    fashions = Message.objects.all()
    context = {
        "fashions" : fashions

    }
    return render(request, 'main/content.html',context )