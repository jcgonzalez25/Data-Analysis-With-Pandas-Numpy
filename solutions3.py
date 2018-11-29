import numpy as np

if __name__ == "__main__":
  z = np.zeros((10,))
  print(z)
  threes = np.array([ 3 for i in range(10)])
  print(threes)
  l = np.array([i for i in range(1,26)])
  print(l)
  new = l.reshape(5,5)
  print(new)
  sorted1 = new[::-1]
  print(sorted1)
  print("dont understand 8")
  print("dont understand 9")
  print("dont understand 10")
  ones = np.ones(8).reshape(8,1)
  zeros = np.array([2 for i in range(8)]).reshape(8,1)
  cBoard = np.concatenate((ones,zeros,ones,zeros,ones,zeros,ones,zeros),axis=1)
  print(cBoard)
  A = np.array([3 for i in range(12)]).reshape(3,4)
  B = np.array([2 * 3 for i in range(20)]).reshape(4,5)
  print(B)
  #ones  = np.ones(8).reshape(10,1)
  #zeros = np.array([1 if i == 0 or i == 9 else 0 for i in range(10)]).reshape
