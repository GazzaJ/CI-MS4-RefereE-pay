from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_matches, name='matches'),
    path('<int:game_id>/', views.match_detail, name='match_detail'),
    path('travel/<int:game_id>/', views.add_travel, name='add_travel'),
    path('comp/', views.add_competition, name='add_competition'),
    path('club/', views.add_club, name='add_club'),
    path('team/', views.add_team, name='add_team'),
    path('add/', views.add_match, name='add_match'),
    path('edit/<int:game_id>/', views.edit_match, name='edit_match'),
    path('delete/<int:game_id>/', views.delete_match, name='delete_match'),
    path('chat/<int:game_id>/', views.match_chat, name='match_chat'),
    path('add_chat/<int:game_id>/', views.add_chat, name='add_chat'),
    path('clubs', views.all_clubs, name='clubs'),
    path('edit_club/<int:club_id>/', views.edit_club, name='edit_club'),
    path('delete_club/<int:club_id>/', views.delete_club, name='delete_club'),
    path('teams/<int:club_id>/', views.club_teams, name='teams'),
    path('edit_team/<int:team_id>', views.edit_team, name='edit_team'),

    path('ajax/load_teams', views.load_teams, name='ajax_load_teams'),
]
