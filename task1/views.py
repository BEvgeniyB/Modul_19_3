from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
from .forms import UserRegister
from .models import *

#users = ["Petro", "Sergey", "Diana", "Teodor"]
# Create your views here.

def main(request):
    title = 'Главная страница сайта'
    context = {'Title':title,}
    return render(request,"main_3.html",context=context)

def shop(request):
    title = 'Магазин'
    games = Game.objects.all()

    context = {'list':games,'Title':title}
    return render(request,"shop.html",context=context)

def shopping_cart(request):
    title = 'Корзина'
    context = {'title':title,}
    return render(request,"shopping_cart.html",context=context)

def sign_up_by_django(request: WSGIRequest):
    buyers = Buyer.objects.all()
    users = [buyer.name for buyer in buyers]
    info = {}
    if request.method == "POST":
        form = UserRegister(request.POST)
        info['form'] = form
        if form.is_valid():
            info['username'] = form.cleaned_data["username"]
            info['password'] = form.cleaned_data["password"]
            info['repeat_password'] = form.cleaned_data["repeat_password"]
            info['age'] = form.cleaned_data["age"]

            if info['password'] == info['repeat_password'] and not users.count(info['username']):
                Buyer.objects.create(name=info['username'], age= info['age'])
                info["generated"] = f"Приветствуем, {info['username']}!"
            elif users.count(info['username']):
                info["error"] = "Пользователь уже существует"
            elif info['password'] != info['repeat_password']:
                info["error"] = "Пароли не совпадают"
            else:
                info["error"] = "Вы должны быть старше 18"
        return render(request, template_name="registration_page.html", context=info)

    else:
        form = UserRegister()
        return render(request, template_name="registration_page.html",context={'form':form})
