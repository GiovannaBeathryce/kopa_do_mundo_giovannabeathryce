# from django.shortcuts import render
from rest_framework.views import APIView, Request, Response, status
from .models import Team
from django.forms.models import model_to_dict


class TeamView(APIView):
    def get(self, req: Request) -> Response:
        teams = Team.objects.all()
        teams_list = []
        for team in teams:
            team_dict = model_to_dict(team)
            teams_list.append(team_dict)

        return Response(teams_list)
    

    def post(self, req: Request) -> Response:
        team = Team.objects.create(**req.data)

        return Response(model_to_dict(team), status.HTTP_201_CREATED)
    

class TeamDetailView(APIView):
    def get(self, req: Request, id_team: int) -> Response:
        try:
            team = Team.objects.get(id=id_team)
        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, status.HTTP_404_NOT_FOUND)

        return Response(model_to_dict(team), status.HTTP_200_OK)
    

    def patch(self, req: Request, id_team: int) -> Response:
        try:
            team = Team.objects.get(id=id_team)
        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, status.HTTP_404_NOT_FOUND)

        for key, value in req.data.items():
            setattr(team, key, value)

        team.save()    

        return Response(model_to_dict(team), status.HTTP_200_OK)

    
    def delete(self, req: Request, id_team: int) -> Response:
        try:
            team = Team.objects.get(id=id_team)
        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, status.HTTP_404_NOT_FOUND)

        team.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

