import nflgame


class fantasyqb:
    def __init__(self, name, yards, pick, td, ept,rush, rushtd):
        self.name = name
        self.yards = yards
        self.pick = pick
        self.td = td
        self.ept = ept
        self.rush = rush
        self.rushtd = rushtd

    def func(self):
        fyards = self.yards * 0.04
        fint = self.pick * -2
        ftd = self.td * 4
        f2pt = self.ept * 2
        rush = self.rush * 0.1
        rushtd = self.rushtd * 6
        fscore = fyards + fint + ftd + f2pt + rush + rushtd
        print(fscore)


f = open("players.txt", "r")
for line in open("players.txt"):
    first, last, pos = line.strip().split(',')
    name = first[:1] + "." +last
    print(name)
    if pos == "QB":
      QB = [name]
#    elif pos == "RB":
#       RB = [name]
#    print(QB)
    #print(RB)

game = nflgame.games(2017, 14)
qb = nflgame.combine(game)
wentz = qb.name(QB[0])
qb = fantasyqb(wentz, wentz.passing_yds, wentz.passing_ints, wentz.passing_tds, wentz.passing_twoptm, wentz.rushing_yds, wentz.rushing_tds)
qb.func()

#game = nflgame.one(2017, 14, "LA", "PHI")
#wentz = game.players.name("C.Wentz")
#fantasy_score = wentz.passing_yds * 0.04
#print(fantasy_score)
#print(game.players.passing())
