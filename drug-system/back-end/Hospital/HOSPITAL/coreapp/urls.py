from django.urls import path
from . import views

urlpatterns = [
    path('',views.Overview,name='api-overview'),
    path('drug-list/',views.DrugList,name='drug-list'),
    path('drug-add/',views.AddGrug,name='drug-add'),
    path('drug-update/<int:pk>/',views.UpadateDrug,name='drug-update'),
    path('drug-delete/<int:pk>/',views.Delete,name='drug-delete'),
]