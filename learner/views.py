from django.shortcuts import render, redirect, HttpResponse
from django.http import HttpResponseBadRequest
from .models import User, Problem
from django.contrib.auth.hashers import make_password, check_password
import json
import sys, os
import subprocess
# Create your views here.



def index(request):
    if 'sid' in request.session:
        return render(request, 'pages/homepage.html')
    else:
        return render(request, 'index.html')

def home(request):
    if 'sid' in request.session:
        return render(request, 'pages/homepage.html')
    else:
        return redirect('/')

def profile(request):
    if 'sid' in request.session:
        return render(request, 'pages/profile.html')
    else:
        return redirect('/')

def class_start(request):
    if 'sid' in request.session:
        return render(request, 'classes/class_start.html')
    else:
        return redirect('/')

def step(request,page,name):
    if 'sid' in request.session:
        progress = request.session['progress']
        path = 'classes/step'+str(page)+'/'+name+'.html'
        return render(request, path)
    else:
        return redirect('/')

    
def signUp(request):
    if request.method == "GET":
        return render(request, 'pages/signUp.html')
    elif request.method == "POST":
        #이미 있는 계정 등 예외처리
        useremail = request.POST['email']
        username = request.POST['name']
        password = request.POST['loginPw']
        if not User.objects.filter(useremail = useremail):
            user = User(useremail = useremail, username = username, password = make_password(password))
            user.save()
            request.session['sid']=User.objects.filter(useremail = useremail)
            request.session['email']=useremail
            request.session['name']=username
            request.session['progress']=user.progress
        return render(request, 'pages/homepage.html')


def login(request):
    if request.method=="POST":
        useremail = request.POST.get('email')
        password = request.POST.get('loginPw')

        res_data = {}
        
        if User.objects.filter(useremail = useremail):
            user = User.objects.get(useremail = useremail)
            if check_password(password,user.password):
                request.session['sid']=user.id
                request.session['email']=user.useremail
                request.session['name']=user.username
                request.session['progress']=user.progress
                return redirect('classes/main/homepage')
            else:
                res_data['error'] = "비밀번호가 틀렸습니다"
        else:
            res_data['error'] = "존재하지 않는 이메일주소입니다"
        return render(request,'index.html',res_data)
    return HttpResponseBadRequest('인가되지 않은 접근')

def change_pass(request):
    res_data = {}
    if request.method=="POST":
        new_pass = request.POST['new_pass']
        if 'sid' in request.session:
            if User.objects.filter(pk = request.session.id):
                user = User.objects.filter(pk = request.session.id)
                user.update(password=new_pass)
                return redirect('/')

    return HttpResponseBadRequest('인가되지 않은 접근')


def logout(request):
    if 'sid' in request.session:
        User.objects.filter(pk=request.session['sid']).update(progress=request.session['progress'])
        del(request.session['sid'])
        request.session.flush()
    return redirect('/') 

def duplication_check(request):
    userEmail = request.POST.get('userEmail')
    result = not User.objects.filter(username=userEmail).exists()
    return HttpResponse(json.dumps({'result' : result}), content_type='application/json')


def judge(request):
    if request.method == "POST":
        pno = request.POST['pno']
        code = request.POST['code']
        success = False

        #subprocess run
        p = subprocess.Popen(['python3', os.path.dirname(__file__)+'/judge/'+pno+'.py',code], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = p.communicate()
        err_str = err.decode('utf-8').split("\n")
        err_decode = '\n'.join(err_str[3:-1])
        print(err)
        if p.returncode == 0:
            success = True

        request.session['progress'] += 1
        return HttpResponse(json.dumps({'success' : success, 'out' : out.decode('utf-8')[:-1],'log': err_decode }), content_type='application/json')
    return HttpResponseBadRequest('인가되지 않은 접근')


def quiz(request):
    if request.method == "POST":
        qno = request.POST['qno']
        i = 1
        ans = []
        while 'q'+str(i) in request.POST:
            ans.append(request.POST['q'+str(i)])
            i = i+1
        path = os.path.dirname(__file__)+"/quiz/"+str(qno)+".txt"
        
        success = True
        
        with open(path,'r') as file:
            data = file.read().split('\n')
            for a,b in zip(ans,data):
                if a != b:
                    success = False
                    break
        
        request.session['progress'] += 1
        return HttpResponse(json.dumps({'success' : success}),  content_type='application/json')
    return HttpResponseBadRequest('인가되지 않은 접근')

