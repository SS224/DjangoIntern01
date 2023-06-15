from django.contrib import admin
from django.urls import path
from appOne import views as v1
from appTwo import views as v2
from appThree import views as v3

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', v1.d1),
    path('hi/', v2.d1),
    path('hey/', v3.d1)
]
