from stackintro import stackcheck

s = stackcheck()
s.push(34)
s.push(53)
s.push(12)
while s.isEmpty() is False:
    print(s.pop())
s.top()