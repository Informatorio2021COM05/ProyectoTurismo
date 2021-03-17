from django.urls import path
from .views import SignUpView, BienvenidaView, SignInView, SignOutView

urlpatterns = [
    path('bienvenida/', BienvenidaView.as_view(), name='bienvenida'),
    path('registrate/', SignUpView.as_view(), name='sign_up'),
    path('incia-sesion/', SignInView.as_view(), name='sign_in'),
    path('cerrar-sesion/', SignOutView.as_view(), name='sign_out'),
]
