"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
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
from django.http import HttpResponse
from django.urls import path

from django.core.cache import cache


async def async_view(request):
    number = await cache.a.get('number', 0)
    await cache.a.set('number', number+1)
    return HttpResponse(str(number))


def sync_view(request):
    number = cache.s.get('number', 0)
    cache.s.set('number', number+1)
    return HttpResponse(str(number))


urlpatterns = [
    path('admin/', admin.site.urls),
    path('async/', async_view),
    path('sync/', sync_view),
]

