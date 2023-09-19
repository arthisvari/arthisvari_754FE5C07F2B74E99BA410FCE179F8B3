#Implement a class called player that represents a cricket player.The player class should have a method called play() which prints"The player is playing cricket. Derived two classes, Batsman and Bowler,from the player class. Override the play() method in each derived class to print "The batsman is batting" and "The bowler is bowling",respectively. Write a program to creat objects of both the Batsman ana Bowler classes and call the play() method for each objects.

#Define the base class player
class Player:
  def play(self):
    print("The player is playing cricket")

#Define the derived class batsman
class Batsman(Player):
  def play(self):
    print("The batsman is batting")

#Define the derived class bowler
class Bowler(Player):
  def play(self):
    print("The bowler is bowling")

#Create objects of batsman and bowler
batsman=Batsman()
bowler=Bowler()

#Call the play() method
batsman.play()
bowler.play()
