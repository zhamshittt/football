from django.db import models

class Tournament(models.Model):
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to='images')
    year = models.IntegerField()
    member_count = models.IntegerField()

    class Meta:
        verbose_name = 'Турнир'
        verbose_name_plural = 'Турниры'

    def __str__(self):
        return f" {self.title} "

class Team(models.Model):
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to='images')

    class Meta:
        verbose_name = 'Команда'
        verbose_name_plural = 'Команды'

    def __str__(self):
        return f" {self.title} "



class TourmentTeam(models.Model):
    team = models.ManyToManyField('Team')
    tourment = models.ForeignKey(Tournament, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Чемпионат мира'
        verbose_name_plural = 'Чемпионаты мира'

    def __str__(self):
        return f"{self.tourment}"

class Match(models.Model):

    class Meta:
        verbose_name = 'Матч'
        verbose_name_plural = 'Матчи'

    STATUS_CHOICES = (
        (1, 'Запланированный'),
        (2, 'Прямо сейчас'),
        (3, 'Завершенный')
    )
    STAGE_CHOICES = (
        (1, '1/8 финал'),
        (2, '1/4 финал'),
        (3, '1/2 финал'),
        (4, '3-место'),
        (5, 'Финал')
    )
    WINS_CHOICES = (
        (1, 'Побед хозяев'),
        (2, 'Побед гостей'),
        (3, 'Ничья')
    )
    date = models.DateField()
    home_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='home_matches')
    away_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='away_matches')
    winner = models.PositiveSmallIntegerField(choices=WINS_CHOICES, default=1)
    home_team_score = models.PositiveIntegerField()
    away_team_score = models.PositiveIntegerField()
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    status = models.PositiveSmallIntegerField(choices=STATUS_CHOICES)
    stage = models.PositiveSmallIntegerField(choices=STAGE_CHOICES)
    is_played = models.BooleanField(default=True)
    is_penalty = models.BooleanField(default=False)
    home_team_penalty = models.PositiveSmallIntegerField(null=False, default=0)
    away_team_penalty = models.PositiveSmallIntegerField(null=False, default=0)

    def __str__(self):
        return f"{self.home_team} vs {self.away_team}"
class Player(models.Model):

    class Meta:

        verbose_name = 'Игрок'
        verbose_name_plural = 'Игроки'

    name = models.CharField(max_length=250)
    shirt_number = models.IntegerField()
    role = models.CharField(max_length=250)
    image = models.ImageField(upload_to='images', null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    height = models.PositiveSmallIntegerField(null=True, blank=True)
    weight = models.PositiveSmallIntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.name}"

class PlayerStatistics(models.Model):

    class Meta:
        verbose_name = 'Статистика игрока'
        verbose_name_plural = 'Статистики игроков'

    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    team = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    goal = models.PositiveSmallIntegerField()
    penalty = models.PositiveSmallIntegerField()
    minut = models.PositiveSmallIntegerField()
    game = models.PositiveSmallIntegerField()
    tourment = models.ForeignKey(Tournament, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.player}"

class Trainers(models.Model):

    class Meta:
        verbose_name = 'Тренер'
        verbose_name_plural = 'Тренеры'

    image = models.ImageField(upload_to='images', null=True, blank=True)
    name = models.CharField(max_length=250)
    birthday = models.DateField(null=True, blank=True)
    team = models.CharField(max_length=100)
    matches = models.PositiveSmallIntegerField()
    wins = models.PositiveSmallIntegerField()
    drows = models.PositiveSmallIntegerField()
    defeats = models.PositiveSmallIntegerField()
    points = models.PositiveSmallIntegerField()
    tourment = models.ForeignKey(Tournament, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"

class Stadium(models.Model):

    class Meta:
        verbose_name = 'Стадион'
        verbose_name_plural = 'Стадионы'

    image = models.ImageField(upload_to='images', null=True, blank=True)
    name = models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    capacity = models.PositiveSmallIntegerField()
    average_capacity = models.PositiveSmallIntegerField()
    memorability = models.DecimalField(max_digits=8, decimal_places=2)
    matches = models.PositiveSmallIntegerField()
    tourment = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.name}"

class Judge(models.Model):

    class Meta:
        verbose_name = 'Судьия'
        verbose_name_plural = 'Судьи'

    image = models.ImageField(upload_to='images', null=True, blank=True)
    name = models.CharField(max_length=250)
    birthday = models.DateField(null=True, blank=True)
    matches = models.PositiveSmallIntegerField()
    chief_judge = models.PositiveSmallIntegerField()
    yellow_card = models.PositiveSmallIntegerField()
    second_yellow_card = models.PositiveSmallIntegerField()
    red_card = models.PositiveSmallIntegerField()
    penalty = models.PositiveSmallIntegerField()
    tourment = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.name}"


class TeamComposition(models.Model):

    class Meta:
        verbose_name = 'Состав'
        verbose_name_plural = 'Составы'

    STATUS_CHOICES = (
        (1, 'Дома'),
        (2, 'В гости')
    )
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    players = models.ManyToManyField(Player)
    status = models.PositiveSmallIntegerField(choices=STATUS_CHOICES)

    def __str__(self):
        return f"{self.players}"

class Goal(models.Model):

    class Meta:
        verbose_name = 'Гол'
        verbose_name_plural = 'Голы'

    time = models.CharField(max_length=250)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.player}"

class TeamPlayer(models.Model):

    class Meta:
        verbose_name = 'Командный игрок'
        verbose_name_plural = 'Командные игроки'

    players = models.ManyToManyField(Player)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.team}"



