import collections as co
st=co.deque()
print(st)
import queue as q
s=q.LifoQueue(4)#it tells max size
s.put(1)
s.put(3)
s.put(5,timeout=10)
print(s.get(),s.get(),s.get(),s.get())


