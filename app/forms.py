from django import forms
from django.core.validators import RegexValidator
from django.contrib.auth.forms import UserCreationForm


######################################
PHONE_REGEX = r'^\+?7(?:[0-9]{2})?[0-9]{9}$'
# Создаем валидатор для телефона
tel_validator = RegexValidator(regex=PHONE_REGEX, message="Некорректный номер телефона.")
class FormOrder(forms.Form):
    city = forms.CharField(label='Город',help_text='',
                           error_messages={'required':'не заполнил поле'})
    street = forms.CharField(label='Улица',help_text='')
    house = forms.CharField(label='Дом',help_text='')
    tel = forms.CharField(label='Телефон',widget=forms.TextInput(
                            attrs={'placeholder': '+7'}))
    nerobot = forms.BooleanField(label='не робот')
######################################

# class FormOrder(forms.Form):
#     adres = forms.CharField(label='Адрес доставки')
#     tel = forms.CharField(label='Телефон')
#     nerobot = forms.BooleanField(label='не робот')
class formRegistr(UserCreationForm):
    username = forms.CharField(label='Login',
                                help_text='')
    password1 = forms.CharField(label='Пароль',
                                help_text='',
                                widget=forms.PasswordInput(
                                attrs={'autocomplete': 'new-password'}
                                ))

    password2 = forms.CharField(label='Подтверждение Пароля',
                                    help_text='',
                                    widget=forms.PasswordInput(
                                        attrs={'autocomplete': 'new-password'}
                                    ))
    email = forms.EmailField(label='Почта',
                            widget=forms.TextInput(
                            attrs={'placeholder': 'qwe@mail.ru'}))
    first_name = forms.CharField(label='Имя', required=False)
    last_name = forms.CharField(label='Фамилия', required=False)
    # captcha = CaptchaField()

