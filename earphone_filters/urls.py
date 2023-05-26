
from django.urls import path
from . import views

urlpatterns = [
    path("", views.earphone_list, name='earphone_list'),
    path('earphones/<int:pk>/', views.earphone_detail, name='earphone_detail'),
]
