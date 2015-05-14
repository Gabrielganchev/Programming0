__author__ = 'ganchev'
class BowlingGame:
    def __init__(self):
        self.rolls = []
    def roll(self,pin):
        self.rolls.append(pin)
    def score(self):
        result = 0
        rollIndex =0
        for frameindex in range(10):
            if self.isStrike(rollIndex):
                result +=self.strikeScore(rollIndex)
                rollIndex +=1
            elif self.isSpare(rollIndex):
                result +=self.spareScore(rollIndex)
                rollIndex+=2
            else:
                result +=self.spareScore(rollIndex)
                rollIndex+=2
        return result
    def isSpare(self,rollIndex):
        return self.rolls[rollIndex]+self.rolls[rollIndex+1]==10

    def spareScore(self,rollIndex):
        return 10 + self.roll(rollIndex +2)
    def frameScore(self,rollIndex):
        return self.rolls(rollIndex) + self.roll(rollIndex +1)

