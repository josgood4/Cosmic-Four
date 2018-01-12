import inflect

def countLets(s):
  count = 0
  for i in range(len(s)):
    if(s[i]!='-' and s[i]!=' '):
      count += 1
  return count

eng = inflect.engine()
print(eng.number_to_words(99))
print(countLets(eng.number_to_words(99)))
