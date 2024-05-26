from django.shortcuts import render,redirect
from .models import *
from .forms import *


# Create your views here.
def index(req):
    # telegram()
    return render(req,'index.html')
######################################################
def kabinet(req):

    user = req.user
    items = Order.objects.filter(user=user)
    data = {'items':items}
    return render(req,'kabinet.html',data)
######################################################
def goods(req,cat):
    items = Tovar.objects.filter(category=cat)
    print(items)
    data={'items':items,'cat':cat}
    return render(req, 'goods.html',data)

def buy(req,itemid,cat):
    item = Tovar.objects.get(id=itemid)
    print(item)
    userid = req.user.id
    if Cart.objects.filter(user_id=userid, tovar_id=itemid):
        item = Cart.objects.get(tovar_id=itemid)
        item.count+=1
        item.summa = item.calcSumma()
        item.save()
    else:
        Cart.objects.create(count=1, tovar_id=itemid,
                            user_id=userid,
                            summa=item.price)
    return redirect('goods',cat)

def cart(req):
    forma = FormOrder()
    mycart = Cart.objects.filter(user_id=req.user.id)
    print(mycart.values_list())
    q=list()
    for i in mycart:
        item=i.tovar
        q.append(item)
    print(q)

    total =0
    sps = ''
    for one in mycart:
        total+=one.summa

    if req.POST:
        print(1)
        forma=FormOrder(req.POST)
        if forma.is_valid():
            print('ok')
            k1 = forma.cleaned_data.get('city')
            k2 = forma.cleaned_data.get('street')
            k3 = forma.cleaned_data.get('house')
            k4 = forma.cleaned_data.get('tel')
            print(k1,k2,k3,k4)
            zakaz=''
            for one in mycart:
                zakaz+=(one.tovar.name+' '+str(one.count)+
                        ' '+str(one.summa)+'\n')
            zakaz+='Всего: '+str(total)+'\n'
            zakaz+='Адрес ' + k1 +' '+ k2 +' '+ k3 +'\n'
            zakaz+='Телефон' + k4
            curOrder=Order.objects.create(adres=k1 +' '+' '+ k2 +' '+ k3,tel=k4,zakaz=zakaz,
                                 status='в сборке',user=req.user,
                                 total=total)

            for one in mycart:
                print(one.tovar)
                print(curOrder)
                curOrder.items.add(one.tovar)
            curOrder.save()

            mycart.delete()
            total=0
            forma=FormOrder()
            sps = 'Спасибо за заказ'
            telegram(zakaz)
    data = {'items':mycart,'total':total,
            'formaorder':forma, 'sps':sps}

    return render(req,'cart.html',data)

def delete(req,itemid):
    item =Cart.objects.get(id=itemid)
    item.delete()
    return redirect('cart')

def edit(req,itemid,num):
    num=int(num)
    item = Cart.objects.get(id=itemid)
    item.count+=num
    item.summa = item.calcSumma()
    if  item.count>0:
        item.save()
    return redirect('cart')



from django.contrib.auth.forms import UserCreationForm
from .forms import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
def registr(req):
    forma = UserCreationForm()
    print(1)
    if req.POST:
        print(2)
        forma = formRegistr(req.POST)#Форма регистрации проверка
        if forma.is_valid():#проверка пройдена
            print(3)

            #Собираем данные
            k1 = forma.cleaned_data.get('username')
            k2 = forma.cleaned_data.get('password1')
            k3 = forma.cleaned_data.get('email')
            k4 = forma.cleaned_data.get('first_name')
            k5 = forma.cleaned_data.get('last_name')
            User.objects.create_user(username=k1,password=k2)#новая строка в таблице
            user = User.objects.get(username=k1)#находим пользователя
            # заполняем данные
            user.email = k3
            user.last_name = k5
            user.first_name = k4
            user.save()#сохраняем
            # # modelProfile.objects.create(balance=1000,podpiska_id=1,user_id=user.id)
            login(req,user)#Вход пользователя на сайт
            return redirect('home')#на главную стр. перемещаемся
        else:
            forma = formRegistr()#форма регистрации
            data = {'form':forma}
            return render(req,'registration/registration.html',data)

# def profile(req):
#
#
#     return render(req,'kabinet.html')

def telegram(message):
    token = '6647043691:AAHTEq8ajZMPoNxhBDk_42QzOTMtSWa-Ngg'
    chat = 1153573167
    import telebot
    #
    bot = telebot.TeleBot(token)#Подкл.к Боту
    bot.send_message(chat, message)

def myzakaz(req,itemid):
    item = Order.objects.get(id=itemid)
    data = {'item':item}
    return render(req,'myzakaz.html',data)