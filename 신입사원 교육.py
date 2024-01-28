#최소힙
import heapq

def solution(ability, number):
    heapq.heapify(ability) 

    for i in range(number):
        x = heapq.heappop(ability)
        y = heapq.heappop(ability)
        heapq.heappush(ability, x + y)
        heapq.heappush(ability, x + y)

    return sum(ability)

#우선순위 큐
import queue

def solution(ability, number):
    pq = queue.PriorityQueue()

    for n in ability:
        pq.put(n)

    for i in range(number):
        x = pq.get()
        y = pq.get()
        pq.put(x + y)
        pq.put(x + y)

    result = 0
    while not pq.empty():
        result += pq.get()

    return result
