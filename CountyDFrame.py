from ElectionDFrame import getElectionDFrame
import pandas as pd
import numpy as np
class CountyDFrame:
  def __init__(self):
    dbPath = "/u1/junk/cs617/Data/election.db"
    self.Election = getElectionDFrame().fillna(0)

  def changeTable(self):
    self.Election['total'] = self.Election.iloc[:,1:].apply(np.sum,axis=1)
    self.Election          = self.Election.transpose()
    self.Election.columns  = self.Election.iloc[0]
    self.Election          = self.Election.drop("Candidate").astype('int64')
    self.findWinner()
    self.export_to_html()
  def findWinner(self):
    candidatesWinTotal = {candidate:0 for candidate in self.Election.columns.values}
    winners = self.Election.iloc[:-1].apply(lambda x: x.nlargest(1).index[0] ,axis=1).values
    print(self.Election.iloc[:-1,1])
    for winner in winners:
      candidatesWinTotal[winner]+=1
    print("Winner")
    print(pd.Series(candidatesWinTotal).nlargest(1))
  def export_to_html(self):
    f = open("election.html",'w')
    f.write(self.Election.to_html())
    f.close()
