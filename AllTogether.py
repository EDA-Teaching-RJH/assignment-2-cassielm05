### Part Four -- your code goes here. 
import random

numlist = []

for x in range(10):
    numlist.append(random.randint(1,100))

print(numlist)

count = 0
while count < len(numlist):
   if numlist[count] % 2 == 0:
        numlist.pop(count)
   else:
    count +=1

print(numlist)
   
