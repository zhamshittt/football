from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import Tournament, Team, Match, Player, TeamComposition, Goal, TourmentTeam, TeamPlayer, PlayerStatistics, Trainers, Stadium, Judge
admin.site.register(Tournament)
admin.site.register(Team)
admin.site.register(Match)
admin.site.register(Player)
admin.site.register(TeamComposition)
admin.site.register(Goal)
admin.site.register(TourmentTeam)
admin.site.register(TeamPlayer)
admin.site.register(PlayerStatistics)
admin.site.register(Trainers)
admin.site.register(Stadium)
admin.site.register(Judge)

admin.site.site_header = _('Чемпионат Мира по Футболу')

