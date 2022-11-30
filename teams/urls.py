from django.urls import path
from teams.views import TeamView, TeamDetailView

urlpatterns = [
    path('teams/', TeamView.as_view()),
    path('teams/<int:id_team>/', TeamDetailView.as_view())
]

