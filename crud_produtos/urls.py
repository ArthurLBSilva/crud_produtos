from django.urls import path
from loja import views
urlpatterns = [
    path('cadastro/', views.home, name='home'),
]
