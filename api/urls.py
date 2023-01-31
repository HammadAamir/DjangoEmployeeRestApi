from django.urls import path
from . import views

urlpatterns = [
    path('', views.overview),
    path('get/', views.getData),
    path('get/<int:pk>/', views.getEmployee),
    path('add/', views.addEmployee),
    path('update/<int:pk>', views.updateEmployee),
    path('delete/<int:pk>', views.deleteEmployee)
]
