"""
URL configuration for progym project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from gym1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),

    path('login/',views.login),
    path('login1/',views.login1),
    path('trainerHome/',views.trainerHome),
    path('userHome/',views.userHome),
    path('adminHome/',views.adminHome),

    # path('trainerForm',views.trainerForm),
    path('create_account/',views.create_account),
    path('trainers/',views.trainers),
    path('about/',views.about),
    path('service/',views.service),
    path('contact/',views.contact),
    path('create_account2/',views.create_account2),
    path('create_trainer2/',views.create_trainer2),
    path('view_trainer/',views.view_trainer),
    # path('update_trainer2/<int:id>',views.update_trainer2),
]


if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)