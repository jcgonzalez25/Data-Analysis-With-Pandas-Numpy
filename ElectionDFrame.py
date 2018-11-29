import pandas as pd
import numpy as np
import sqlite3
def getElectionDFrame():
  dbPath     = "/u1/junk/cs617/Data/election.db"
  connection = sqlite3.connect(dbPath)
  df         = pd.read_sql_query("select * from votes",connection)
  df         = df.drop('index',axis=1)
  connection.close()
  return df

class ElectionDFrame:
  def __init__(self):
    self.df       = getElectionDFrame()
    self.numpy    = self.df.values
    self.allPolls = self.numpy.reshape(9,87)
    self.columns  = self.df.columns[1:]
    self.nanPairs =[]
  def findEmptyVotes(self):
    nanPairs = []
    for poll_info in self.allPolls:
      for index,canidate_votes in enumerate(poll_info):
        if index == 0:
          canidate_name = canidate_votes
          continue
        if np.isnan(canidate_votes):
            pair = [canidate_name,self.columns[index-1]]
            nanPairs.append(pair)
    self.nanPairs = nanPairs
  def printPairs(self):
    print(self.nanPairs)
