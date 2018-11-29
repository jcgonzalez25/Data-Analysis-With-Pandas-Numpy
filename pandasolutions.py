from StudentDFrame  import StudentDFrame
from ElectionDFrame import ElectionDFrame
from CountyDFrame   import CountyDFrame
from Logger import Logger
class Questions:
  def first():
    Students = StudentDFrame("/u1/junk/cs617/Data/b1.csv")
    Students.handleMissing(0)
    Students.addTotal()
    Students.printUpdated()
  def second():
    Logs = Logger()
    Logs.createUserDataframe()
    Logs.createLoginDataframe()
    Logs.printBoth()
  def third():
    Elections = ElectionDFrame()
    Elections.findEmptyVotes()
    Elections.printPairs()
  def fourth():
    C = CountyDFrame()
    C.changeTable()


if __name__ == "__main__":
  Questions.first()
  Questions.second()
  Questions.third()
  Questions.fourth()
