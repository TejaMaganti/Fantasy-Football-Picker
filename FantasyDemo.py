import nflgame
import FantasyScore

QB = []
RB = []
WR = []
DEF = []
K = []

f = open("players.txt", "r")
for line in open("players.txt"):
    first, last, pos = line.strip().split(',')
    name = first[:1] + "." +last
    if pos == "QB":
        QB.append(name)
    elif pos == "RB":
        RB.append(name)
    elif pos == "WR":
        WR.append(name)
print(QB)
print(RB)

game = nflgame.games(2017, 14)
qb = nflgame.combine(game)
wentz = qb.name(QB[0])
bell =  qb.name(RB[0])
qb1 = FantasyScore.QB(wentz, wentz.passing_yds, wentz.passing_ints, wentz.passing_tds, wentz.passing_twoptm,
                      wentz.rushing_yds, wentz.rushing_tds)
rb = FantasyScore.RB(bell, bell.rushing_yds, bell.rushing_tds, bell.rushing_twoptm, bell.receiving_yds,
                     bell.receiving_tds )
qb1.QBScore()
rb.RBScore()
#game = nflgame.one(2017, 14, "LA", "PHI")
#wentz = game.players.name("C.Wentz")
#fantasy_score = wentz.passing_yds * 0.04
#print(fantasy_score)
#print(game.players.passing())
