
import random
import teamPackage.Player

class FieldSquare(object):
 def __init__(self,ball,position):	
  self.hasBall = setHasBall(ball)
  self.key = setKey(position, 10)
  self.playerSpace = []
  Player.fielder = fielder
       
 def setSize(self,size):
       self.playerSpace = [0]*size

 def getHasBall(self):
       return self.hasBall

 def setHasBall(self, HasBall):
       self.hasBall = HasBall

 def getKey(self):
       return self.key

 def setKey(self,Key,Size):
       self.key = Key
       self.size = Size
       setSize(self.size)

 def  getFielder(Player):
       return Player.fielder

 def setFielder(Fielder):
       Player.fielder = Fielder
       for i in range(0, len(playerSpace)):
           if i < 50:
               playerSpace[i] = (int)(fielder.getFP()*100) - (i)
           else:
               playerSpace[i] = 60
               #playerSpace[i] = 60;
	
def wasBallCaught():
       temp = (int)(Math.random() * (len(playerSpace)-1))
       temp2 = (int)(Math.random() * 100)
       print "chance " + (100 - playerSpace[temp]) + " random num " + temp2
       if temp2 > (100 - playerSpace[temp]):
           print "BALL HAS BEEN CAUGHT OUT"
           return true
       else:
           return false


