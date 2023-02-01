from django.urls import path

from django.contrib.auth import views as auth_views

from .views import PaginaPerfil


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(
        template_name='usuarios/login.html'
    ), name='login'),

    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('perfil/', PaginaPerfil.as_view(), name='perfil'),

]