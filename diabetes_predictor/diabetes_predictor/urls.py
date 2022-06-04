"""diabetes_predictor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import include, path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    # path('apoiar', views.apoiar, name="apoiar"),
    # path('register',views.register, name="register"),
    # path('login',views.login, name="login"),
    # path('diagnostico',views.diagnostico, name="diagnostico"),
    # path('base',views.base, name="base"),
    # path('diabetes',views.diabetes,name="diabetes"),
    # path('diabetesTipo1',views.diabetesTipo1,name="diabetesTipo1")
    path('diabetes',include('diabetes.urls')),
    path('diagnostic',include('diagnostic.urls')),
    path('login',include('login.urls')),
   #path('loginRef',views.login,name="loginRef"),
    path('register',include('register.urls')),
    path('projectsupport',include('project_support.urls')),
]

urlpatterns += staticfiles_urlpatterns()
