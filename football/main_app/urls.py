from django.urls import path
from . import views
app_name = 'main'

urlpatterns = [
    path('index/', views.IndexView.as_view(),
     name='index'),
    path('team/', views.TourmentTeamView.as_view(),
         name='team'),
    path('tourment/table/', views.TourmentTableView.as_view(),
         name='tourment_table'),
    path('tourment/team/<int:team_id>', views.TeamDetailView.as_view(),
         name='team_detail'),
    path('tourment/player/statistics', views.PlayerStatisticsView.as_view(),
         name='player_statistics'),
    path('tourment/trainers', views.TrenersView.as_view(),
         name='trainers'),
    path('tourment/stadiums', views.StadiumsView.as_view(),
         name='stadiums'),
    path('tourment/judges', views.JudgesView.as_view(),
         name='judges'),
]