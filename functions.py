# TASK: Update both functions to reverse the letters in the name and provide the square root of the users age.

# Returns a string that is the contents of the myName variable written backwards
# ie: passing Atkinson as the parameter would return nosniktA
def reverseName(myName):
    # start with nothing
  result = ''
  # validate
  if len(myName) <= 0 or myName == '':
    return result

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
    # import python math and numbers
  import math

  result = 0.0
  # validate
  if len(myAge) <= 0 or myAge == '':
    return result
  
  # make sure the number is a number
  ageToSqrt = float(myAge)
  if ageToSqrt <= 0:
    return result
  
  # get the square root
  result = math.sqrt(ageToSqrt)
  return result
