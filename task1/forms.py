from django import forms



class UserRegister(forms.Form):
    username = forms.CharField(min_length=4,max_length=30 ,label="Введите логин")
    password  = forms.CharField(min_length=4,max_length=8, label="Введите пароль")
    repeat_password  = forms.CharField(min_length=4,max_length=8, label="Повторите пароль")
    age  = forms.IntegerField(min_value=19,max_value=120, label="Введите свой возраст")
    #balance = forms.IntegerField(label="ваш баланс")
