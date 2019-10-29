from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('detail/<id>/', views.game_detail, name="gameplay_detail"),
    path('make_move/<id>/', views.make_move, name="gameplay_make_move"),
    path('all/', views.AllGamesList.as_view())
]
