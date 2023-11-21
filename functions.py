# TASK: Update both functions to reverse the letters in the name and provide the square root of the users age.

# Returns a string that is the contents of the myName variable written backwards
# ie: passing Atkinson as the parameter would return nosniktA
def reverseName(myName):
  # start with nothing
  result = ''
  # put the position finder at the end of the string
  pos = len(myName) - 1
  # loop backwards
  while pos >= 0:
    result = result + myName[pos]
    pos = pos - 1
  
  return result

# Returns a float value that is the contents of the myAge variable square rooted
# ie: passing 16 as the parameter would return 4.0
def rootAge(myAge):
  # import python math
  import math
  # make sure the number is a number
  ageToSqrt = float(myAge)
  # get the square root
  result = math.sqrt(ageToSqrt)
  return result
