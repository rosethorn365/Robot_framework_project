def isReferenceNumberCorrect(referencenumber):

  listedRefNumber = list(referencenumber)

  #print(listedRefNumber)
  checknumber = listedRefNumber.pop()
  totalAmount = 0
  product = 1

  while (len(listedRefNumber) > 0):
      if (product == 1):
         product = 7
         totalAmount = totalAmount + (product * int(listedRefNumber.pop()))
      elif (product == 3):
         product = 1
         totalAmount = totalAmount + (product * int(listedRefNumber.pop()))
      else:
         product = 3
         totalAmount = totalAmount + (product * int(listedRefNumber.pop()))

  # print(totalAmount)
  result = (10 - (totalAmount % 10) % 10)

  if ( result == int(checknumber)):
     
     return True


  return False

def isEqual(headerTotal, rowTotal, maxDifference):
   
   if ( abs(headerTotal-rowTotal) < maxDifference ):
       return True
   return False



if __name__ == "__main__":
  ref = '1531439'
  val = isReferenceNumberCorrect(ref)
  print(val)