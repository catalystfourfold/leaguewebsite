from django.db import models

class Division(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=50)
    division = models.ForeignKey(Division, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Player(models.Model):
    name = models.CharField(max_length=100)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    avg = models.DecimalField(default="0.000", max_digits=4, decimal_places=3, null=True, blank=True)
    gp = models.PositiveIntegerField(default="0", null=True, blank=True)
    gs = models.PositiveIntegerField(default="0", null=True, blank=True)
    pa = models.PositiveIntegerField(default="0", null=True, blank=True)
    ab = models.PositiveIntegerField(default="0", null=True, blank=True)
    r = models.PositiveIntegerField(default="0", null=True, blank=True)
    h = models.PositiveIntegerField(default="0", null=True, blank=True)
    twob = models.PositiveIntegerField(default="0", null=True, blank=True)
    threeb = models.PositiveIntegerField(default="0", null=True, blank=True)
    hr = models.PositiveIntegerField(default="0", null=True, blank=True)
    rbi = models.PositiveIntegerField(default="0", null=True, blank=True)
    bb = models.PositiveIntegerField(default="0", null=True, blank=True)
    k = models.PositiveIntegerField(default="0", null=True, blank=True)
    hbp = models.PositiveIntegerField(default="0", null=True, blank=True)
    ibb = models.PositiveIntegerField(default="0", null=True, blank=True)
    sb = models.PositiveIntegerField(default="0", null=True, blank=True)
    cs = models.PositiveIntegerField(default="0", null=True, blank=True)
    sh = models.PositiveIntegerField(default="0", null=True, blank=True)
    sf = models.PositiveIntegerField(default="0", null=True, blank=True)
    dp = models.PositiveIntegerField(default="0", null=True, blank=True)
    roe = models.PositiveIntegerField(default="0", null=True, blank=True)
    fc = models.PositiveIntegerField(default="0", null=True, blank=True)
    lob = models.PositiveIntegerField(default="0", null=True, blank=True)
    tb = models.PositiveIntegerField(default="0", null=True, blank=True)
    obp = models.DecimalField(default="0.000", max_digits=4, decimal_places=3, null=True, blank=True)
    slg = models.DecimalField(default="0.000", max_digits=4, decimal_places=3, null=True, blank=True)
    ops = models.DecimalField(default="0.000", max_digits=4, decimal_places=3, null=True, blank=True)

    def __str__(self):
        return self.name
    
class Game(models.Model):
    division = models.ForeignKey(Division, on_delete=models.CASCADE)
    day = models.CharField(max_length=5)
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(max_length=10)
    score = models.CharField(max_length=10)
    visitors = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='away_games')
    home = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='home_games')
    venue = models.CharField(max_length=50)