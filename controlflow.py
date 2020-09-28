#01-Letter check
letter = str(input('Enter a letter: ').lower())
vowels = 'aeiou'
def checking():
   ans = False
   if len(letter) < 2 and letter.isalpha() == True:
      for v in vowels:
         if letter == v: ans = True
   if ans == True:print(f'The letter {letter} is a vowel')
   else:print(f'The letter {letter} is a consonant')
   return True

x=False
while x != True:
   x=checking()

#02-Length of Phrase
def entering():
   phrase = str(input('Enter a phrase: ').lower())
   if phrase.isalpha()==True:
      leng = len(phrase)
      if leng>0 and phrase!= 'quit':print(f'What you entered {phrase} is {leng} characters long')
      else:return True

x=False
while x !=True:
   x=entering()

#03-Calculate Dog Years
def aging():
   a = input('Input your dog\'s age in human years: ')
   if len(a)>0 and a.isdigit() == True:
      age = int(a)
      ans = 0
      i=0
      while i < age:
         if i < 2:
            ans += 10
            i += 1
         else:
            while i < age:
               ans += 7
               i += 1
   print(ans)
   return True
          
b=False
while b !=True:
    b=aging()

#04-What Kind of Triangle
def findTri():
   a=input('Input the first Number: ')
   b=input('Input the second Number: ')
   c=input('Input the third Number: ')
   if a.isdigit() == True:
      print('Yes!')
   if a == b and b == c:
      print('You entered an equilateral triangle')
      return True
   elif a == b and b != c:
      print('you entered an isosceles triangle')
      return True
   elif a != b and a != c and b != c:
      print('you entered a scalene triangle')
      return True
   
x=False
while x != True:
   x=findTri()

#05-Fibonacci Sequence
i=0
goal=49
a=0;
b=1;
c=0;
while i < goal:
   c=a+b
   a=b
   b=c
   print(f'term:{i} / number:{b}')
   i+=1
#06-Seasons
ms=('jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec')
month=str(input('Enter the month as three characters: '))
day=int(input('Enter the day of that month: '))
for m in ms:
   if month ==m:
      if m == ms[0]:print(f'January {day} is in Winter')
      if m == ms[1]:print(f'February {day} is in Winter')
      if m == ms[2] and day<= 19:print(f'March {day} is in Winter')
      elif m == ms[2] and day>= 20:print(f'March {day} is in Spring')
      if m == ms[3]:print(f'April {day} is in Spring')
      if m == ms[4]:print(f'May {day} is in Spring')
      if m == ms[5] and day<=20:print(f'June {day} is in Spring')
      elif m == ms[5] and day>=21:print(f'June {day} is in Summer')
      if m == ms[6]:print(f'July {day} is in Summer')
      if m == ms[7]:print(f'August {day} is in Summer')
      if m == ms[8] and day<=21:print(f'September {day} is in Summer')
      elif m == ms[8] and day>=22:print(f'September {day} is in Fall')
      if m == ms[9]:print(f'October {day} is in Fall')
      if m == ms[10]:print(f'November {day} is in Fall')
      if m == ms[11] and day<=20:print(f'December {day} is in Fall')
      elif m == ms[11] and day>=21:print(f'December {day} is in Winter')