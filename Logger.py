import pandas as pd
import subprocess as ps
import re
class Cleaner:
  def __init__(self,filePath="",command=""):
    if filePath:
      self.fd    = open(filePath,"r")
      self.users = self.fd.read().split('\n')
      self.fd.close()
    else :
      commOutput = ps.check_output("lastlog")
      self.output = commOutput.decode("utf-8")
  def emptyGecos(self,fields):
    return bool(len(fields[4]) == 0)
  def getUsers(self):
    self.users.pop()
    parsedUsers = []
    for user in self.users:
      fields   = user.split(':')
      if self.emptyGecos(fields):
        continue
      uName    = fields[0]
      fullName = fields[4].split(',')[0]
      parsedUsers.append([uName,fullName])
    return parsedUsers

  def neverLoggedIn(self,userInfo):
    return bool(re.match(r".*Never logged in",userInfo))
  def getRelevantInfo(self,userInfo):
    fields    = userInfo.split()
    logInDate = [field + ' ' for field in fields[-6:]]
    logInDate = ''.join(logInDate)
    logInDate = pd.to_datetime(logInDate)
    fromHost  = ''.join(fields[-7:-6])
    userName  = fields[0]
    return [userName,logInDate,fromHost]
  def getLoginInfo(self):
    usersLogInfo = self.output.split('\n')
    usersLogInfo.pop(0)
    #key:username value:date logged in
    loginInfo = []
    for userInfo in usersLogInfo:
      if self.neverLoggedIn(userInfo) or len(userInfo) == 0:
        continue
      f = self.getRelevantInfo(userInfo)
      username  = f[0]
      loginDate = f[1]
      fromHost  = f[2]
      loginInfo.append([username,loginDate,fromHost])
    return loginInfo
class Logger:
  def __init__(self):
    #array of lists [uName , fullName] from passwd
    self.pwUsers         = Cleaner(filePath="/etc/passwd").getUsers()
    #dictionary - key=username value = [loginDate, fromHost]
    self.usersLoginInfo = Cleaner(command="lastLogIn").getLoginInfo()
    self.UsersDataFrame  = pd.DataFrame(columns=['login_name','real_name'])
    self.LoginDataFrame  = pd.DataFrame(columns=['login_name','login_date','login_host'])
  def createUserDataframe(self):
    for index,user in enumerate(self.pwUsers):
      self.UsersDataFrame.loc[index] = [user[0],user[1]]
  def createLoginDataframe(self):
    for index,user in enumerate(self.usersLoginInfo):
      self.LoginDataFrame.loc[index] = [user[0],user[1],user[2]]
    #self.LoginDataFrame.sort_values('login_date')
  def printBoth(self):
    both = self.UsersDataFrame.join(self.LoginDataFrame.set_index('login_name'),how='inner',on='login_name')
    print(both.sort_values('login_date'))
