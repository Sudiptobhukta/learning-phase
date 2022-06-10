
from multiprocessing import Process

def sq(n):
    print(n**2)

ary =[]
for i in range(4):
    ary.append(Process(target=sq, args=(i+1,)))

for j in ary:
    j.start()
print("Hello")