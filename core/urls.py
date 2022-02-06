"""core URL Configuration
"""

from django.contrib import admin
from django.urls import path, include 

from TODOapp.views import SetTaskView
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'task', SetTaskView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
