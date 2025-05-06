import heapq as hq
import sys


pq=[]
for _ in range(int(sys.stdin.readline())):
    x = int(sys.stdin.readline())
    if x: 
        hq.heappush(pq, (abs(x), x))
    else:   # x == 0
        if pq:
            print(hq.heappop(pq)[1])
        else:
            print(0)
