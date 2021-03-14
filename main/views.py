from django.shortcuts import render, redirect
from .models import TextSnippet, SecretKey
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.models import  auth, Group
from django.contrib import messages
# Create your views here.

def main(request):
    user = request.user
    # url =  request.GET.get('url')
    # text = request.GET.get('text')
    # if url is None and text is None:
    return render(request, 'index.html', {'user':user})
    # else:
    #     return render(request, 'index.html', {'url':url, 'text':text})


def generate_url(request):
    if request.user.is_authenticated:
        text = request.POST['textmessage']
        var = TextSnippet.objects.create(text=text)
        uuid = var.uuid
        secret = SecretKey.objects.create(text_id=var)
        secretkey = secret.id
        url = 'http://localhost:8000/viewpage/?uuid='+str(uuid)+'&secretkey='
        return render(request, 'index.html', {'url':url, 'text':text, 'secretkey':secretkey})
    else:
        return redirect('login')

def viewpage(request):
    if request.user.is_authenticated:
        uuid = request.GET.get('uuid')
        secretkey = request.GET.get('secretkey')
        # print(uuid, secretkey)
        try:
            var = TextSnippet.objects.filter(uuid=uuid)
            var2 = SecretKey.objects.filter(text_id=secretkey)

            if var is not None and var2 is not None:
                text = var[0].text
                return render(request, 'viewpage.html', {'text':text})
        except Exception as e:
            return render(request, 'invalid.html')

    return redirect('login')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        # print(type(user))
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
