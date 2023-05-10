from django.shortcuts import render, redirect
from django.views.generic.base import View, TemplateResponseMixin
from .models import Tournament, Match, TourmentTeam, Team, TeamPlayer, PlayerStatistics, Trainers, Stadium, Judge

class IndexView(TemplateResponseMixin, View):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        pk = request.GET.get('tourment_id', 1)
        tourment_id = Tournament.objects.get(pk=pk)
        tourments = Tournament.objects.all()
        matches_count = Match.objects.filter(tournament=tourment_id).count()
        matches_played = Match.objects.filter(tournament=tourment_id, is_played=True).count()
        home_wins = Match.objects.filter(tournament=tourment_id, winner=1).count()
        away_wins = Match.objects.filter(tournament=tourment_id, winner=2).count()
        drows = Match.objects.filter(tournament=tourment_id, winner=3).count()
        if pk:
            matches_1_8 = Match.objects.filter(tournament=tourment_id, stage=1)
            matches_1_4 = Match.objects.filter(tournament=tourment_id, stage=2)
            matches_1_2 = Match.objects.filter(tournament=tourment_id, stage=3)
            matches_3_mesto = Match.objects.filter(tournament=tourment_id, stage=4)
            matches_final = Match.objects.filter(tournament=tourment_id, stage=5)
            return self.render_to_response({
                'tourments': tourments, 'matches_1_8': matches_1_8,
                'matches_1_4': matches_1_4, 'matches_1_2': matches_1_2,
                'matches_3_mesto': matches_3_mesto, 'matches_final': matches_final,
                'drows': drows, 'matches_count': matches_count, 'matches_played': matches_played,
                'home_wins': home_wins, 'away_wins': away_wins, 'pk': pk
            })
        return self.render_to_response({
            'tourments': tourments, 'matches_count': matches_count, 'matches_played': matches_played,
            'home_wins': home_wins, 'away_wins': away_wins, 'drows': drows, 'tourment_id': tourment_id
            })

class TourmentTeamView(TemplateResponseMixin, View):
    template_name = 'team.html'

    def get(self, request, *args, **kwargs):
        pk = request.GET.get('tourment_id', 1)
        tourment_id = Tournament.objects.get(pk=pk)
        tourments = Tournament.objects.all()
        team_tourment = TourmentTeam.objects.get(tourment=tourment_id)
        teams = team_tourment.team.all()
        return self.render_to_response({
            'tourments': tourments, 'tourment_id': tourment_id, 'pk': pk, 'teams': teams
            })

class TourmentTableView(TemplateResponseMixin, View):
    template_name = 'tourment_table.html'

    def get(self, request, *args, **kwargs):
        pk = request.GET.get('tourment_id', 1)
        tourment_id = Tournament.objects.get(pk=pk)
        tourments = Tournament.objects.all()
        matches_1_8 = Match.objects.filter(tournament=tourment_id, stage=1)
        matches_1_4 = Match.objects.filter(tournament=tourment_id, stage=2)
        matches_1_2 = Match.objects.filter(tournament=tourment_id, stage=3)
        matches_3_mesto = Match.objects.filter(tournament=tourment_id, stage=4)
        matches_final = Match.objects.filter(tournament=tourment_id, stage=5)

        return self.render_to_response({
            'tourments': tourments, 'matches_1_8': matches_1_8,
            'matches_1_4': matches_1_4, 'matches_1_2': matches_1_2,
            'matches_3_mesto': matches_3_mesto, 'matches_final': matches_final, 'pk': pk
        })

class TeamDetailView(TemplateResponseMixin, View):
    template_name = 'team_detail.html'

    def get(self, request, *args, **kwargs):
        pk = request.GET.get('tourment_id', 1)
        team_id = self.kwargs.get('team_id')
        team = Team.objects.get(id=team_id)
        team_player = TeamPlayer.objects.get(team=team)
        players = team_player.players.all()
        tourments = Tournament.objects.all()
        return self.render_to_response({
            'tourments': tourments, 'pk': pk,
            'team': team, 'players': players
        })

class PlayerStatisticsView(TemplateResponseMixin, View):
    template_name = 'player_statistics.html'

    def get(self, request, *args, **kwargs):
        pk = request.GET.get('tourment_id', 1)
        players = PlayerStatistics.objects.filter(tourment=pk)
        tourments = Tournament.objects.all()
        return self.render_to_response({
            'tourments': tourments, 'pk': pk, 'players': players
        })

class TrenersView(TemplateResponseMixin, View):
    template_name = 'trainers.html'

    def get(self, request, *args, **kwargs):
        pk = request.GET.get('tourment_id', 1)
        trainers = Trainers.objects.filter(tourment=pk)
        tourments = Tournament.objects.all()
        return self.render_to_response({
            'tourments': tourments, 'pk': pk, 'trainers': trainers
        })

class StadiumsView(TemplateResponseMixin, View):
    template_name = 'stadiums.html'

    def get(self, request, *args, **kwargs):
        pk = request.GET.get('tourment_id', 1)
        stadiums = Stadium.objects.filter(tourment=pk)
        tourments = Tournament.objects.all()
        return self.render_to_response({
            'tourments': tourments, 'pk': pk, 'stadiums': stadiums
        })

class JudgesView(TemplateResponseMixin, View):
    template_name = 'judges.html'

    def get(self, request, *args, **kwargs):
        pk = request.GET.get('tourment_id', 1)
        judges = Judge.objects.filter(tourment=pk)
        tourments = Tournament.objects.all()
        return self.render_to_response({
            'tourments': tourments, 'pk': pk, 'judges': judges
        })

        