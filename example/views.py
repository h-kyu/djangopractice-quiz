from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# Create your views here.

def index(request):
    return render(request, 'example/index.html')

def infoForm(request):
    return render(request, 'example/infoForm.html')
    # if request.method == 'GET':
    #     return render(request, 'example/infoForm.html')
    # elif request.method == 'POST':
    #     return HttpResponse('example/infoResult.html')
        
def infoResult(request):   
    id = request.POST['id']
    pw = request.POST['pw']
    msg = request.POST['message']
    context = {'id':id, 'pw':pw, 'msg':msg}
    
    return render(request, 'example/infoResult.html', context)

def selectForm(request):
    if request.method == 'GET':
        return render(request, 'example/selectForm.html')
    elif request.method == 'POST':
        return HttpResponse('example/selectResult.html')
    
def selectResult(request):
    skl = request.POST['school']
    country = request.POST['country']
    inter = request.POST['inter']
    context = {'학교':skl, '국가':country, '관심':inter}
    
    return render(request, 'example/selectResult.html', context)


def comboForm(request):
    if request.method == 'POST':
        potal = request.POST['potal']    
        return HttpResponseRedirect(potal) # 여기로 다시 요청
    else:
        return render(request, 'example/comboForm.html')
    
def forForm(request):
    return render(request, 'example/forForm.html')

def forResult(request):
    number = request.POST['number']
    sum=0
    for i in range(1, int(number)+1):
        sum+=i
    context = {
        'number':number,
        'sum':sum
    }              
    return render(request, 'example/forResult.html', context)

def lottoForm(request):
    return render(request, 'example/lottoForm.html')

import random

def lottoResult(request):
    lotto = int(request.POST['lotto'])
    lottonum=random.randint(1,45)
    lotto_lst=[]
    for i in range(lotto):
        lot=[]
        for j in range(6):
            while lottonum in lot:
                lottonum=random.randint(1,45)
            lot.append(lottonum)
        lotto_lst.append(lot)
    context={
        'lotto':lotto_lst
    }
        
    
    return render(request, 'example/lottoResult.html', context)
