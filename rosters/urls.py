from django.urls import path
from . import views

urlpatterns = [
    path('divisions/', views.divisions, name='divisions'),
    path('add-division/', views.add_division, name='add-division'),
    path('teams/', views.teams, name='teams'),
    path('add-team/', views.add_team, name='add-team'),
    path('team/<int:team_id>/', views.team_detail, name='team-detail'),
    path('add-player/<int:division_id>/', views.add_player, name='add-player'),
    path('edit-player-stats/', views.edit_player_stats, name='edit-player-stats'),
    path('schedules/', views.schedules, name='schedules'),
    path('scheduled-games/<int:division_id>/', views.scheduled_games, name='scheduled-games'),
    path('add-game/<int:division_id>/', views.add_game, name='add_game'),
]
