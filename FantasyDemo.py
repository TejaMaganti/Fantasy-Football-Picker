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
    elif pos == "K":
        K.append(name)
print(QB)
print(RB)
print(WR)
print(K)


game = nflgame.games(2017, 14)
players = nflgame.combine(game)
wentz = players.name(QB[0])
bell =  players.name(RB[0])
hopkins = players.name(WR[0])
Elliot = players.name(K[0])

qb = FantasyScore.QB(wentz, wentz.passing_yds, wentz.passing_ints, wentz.passing_tds, wentz.passing_twoptm, wentz.rushing_yds, wentz.rushing_tds)
rb = FantasyScore.RB(bell, bell.rushing_yds, bell.rushing_tds, bell.rushing_twoptm, bell.receiving_yds, bell.receiving_tds )
wr = FantasyScore.WR(hopkins, hopkins.receiving_yds, hopkins.receiving_tds, hopkins.fumbles_lost, hopkins.receiving_twoptm)
qb.QBScore()
rb.RBScore()
wr.WRScore()

#game = nflgame.one(2017, 14, "LA", "PHI")
#wentz = game.players.name("C.Wentz")
#fantasy_score = wentz.passing_yds * 0.04
#print(fantasy_score)
#print(game.players.passing())
