

class QB:
    def __init__(self, name, yards, pick, td, ept,rush, rushtd):
        self.name = name
        self.yards = yards
        self.pick = pick
        self.td = td
        self.ept = ept
        self.rush = rush
        self.rushtd = rushtd

    def QBScore(self):
        fyards = self.yards * 0.04
        fint = self.pick * -2
        ftd = self.td * 4
        f2pt = self.ept * 2
        rush = self.rush * 0.1
        rushtd = self.rushtd * 6
        fscore = fyards + fint + ftd + f2pt + rush + rushtd
        print(fscore)

class RB:
    def __init__(self, name, rushyards, rushtd, ept, recyards, rectd):
        self.name =  name
        self.rushyards = rushyards
        self.rushtd = rushtd
        self.ept = ept
        self.recyards = recyards
        self.rectd = rectd

    def RBScore(self):
        fyards = self.rushyards * 0.1
        ftd = self.rushtd * 6
        fept = self.ept * 2
        frecyd = self.recyards * 0.1
        frectd = self.rectd * 6
        fscore = fyards + ftd + fept + frecyd + frectd
        print(fscore)