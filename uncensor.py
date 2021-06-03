'''
A Code, which i wrote for a edabit challenge. I am pretty proud of it, so i saved it
It basically takes a string which has every vowel censored by an "*"
Then it takes a string containing all the missing vowels
The written Function replaces the "*"s with the correct vowel.

'''

def uncensor(txt, vowels):
  # filling lst which is a list containing every letter in txt
  lst = []
  for letter in txt:
    lst.append(letter)
      
  l = []
  for vowel in vowels:
    l.append(vowel)
  
  for i in range(len(lst)):
    if lst[i] == '*':
      lst[i] = l[0]
      l.remove(l[0])

  txt = ""
  for letter in lst:
      txt += letter
  return txt


# running the code
print(uncensor("Wh*r* d*d my v*w*ls g*?", "eeioeo"))
print(uncensor("*PP*RC*S*", "UEAE"))
