from django.urls import path
from . import views

urlpatterns = [
    path('createUser/', views.createUser),
    path('login/', views.loginUser),
    path('checkLogin/', views.checkLogin),
    path('logout/', views.userLogout),
    path('createTask/', views.criarTarefa),
    path('verTarefas/', views.verTarefas),
    path('verUmaTarefa/', views.verTarefaUnica),
    path('apagarTask/', views.deletarTarefa),
    path('editarTask/', views.editarTarefa),
    path('concluirTask/', views.concluirTask)
]