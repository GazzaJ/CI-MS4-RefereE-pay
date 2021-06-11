from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_matches, name='matches'),
    path('<game_id>', views.match_detail, name='match_detail'),
    path('<game_id>', views.match_fees, name='match_fees'),
]
