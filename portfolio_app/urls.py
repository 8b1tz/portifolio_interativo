from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sobre/', views.sobre, name='sobre'),
    path('projetos/', views.listar_projetos, name='projetos'),

    # Login e logout
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),

    # Registro
    path('register/', views.register, name='register'),

    # Demonstrar interesse
    path('demonstrar-interesse/', views.demonstrar_interesse, name='demonstrar_interesse'),

    # Painel de interesses (para superusuário)
    path('painel/interesses/', views.listar_interesses, name='listar_interesses'),
    path('painel/interesses/<int:interest_id>/responder/', views.responder_interesse, name='responder_interesse'),
]
