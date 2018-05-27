import math

print("1,1,2,3,5,8,13,21,34,55,89,144")



fibonacci = []
fibonacci.append(1)
fibonacci.append(1)

for i in range(1,20):
    #print(str(i) + "\t" + str(math.log(3, math.pow(3,i))))
    fibonacci.append(fibonacci[len(fibonacci) - 1] + fibonacci[len(fibonacci) - 2])

for item in fibonacci:
    print(item)
