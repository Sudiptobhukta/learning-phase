from stackintro import stack
s = stack()
s.push(14)
s.push(15)
s.push(20)
s.push(45)

while s.isEmpty is False:
    print(s.pop())


s.top()