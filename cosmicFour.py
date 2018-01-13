import inflect

eng = inflect.engine()

def countLets(s):
  count = 0
  for i in range(len(s)):
    if(s[i]!='-' and s[i]!=' ' and s[i]!=','):
      count += 1
  return count

def cosmicFour(num):
  if num==4:
    print("...and 4 is cosmic")
    return None
  s = eng.number_to_words(num, andword='')
  ##print(s)
  next = countLets(s)
  print(str(num) + " goes to " + str(next))
  return cosmicFour(next)
  
##print(eng.number_to_words(99))
##print(countLets(eng.number_to_words(99)))

for i in range(1000000):
  cosmicFour(i)
