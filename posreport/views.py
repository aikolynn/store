#coding=utf-8
# from debug_toolbar.panels import logging
from django.db.models import *
from django.shortcuts import render,HttpResponseRedirect,redirect
from models import *
from django.core.urlresolvers import reverse
from django.core.paginator import *
import datetime
from forms import *
from django.contrib.auth  import login,logout,authenticate
from django.contrib import auth
# logger = logging.getLogger('posreport.views')
# Create your views here.
def index(request):
    store = Store.objects.all()
    classn=inventoryclass.objects.filter(depth=1)
    return render(request, 'templates/index.html', locals())

def flow(request):
    shop=Store.objects.all()
    cx_sd=request.GET.get('cx_sd')
    cx_ed=request.GET.get('cx_ed')
    cx_shop=request.GET.get('cx_shop')
    print cx_sd,cx_shop,cx_ed
    try:
        if cx_sd==None and cx_ed==None:
            print cx_ed,cx_sd,cx_shop
            #因数据最早从2006年开始，所以默认设置为2006-01-01
            cx_sd='2006-01-01'
            sd=datetime.datetime.strptime(cx_sd,'%Y-%m-%d')
            ed=datetime.datetime.now()
            #将结束时间转为文本格式，以便分页传参
            cx_ed=datetime.datetime.strftime(ed,'%Y-%m-%d')
            flow_list=OrderMain.objects.values('order_id','idstore__name','order_data','order_weekday','order_saleamount','idemployee__name').filter(order_data__range=(sd,ed))
            sum_orderid=OrderMain.objects.filter(order_data__range=(sd,ed)).aggregate(Count('order_id'))
            sum_amount=OrderMain.objects.filter(order_data__range=(sd,ed)).aggregate(Sum('order_saleamount'))
        elif  cx_sd!='' and cx_ed!='' and cx_shop=='所有':
            print 2
            sd=datetime.datetime.strptime(cx_sd,'%Y-%m-%d')
            ed=datetime.datetime.strptime(cx_ed,'%Y-%m-%d')
            flow_list=OrderMain.objects.values('order_id','idstore__name','order_data','order_weekday','order_saleamount','idemployee__name').filter(order_data__range=(sd,ed))
            sum_orderid=OrderMain.objects.filter(order_data__range=(sd,ed)).aggregate(Count('order_id'))
            sum_amount=OrderMain.objects.filter(order_data__range=(sd,ed)).aggregate(Sum('order_saleamount'))
        elif  cx_sd!='' and cx_ed=='' and cx_shop=='所有':
            print 10
            sd=datetime.datetime.strptime(cx_sd,'%Y-%m-%d')
            ed=datetime.datetime.strptime(cx_ed,'%Y-%m-%d')
            flow_list=OrderMain.objects.values('order_id','idstore__name','order_data','order_weekday','order_saleamount','idemployee__name').filter(order_data__range=(sd,ed))
            sum_orderid=OrderMain.objects.filter(order_data__range=(sd,ed)).aggregate(Count('order_id'))
            sum_amount=OrderMain.objects.filter(order_data__range=(sd,ed)).aggregate(Sum('order_saleamount'))
        else :
             print 1
             sd=datetime.datetime.strptime(cx_sd,'%Y-%m-%d')
             ed=datetime.datetime.strptime(cx_ed,'%Y-%m-%d')
             flow_list=OrderMain.objects.values('order_id','idstore__name','order_data','order_weekday','order_saleamount','idemployee__name').filter(order_data__range=(sd,ed),idstore__name=cx_shop)
             sum_orderid=OrderMain.objects.filter(order_data__range=(sd,ed),idstore__name=cx_shop).aggregate(Count('order_id'))
             sum_amount=OrderMain.objects.filter(order_data__range=(sd,ed),idstore__name=cx_shop).aggregate(Sum('order_saleamount'))
    except:
        pass
    flow_pagelist=Paginator(flow_list,100,)
    try:
        page=int(request.GET.get('page',1))
        flow_list=flow_pagelist.page(page)
    except:
        flow_list=flow_pagelist.page(1)
    return render(request,'templates/flow.html',locals())
#用户登录
def do_login(request):
    try:
        if request.method=="POST":
            Login_form=login_form(request.POST)
            if Login_form.is_valid():
                username=Login_form.cleaned_data["username"]
                password=Login_form.cleaned_data["password"]
                user=auth.authenticate(username=username,password=password)
                if user is not None:
                    user.backend = 'django.contrib.auth.backends.ModelBackend'
                    login(request,user)
                else:
                    return HttpResponseRedirect("/do_login/")
                return HttpResponseRedirect("/flow/")
            else:
                 return redirect(reverse('posreport.views.do_login'))
        else:
            Login_form=login_form()
    except Exception as e:
        # logger.error(e)
        pass
    return render(request,'templates/login.html',locals())
