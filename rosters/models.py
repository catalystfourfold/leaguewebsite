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
    
    def calc_stats(self):
        games = self.playergamestats_set.all()

        avg = sum(game.avg for game in games) / len(games)
        gp = sum(game.gp for game in games)
        gs = sum(game.gs for game in games)
        pa = sum(game.pa for game in games)
        ab = sum(game.ab for game in games)
        r = sum(game.r for game in games)
        h = sum(game.h for game in games)
        twob = sum(game.twob for game in games)
        threeb = sum(game.threeb for game in games)
        hr = sum(game.hr for game in games)
        rbi = sum(game.rbi for game in games)
        bb = sum(game.bb for game in games)
        k = sum(game.k for game in games)
        hbp = sum(game.hbp for game in games)
        ibb = sum(game.ibb for game in games)
        sb = sum(game.sb for game in games)
        cs = sum(game.cs for game in games)
        sh = sum(game.sh for game in games)
        sf = sum(game.sf for game in games)
        dp = sum(game.dp for game in games)
        roe = sum(game.roe for game in games)
        fc = sum(game.fc for game in games)
        lob = sum(game.lob for game in games)
        tb = sum(game.tb for game in games)
        obp = sum(game.obp for game in games) / len(games)
        slg = sum(game.slg for game in games) / len(games)
        ops = sum(game.ops for game in games) / len(games)

        return {
            'avg': avg,
            'gp': gp,
            'gs': gs,
            'pa': pa,
            'ab': ab,
            'r': r,
            'h': h,
            'twob': twob,
            'threeb': threeb,
            'hr': hr,
            'rbi': rbi,
            'bb': bb,
            'k': k,
            'hbp': hbp,
            'ibb': ibb,
            'sb': sb,
            'cs': cs,
            'sh': sh,
            'sf': sf,
            'dp': dp,
            'roe': roe,
            'fc': fc,
            'lob': lob,
            'tb': tb,
            'obp': obp,
            'slg': slg,
            'ops': ops,
        }

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

class PlayerGameStats(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    avg = models.DecimalField(default="0.000", max_digits=4, decimal_places=3)
    gp = models.PositiveIntegerField(default="0")
    gs = models.PositiveIntegerField(default="0")
    pa = models.PositiveIntegerField(default="0")
    ab = models.PositiveIntegerField(default="0")
    r = models.PositiveIntegerField(default="0")
    h = models.PositiveIntegerField(default="0")
    twob = models.PositiveIntegerField(default="0")
    threeb = models.PositiveIntegerField(default="0")
    hr = models.PositiveIntegerField(default="0")
    rbi = models.PositiveIntegerField(default="0")
    bb = models.PositiveIntegerField(default="0")
    k = models.PositiveIntegerField(default="0")
    hbp = models.PositiveIntegerField(default="0")
    ibb = models.PositiveIntegerField(default="0")
    sb = models.PositiveIntegerField(default="0")
    cs = models.PositiveIntegerField(default="0")
    sh = models.PositiveIntegerField(default="0")
    sf = models.PositiveIntegerField(default="0")
    dp = models.PositiveIntegerField(default="0")
    roe = models.PositiveIntegerField(default="0")
    fc = models.PositiveIntegerField(default="0")
    lob = models.PositiveIntegerField(default="0")
    tb = models.PositiveIntegerField(default="0")
    obp = models.DecimalField(default="0.000", max_digits=4, decimal_places=3)
    slg = models.DecimalField(default="0.000", max_digits=4, decimal_places=3)
    ops = models.DecimalField(default="0.000", max_digits=4, decimal_places=3)