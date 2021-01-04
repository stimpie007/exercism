from operator import attrgetter


class Team:
    def __init__(self, team):
        self.name = team
        self.played = 0
        self.win = 0
        self.draw = 0
        self.loss = 0
        self.points = 0

    def score(self, result):
        if result == "win":
            self.won()
        elif result == "loss":
            self.lost()
        elif result == "draw":
            self.tied()
        else:
            raise ValueError("Only 'win', 'loss' or 'draw' values are allowed")

    def won(self):
        self.played += 1
        self.win += 1
        self.points += 3

    def lost(self):
        self.played += 1
        self.loss += 1

    def tied(self):
        self.played += 1
        self.draw += 1
        self.points += 1


def create_table(teams):
    table = ["Team                           | MP |  W |  D |  L |  P"]
    name_sorted = sorted(teams.values(), key=attrgetter('name'))
    points_sorted = sorted(name_sorted, key=attrgetter('points'), reverse=True)
    for team in points_sorted:
        table.append(team.name.ljust(31) + '|  ' + ' |  '.join(
            str(team.played) +
            str(team.win) +
            str(team.draw) +
            str(team.loss) +
            str(team.points)
        ))
    return table


def tally(rows):
    teams = dict()
    outcome_mapping = {
        "team1": "team2",
        "win": "loss",
        "loss": "win",
        "draw": "draw"
    }

    for row in rows:
        team1, team2, outcome = row.split(';')

        if team1 not in teams:
            teams[team1] = Team(team1)
        if team2 not in teams:
            teams[team2] = Team(team2)

        teams[team1].score(outcome)
        teams[team2].score(outcome_mapping[outcome])

    return create_table(teams)
