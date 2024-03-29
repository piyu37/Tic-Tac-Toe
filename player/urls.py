from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('home/', views.home, name="player_home"),
    path('login/', LoginView.as_view(template_name="player/login_form.html"), name="player_login"),
    path('logout/', LogoutView.as_view(), name="player_logout"),
    path('new_invitation/', views.new_invitation, name="player_new_invitation"),
    path('accept_invitation/<id>/', views.accept_invitation, name="player_accept_invitation"),
    path('signup/', views.SignUpView.as_view(), name='player_signup')
]
