import pandas as pd
class StudentDFrame:
  def __init__(self,csvFile):
    self.filePath  = csvFile
    self.DataFrame = pd.read_table(self.filePath,sep=",")
  def handleMissing(self,fillIn):
    self.DataFrame = self.DataFrame.fillna(fillIn)
  def addTotal(self):
    addQuizes = lambda row:row.quiz1 + row.quiz2 + row.quiz3 + row.quiz4
    self.DataFrame['total'] = self.DataFrame.apply(addQuizes,axis=1)
  def printUpdated(self):
    print(self.DataFrame)
