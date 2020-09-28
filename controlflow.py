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
   print(b)
   i+=1