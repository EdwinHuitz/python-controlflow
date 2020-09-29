#1
def sum_to(num):
   a=0
   b=0
   while a<num:
      a+=1
      b+=a
   print(b)
sum_to(6)
#2
def largest(arr):
   s = sorted(arr)
   return(s[len(s)-1])
print(largest([1,12,3,24,5,36,71,21,43]))
#3
import re
def occurances(a,b):
   total = re.findall(b,a)
   print(len(total))
occurances('ababababa','a')
#4
def products(*args):
   a = 0
   b = 1
   for arg in args:
      a=int(arg)
      b=b*arg
   print(b)
products(1,2,3,4,5,6)