"""
URL configuration for djangoProject1Cart project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views
from django.urls import path,include
urlpatterns = [


    path('admin/', admin.site.urls),
    path('',views.index, name='home'),
    path('goods/<str:cat>/',views.goods, name='goods'),
    path('goods/buy/<int:itemid>/<str:cat>/',views.buy, name='buy'),
    path('cart/',views.cart, name='cart'),
    path('cart/delete/<int:itemid>/',views.delete, name='delete'),
    path('cart/edit/<int:itemid>/<str:num>/',views.edit, name='edit'),
    path('kabinet/',views.kabinet, name='kabinet'),
    path('myzakaz/<int:itemid>/',views.myzakaz,name='myzakaz'),


    path('auth/',include('django.contrib.auth.urls')),
    path('auth/registation/',views.registr,name='registr'),
    path('accounts/login/',views.index),
    # path('auth/profile', views.profile, name='kabinet'),
    # path('auth/profile/change', views.profileChange, name='kabinetChange'),
    # path('captcha/',include('captcha.urls')),
]
