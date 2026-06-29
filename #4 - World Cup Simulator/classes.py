class Team:
  def __init__(self, name, attack, midfield, defense, rating, points, pressure, goals):
    self.name = name
    self.attack = attack
    self.midfield = midfield
    self.defense = defense
    self.rating = rating
    self.points = points
    self.pressure = pressure
    self.goals = goals

class Group:
  def __init__(self, team1, team2, team3, team4):
    self.team1 = team1
    self.team2 = team2
    self.team3 = team3
    self.team4 = team4
    
class Match:
  def __init__(self, team_a, team_b, team_a_goals, team_b_goals, result):
    self.team_a = team_a
    self.team_b = team_b
    self.team_a_goals = team_a_goals
    self.team_b_goals = team_b_goals
