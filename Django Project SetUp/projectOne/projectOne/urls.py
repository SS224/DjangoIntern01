from django.contrib import admin
from django.urls import path
from appOne import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('d1/', views.d1),
    path('d2/', views.d2),
    path('d3/', views.d3)
]
