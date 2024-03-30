from django.contrib import admin
from django.urls import path, include
from analisedf.views import Login
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoginView.as_view()),
    path('',include('analisedf.urls')),
    path('', include('accounts.urls')), # rotas personalizadas como accounts/signup
    path('accounts/', include('django.contrib.auth.urls')), # rotas fornecidas pelo Django
]
