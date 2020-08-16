import traceback

from collections import deque

try:
    tul = (1,2,3,4,'a')
    print(type(tul))
    print(tul)
    tul[1] = 6
    print(tul)

except Exception as e:
    traceback.print_exc()
    print(e)

try:
    list = [1,2,3,4]
    print(type(list))
    print(list)
    list[1] = 6
    print(list)
except Exception as e:
    traceback.print_exc()
    print(e)

try:
    d = deque()
    d.append('a')
    d.append(1)
    d.append(2)
    print(d)

except Exception as e:
    traceback.print_exc()
    print(e)

