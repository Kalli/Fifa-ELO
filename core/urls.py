from django.conf.urls.defaults import patterns, url
from views import home, score, view_team, view_player, achievements, all_teams, all_games, generate_teams, calculate_results, compare_teams
urlpatterns = patterns('',
    url(r'^$', home, name='home'),
    url(r'^score/$', score, name='score'),
    url(r'^achievements/$', achievements, name='achievements'),
    url(r'^generate_teams/$', generate_teams, name='generate-teams'),
    url(r'^compare_teams/$', compare_teams, name='compare-teams'),
    url(r'^all_teams/$', all_teams, name='all-teams'),
    url(r'^all_games/$', all_games, name='all-games'),
    url(r'^calculate_results/$', calculate_results, name='calculate-results'),
    url(r'^view_team/(?P<team_id>\d+)/$', view_team, name='view-team'),
    url(r'^view_player/(?P<player_id>\d+)/$', view_player, name='view-player'),
)
