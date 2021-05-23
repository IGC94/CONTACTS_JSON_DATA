from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add-profile/', views.Crate, name='add-profile'),
    path('profile/<str:pk>', views.Profile_ID, name='profile'),
    path('edit-profile/<str:pk>', views.Edit, name='edit-profile'),
    path('delete/<str:pk>', views.Delete, name='delete'),
    path('json/', views.json, name='json'),
]
