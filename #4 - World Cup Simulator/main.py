import pandas as pd
import random
from classes import Team, Group, Match
import math
import sim

df = pd.read_csv('ratings.csv')

team_names = [
  "mexico", "southKorea", "czechia", "southAfrica",
  "canada", "switzerland", "bosnia", "qatar",
  "scotland", "morocco", "brazil", "haiti",
  "unitedStates", "australia", "turkiye", "paraguay",
  "germany", "ivoryCoast", "ecuador", "curacao",
  "sweden", "japan", "netherlands", "tunisia",
  "newZealand", "iran", "belgium", "egypt",
  "uruguay", "saudiArabia", "spain", "caboVerde",
  "norway", "france", "senegal", "iraq",
  "argentina", "algeria", "austria", "jordan",
  "colombia", "drCongo", "portugal", "uzbekistan",
  "croatia", "england", "ghana", "panama"
]

teams = {name: Team("",0,0,0,0,0,0,0) for name in team_names}

for i, team in enumerate(teams.values()):
  sim.initTeam(team, i, df)

group_names = [
  "group_a", "group_b", "group_c", "group_d",
  "group_e", "group_f", "group_g", "group_h",
  "group_i", "group_j", "group_k", "group_l",
]

groups = {name: Group("","","","") for name in group_names}

matches = [Match("","",0,0,"") for i in range(6 * len(groups))]

for i, group in enumerate(groups.values()):
  start = i * 4
  group.team1, group.team2, group.team3, group.team4 = list(teams.values())[start:start+4]
  match_index = i * 6
  matches[match_index].team_a = group.team1
  matches[match_index].team_b = group.team2
  matches[match_index+1].team_a = group.team3
  matches[match_index+1].team_b = group.team4
  matches[match_index+2].team_a = group.team1
  matches[match_index+2].team_b = group.team4
  matches[match_index+3].team_a = group.team2
  matches[match_index+3].team_b = group.team3
  matches[match_index+4].team_a = group.team1
  matches[match_index+4].team_b = group.team3
  matches[match_index+5].team_a = group.team2
  matches[match_index+5].team_b = group.team4

user_input = input("Welcome to the World Cup Simulator! Type any letter to start.")

for group in groups.values():
  data = {
    "Team": [group.team1.name, group.team2.name, group.team3.name, group.team4.name],
    "Goals": [group.team1.goals, group.team2.goals, group.team3.goals, group.team4.goals],
    "Points": [group.team1.points, group.team2.points, group.team3.points, group.team4.points],
  }
  print(pd.DataFrame(data).sort_values(by='Points', ascending=False))

user_input = input("Are you ready? Type any letter to start.")

for match in matches:
  print(match.team_a.name+" - "+match.team_b.name)
  sim.simulate_match(match, match.team_a, match.team_b)
  print(match.team_a_goals,"-",match.team_b_goals)
  if match.team_a_goals > match.team_b_goals:
    match.result = match.team_a.name
    match.team_a.points += 3
  elif match.team_b_goals > match.team_a_goals:
    match.result = match.team_b.name
    match.team_b.points += 3
  elif match.team_a_goals == match.team_b_goals:
    match.result = "Draw"
    match.team_a.points += 1
    match.team_b.points += 1
  match.team_a.goals += match.team_a_goals
  match.team_b.goals += match.team_b_goals
  print(match.result)

user_input = input("Is it time to reveal the final standings? Type any letter to reveal.")

for group in groups.values():
  data = {
    "Team": [group.team1.name, group.team2.name, group.team3.name, group.team4.name],
    "Goals": [group.team1.goals, group.team2.goals, group.team3.goals, group.team4.goals],
    "Points": [group.team1.points, group.team2.points, group.team3.points, group.team4.points],
  }
  print(pd.DataFrame(data).sort_values(by='Points', ascending=False))


user_input = input("Is it time to start the Round of 32? Type any letter to start.")

advancedTeams = []

group_index = [0, 1, 2, 4, 5, 6, 7, 10]
for group in groups.values():
  genericteams = [
    group.team1,
    group.team2,
    group.team3,
    group.team4
  ]

  teams_sorted = sorted(genericteams, key=lambda t: t.points, reverse=True)

  top1 = advancedTeams.append(teams_sorted[0])
  top2 = advancedTeams.append(teams_sorted[1])
  for i in group_index:
    if list(groups.values())[i] == group:
      top3 = advancedTeams.append(teams_sorted[2])

print()
print("Here are the teams that have advanced to the Round of 32:")
for team in advancedTeams:
  print(team.name)

user_input = input("Type any letter to start.")
stages = 0
while stages < 5:
  random.shuffle(advancedTeams)
  matches.clear()
  matches = [Match("","",0,0,"") for i in range(int(len(advancedTeams) / 2))]

  for i, match in enumerate(matches):
    team_index = i * 2
    match.team_a = advancedTeams[team_index]
    match.team_b = advancedTeams[team_index+1]
    print(match.team_a.name + " - "+ match.team_b.name)

  advancedTeams.clear()

  for match in matches:
    print(match.team_a.name+" - "+match.team_b.name)
    sim.simulate_match(match, match.team_a, match.team_b)
    print(match.team_a_goals,"-",match.team_b_goals)
    if match.team_a_goals > match.team_b_goals:
      match.result = match.team_a.name
      advancedTeams.append(match.team_a)
    elif match.team_b_goals > match.team_a_goals:
      match.result = match.team_b.name
      advancedTeams.append(match.team_b)
    elif match.team_a_goals == match.team_b_goals:
      winner = random.choice([match.team_a, match.team_b])
      match.result = winner.name
      advancedTeams.append(winner)
    print(match.result)

  stages += 1
  if (stages == 1):
    user_input = input("Is it time to move on to the Round of 16? Type any letter to start.")
  elif (stages == 2):
    user_input = input("Is it time to move on to the Quarter Finals? Type any letter to start.")
  elif (stages == 3):
    user_input = input("Is it time to move on to the Semi Finals? Type any letter to start.")
  elif (stages == 4):
    user_input = input("Is it time to move on to the Finals? Type any letter to start.")
  print()
  print("Here are the teams that have advanced:")
  for team in advancedTeams:
    print(team.name)
  user_input = input("Type any letter to start.")
  if (stages == 5):
    print()
    print("And the Champions of the world is "+match.result+"!")
