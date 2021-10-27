from django.urls import path
from . import views, auth
urlpatterns = [
    path('', views.index), 
    path('registro/', auth.registro),
    path('login/', auth.login),
    path('logout/', auth.logout),

    path('crear/mensaje', views.crear_mensaje),
    path('comentario/mensaje', views.crear_comentario),
    path('comentario/<int:val>/eliminar', views.eliminar_comentario)
]
