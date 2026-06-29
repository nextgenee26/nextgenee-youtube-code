import math
import random
import pandas
from classes import Match

def FindPressure(team, data):
  wcwinfactor = 0.50 * (data.loc[data['Country'] == team.name, 'WorldCupWins'].iloc[0] / 5)
  capfactor = 0.10 * (data.loc[data['Country'] == team.name, 'Caps'].iloc[0] / 23)
  stagefactor = 0.40 * (data.loc[data['Country'] == team.name, 'HighestStage'].iloc[0] / 7)
  popularity = 0.7 * (wcwinfactor + capfactor + stagefactor)

  rank = 0.3 * (212 - (data.loc[data['Country'] == team.name, 'Rank'].iloc[0])) / 211

  pressure = max(0.0, min(1.0, popularity + rank))
  return pressure

def initTeam(team, index, data):
  team.name = data.loc[index, 'Country']
  team.attack = data.loc[index, 'Attack']
  team.midfield = data.loc[index, 'Midfield']
  team.defense = data.loc[index, 'Defense']
  team.rating = data.loc[index, 'Rating']
  team.points = 0
  team.goals = 0
  team.pressure = FindPressure(team, data)

def expected_goals(team_a,team_b):

    attack_strength = team_a.attack
    defense_strength = team_b.defense

    exp = (attack_strength - defense_strength) / 13

    exp += team_a.rating / 300

    return max(0.4,exp)

def poisson(lam):
    L = math.exp(-lam)
    k = 0
    p = 1

    while p > L:
        k += 1
        p *= random.random()

    return k - 1

def simulate_match(match, team_a, team_b):
  exp_a = expected_goals(team_a,team_b)
  exp_b = expected_goals(team_b,team_a)

  noise_a = 1.0 + team_a.pressure * 0.5
  noise_b = 1.0 + team_b.pressure * 0.5

  exp_a *= random.uniform(0.92,1.15)
  exp_b *= random.uniform(0.92,1.15)

  goals_a = min(poisson(exp_a * noise_a),6)
  goals_b = min(poisson(exp_b * noise_b),6)

  match.team_a_goals = goals_a
  match.team_b_goals = goals_b

