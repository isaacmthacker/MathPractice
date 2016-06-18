import random
import time

def add(first, second):
  return first+second
def sub(first, second):
  return first-second
def mult(first, second):
  return first*second

operations = {
 '+' : add,
 '-' : sub,
 '*' : mult
}
opSymbols = ['+', '-', '*']
maxLevel = 10
maxTime = 4
levelMaxForRand = [0]
for level in range(1,maxLevel+1):
  levelMaxForRand.append(level*10)

class Problem:
  def __init__(self, firstNum, secondNum, op):
    self.first = firstNum
    self.second = secondNum
    self.opChar = op
    self.operation = operations[op]
    self.result = self.operation(self.first, self.second)
    self.correct = False
    self.startTime = time.time()
    self.endTime = 0

  def checkAnswer(self, valueToCheck):
    self.correct = self.result == valueToCheck
    self.endTime = time.time()-self.startTime
  
  def __str__(self):
    maxNumLength = len(str(levelMaxForRand[maxLevel]*levelMaxForRand[maxLevel]))+1
    retString = str(self.first) + (" "*(maxNumLength-len(str(self.first))))
    retString += " " + self.opChar + " " 
    retString += str(self.second) + (" "*(maxNumLength-len(str(self.second))))
    retString += " = " 
    retString += str(self.result) + (" "*(maxNumLength-len(str(self.result)))) 
    retString += ' : '
    if(self.correct):
      retString += '\033[92mCORRECT  \033[0m'
    else:
      retString += '\033[91mINCORRECT\033[0m'
    if(self.endTime > maxTime):
      retString += '\033[93m'
      retString += ' : %.2fs' % self.endTime
      retString += '\033[0m'
    else:
      retString += ' : %.2fs' % self.endTime
    return retString



numOfProblems = int(raw_input("How many problems?\n"))
level = levelMaxForRand[int(raw_input("What level (1-" + str(maxLevel) + ")?\n"))]

problems = []
numOfCorrect = 0
for x in range(0,numOfProblems):
  op = opSymbols[random.randint(0,len(opSymbols)-1)]
  firstNum = random.randint(0,level)
  secondNum = random.randint(0,level)
  curProb = Problem(firstNum, secondNum, op)
  answer = raw_input(str(firstNum) + ' ' + op + ' ' + str(secondNum) + ' = ')
  curProb.checkAnswer(int(answer))
  if(curProb.correct):
    numOfCorrect += 1
  problems.append(curProb)
 
print "----RESULTS FOR LEVEL " + str(level) + "----"
print "Correct : " + str(numOfCorrect) + "/" + str(numOfProblems)
for problem in problems:
  print problem
score = 100*(float(numOfCorrect)/numOfProblems)
print "SCORE : %.2f" % score














