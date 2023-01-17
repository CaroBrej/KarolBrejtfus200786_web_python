from django.urls import path
from . import views

urlpatterns = [
    path('', views.endpoints),
    #person
    #path('person_list/', views.person_list, name='person_list'),
    path('person_list/', views.PersonList.as_view()),
    #path('person_detail/<int:id>/', views.person_detail),
    path('person_detail/<int:id>/', views.PersonDetail.as_view()),
    #sportclubs
    #path('sport_club_list/', views.sport_clubs_list),
    path('sport_club_list/', views.SportClubsList.as_view()),
    path('sport_club_detail/<int:id>/', views.SportClubDetail.as_view()),
    #tournament
    path('tournament_list/', views.TournamentsList.as_view()),
    path('tournament_detail/<int:id>/', views.TournamentDetail.as_view()),
    # result
    path('results_list/', views.ResultList.as_view()),
    path('results_detail/<int:id>/', views.ResultClubDetail.as_view()),


]