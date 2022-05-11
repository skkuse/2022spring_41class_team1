from django.shortcuts import render, redirect, HttpResponse
from .models import User
from django.contrib.auth.hashers import make_password, check_password
# Create your views here.

def home(request):
    user_pk = request.session.get('sid')
    
    if user_pk:
        user = User.objects.get(pk=user_pk)
        return HttpResponse(user.username)

    return HttpResponse('로그인 성공')

def theory(request):
    return render(request, 'theory.html')

def code_test(request):
    return render(request, 'code_test.html')

def login(request):
    if request.method=="GET":
        return render(request,'login.html')
    elif request.method=="POST":

        username = request.POST.get('username')
        password = request.POST.get('password')

        res_data = {}
        user = User.objects.get(username = username)

        if check_password(password,user.password):
            request.session['sid']=user.id
            return redirect('/')
        else:
            res_data['error'] = "비밀번호가 틀렸습니다"
        return render(request,'login.html',res_data)

def logout(request):
    if request.session['sid']:
        del(request.session['sid'])
    return rediret('/')


def register(request):
    if request.method == "GET":
        return render(request, 'register.html')
    elif request.method == "POST":
        #이미 있는 계정 등 예외처리
        username = request.POST['username']
        password = request.POST['password']
        repassword = request.POST['re-password']

        if password != repassword:
            return HttpResponse("비밀번호 다름")


        user = User(username = username, password = make_password(password))

        user.save()

        return render(request, 'register.html')
