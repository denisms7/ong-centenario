from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from .views import Home, Sobre


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pet.urls')),
    path('', include('usuarios.urls')),


    path('', Home.as_view(), name='inicio'),
    path('estatuto/', Sobre.as_view(), name='estatuto'),
]

if settings.DEBUG == True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
