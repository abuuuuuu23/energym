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

    
    path('create_account/',views.create_account),
    path('trainers/',views.trainers),
    path('about/',views.about),
    path('service/',views.service),
    path('contact/',views.contact),
    path('create_account2/',views.create_account2),
    path('create_trainer2/',views.create_trainer2),
    path('view_trainer/',views.view_trainer),
    path('update_trainer/<int:id>',views.update_trainer),
    path('update_trainer2/<int:id>',views.update_trainer2),
    path('view_user/',views.view_user),
    path('delete_trainer/',views.delete_trainer),
    path('delete_trainer1/<int:id>',views.delete_trainer1),
    path('trainer_d/<int:id>',views.trainer_d),
    path('logout/',views.logout),
    path('update_user/',views.update_user),
    path('update_user2/',views.update_user2),
    path('delete_user/',views.delete_user),
    path('delete_user2/<int:id>',views.delete_user2),
    path('aboutT/',views.aboutT) ,
    path('packages1/',views.packages1),
    path('view_packages/<int:id>',views.view_packages),
    path('view_packages1/',views.view_packages1),
    path('gymdata1/<int:id>',views.gymdata1),
    path('gymdata2/<int:id>',views.gymdata2),
    path('packages2/',views.packages2),
    path('update_packages/<int:id>',views.update_packages),
    path('update_packages2/<int:id>',views.update_packages2),
    path('delete_packages/<int:id>',views.delete_packages),
    path('workout/',views.workout),
    path('pending/',views.pending),
    path('update_status/<int:id>',views.update_status),
    path('update_status2/<int:id>',views.update_status2),
    path('workout2/',views.workout2),


]


if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)