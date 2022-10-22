from __future__ import division
import random

Random=[]
for i in range (10000): #range can be changed
    Random.append(random.randrange(1, 101, 1))
print (Random)

max_value = max(Random)
min_value = min(Random)
avg_value = sum(Random)/len(Random)

print("Max value=",max_value,"Min value=",min_value,"Avg value=",avg_value)

def bubbleSort(Random):
    for passnum in range(len(Random)-1,0,-1):
        for i in range(passnum):
            if Random[i]>Random[i+1]:
                temp = Random[i]
                Random[i] = Random[i+1]
                Random[i+1] = temp
bubbleSort(Random)
print(Random)
