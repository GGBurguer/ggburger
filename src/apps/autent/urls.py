from django.urls import path
from . import views

urlpatterns = [
	path("login_form/", views.login_form_template),
	path("login_sesion/", views.iniciar_sesion, name="iniciar_sesion"),
	path("cargar_entidad/", views.cargar_usuario, name="cargar_usuario"),
	path("login_token_test/", views.token_login_test),
]
