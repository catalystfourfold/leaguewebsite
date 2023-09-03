from django.contrib import admin
from .models import Division, Team, Player, Game

admin.site.register(Division)
admin.site.register(Team)
admin.site.register(Player)
admin.site.register(Game)