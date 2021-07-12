from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_matches, name='matches'),
    path('<int:game_id>/', views.match_detail, name='match_detail'),
    path('add/', views.add_match, name='add_match'),
]
