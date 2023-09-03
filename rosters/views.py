from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Division, Team, Player, Game
from .forms import DivisionForm, TeamForm, PlayerForm, GameForm
from django.contrib.auth.decorators import login_required

def divisions(request):
    divisions = Division.objects.all()
    if request.method == 'POST':
        form = DivisionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('divisions')
    else:
        form = DivisionForm()

    return render(request, 'rosters/divisions.html', {'divisions': divisions, 'form': form})

@login_required
def add_division(request):
    if request.method == 'POST':
        form = DivisionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('divisions')
    else:
        form = DivisionForm()

    return render(request, 'rosters/add_division.html', {'form': form})

def teams(request):
    division_id = request.GET.get('division')
    if division_id:
        division = Division.objects.get(pk=division_id)
        teams = division.team_set.all()
        teams_data = [{'id': team.id, 'name': team.name, 'division_id': team.division_id} for team in teams]
        return JsonResponse({'teams': teams_data})
    else:
        return JsonResponse({'teams': []})

@login_required
def add_team(request):
    if request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('divisions')  
    else:
        form = TeamForm()

    return render(request, 'rosters/add_team.html', {'form': form})

def team_detail(request, team_id):
    team = Team.objects.get(pk=team_id)
    division_id = team.division_id
    division = Division.objects.get(pk=division_id)
    players = team.player_set.all()
    return render(request, 'rosters/team_detail.html', {'team': team, 'division': division, 'players': players})

@login_required
def add_player(request, division_id):
    if request.method == 'POST':
        form = PlayerForm(request.POST)
        print(form.data)
        if form.is_valid():
            player = form.save(commit=False)
            team_id = form.cleaned_data['team']  
            player.team = team_id  
            player.save()
            return redirect('divisions')
    else:
        form = PlayerForm()
    return render(request, 'rosters/add_player.html', {'form': form, 'division_id': division_id})

@login_required
def edit_player_stats(request):
    players = Player.objects.all()

    if request.method == 'POST':
        for player in players:
            avg_key = f'avg_{player.id}'
            gp_key = f'gp_{player.id}'
            gs_key = f'gs_{player.id}'
            pa_key = f'pa_{player.id}'
            ab_key = f'ab_{player.id}'
            r_key = f'r_{player.id}'
            h_key = f'h_{player.id}'
            twob_key = f'2b_{player.id}'
            threeb_key = f'3b_{player.id}'
            hr_key = f'hr_{player.id}'
            rbi_key = f'rbi_{player.id}'
            bb_key = f'bb_{player.id}'
            k_key = f'k_{player.id}'
            hbp_key = f'hbp_{player.id}'
            ibb_key = f'ibb_{player.id}'
            sb_key = f'sb_{player.id}'
            cs_key = f'cs_{player.id}'
            sh_key = f'sh_{player.id}'
            sf_key = f'sf_{player.id}'
            dp_key = f'dp_{player.id}'
            roe_key = f'roe_{player.id}'
            fc_key = f'fc_{player.id}'
            lob_key = f'lob_{player.id}'
            tb_key = f'tb_{player.id}'
            obp_key = f'obp_{player.id}'
            slg_key = f'slg_{player.id}'
            ops_key = f'ops_{player.id}'

            new_avg = request.POST.get(avg_key)
            new_gp = request.POST.get(gp_key)
            new_gs = request.POST.get(gs_key)
            new_pa = request.POST.get(pa_key)
            new_ab = request.POST.get(ab_key)
            new_r = request.POST.get(r_key)
            new_h = request.POST.get(h_key)
            new_2b = request.POST.get(twob_key)
            new_3b = request.POST.get(threeb_key)
            new_hr = request.POST.get(hr_key)
            new_rbi = request.POST.get(rbi_key)
            new_bb = request.POST.get(bb_key)
            new_k = request.POST.get(k_key)
            new_hbp = request.POST.get(hbp_key)
            new_ibb = request.POST.get(ibb_key)
            new_sb = request.POST.get(sb_key)
            new_cs = request.POST.get(cs_key)
            new_sh = request.POST.get(sh_key)
            new_sf = request.POST.get(sf_key)
            new_dp = request.POST.get(dp_key)
            new_roe = request.POST.get(roe_key)
            new_fc = request.POST.get(fc_key)
            new_lob = request.POST.get(lob_key)
            new_tb = request.POST.get(tb_key)
            new_obp = request.POST.get(obp_key)
            new_slg = request.POST.get(slg_key)
            new_ops = request.POST.get(ops_key)

            if new_avg is not None:
                player.avg = new_avg
            if new_gp is not None:
                player.gp = new_gp
            if new_pa is not None:
                player.gs = new_gs
            if new_ab is not None:
                player.ab = new_ab
            if new_r is not None:
                player.r = new_r
            if new_h is not None:
                player.h = new_h
            if new_2b is not None:
                player.twob = new_2b
            if new_3b is not None:
                player.threeb = new_3b
            if new_hr is not None:
                player.hr = new_hr
            if new_rbi is not None:
                player.rbi = new_rbi
            if new_bb is not None:
                player.bb = new_bb
            if new_k is not None:
                player.k = new_k
            if new_hbp is not None:
                player.hbp = new_hbp
            if new_ibb is not None:
                player.ibb = new_ibb
            if new_sb is not None:
                player.sb = new_sb
            if new_cs is not None:
                player.cs = new_cs
            if new_sh is not None:
                player.sh = new_sh
            if new_sf is not None:
                player.sf = new_sf
            if new_dp is not None:
                player.dp = new_dp
            if new_roe is not None:
                player.roe = new_roe
            if new_fc is not None:
                player.fc = new_fc
            if new_lob is not None:
                player.lob = new_lob
            if new_tb is not None:
                player.tb = new_tb
            if new_obp is not None:
                player.obp = new_obp
            if new_slg is not None:
                player.slg = new_slg
            if new_ops is not None:
                player.ops = new_ops

            player.save()

        return redirect('team-detail', team_id=player.team.id)

    return render(request, 'rosters/edit_player_stats.html', {'players': players})

def schedules(request):
    divisions = Division.objects.all()
    return render(request, 'rosters/schedules.html', {'divisions': divisions})

def scheduled_games(request, division_id):
    division = get_object_or_404(Division, id=division_id)
    games = Game.objects.filter(division=division)

    if request.method == 'POST':
        form = GameForm(division_id, request.POST)  # Pass division_id here
        if form.is_valid():
            game = form.save(commit=False)
            game.division = division
            game.save()
            # Optionally, you can add a success message or redirect to the same page
            return redirect('rosters:scheduled_games', division_id=division_id)
    else:
        form = GameForm(division_id=division_id)  # Pass division_id here

    return render(request, 'rosters/scheduled_games.html', {'division': division, 'games': games, 'form': form})

@login_required
def add_game(request, division_id):
    division = get_object_or_404(Division, id=division_id)

    if request.method == 'POST':
        form = GameForm(division_id, request.POST)
        if form.is_valid():
            game = form.save(commit=False)
            game.division = division
            game.save()
            return redirect('rosters:scheduled_games', division_id=division_id)
    else:
        form = GameForm(division_id=division_id)

    return render(request, 'rosters/add_game.html', {'division': division, 'form': form})