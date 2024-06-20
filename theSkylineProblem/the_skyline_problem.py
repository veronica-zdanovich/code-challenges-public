from queue import PriorityQueue
from typing import List


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        intersections = list()
        events = list()

        for index, building in enumerate(buildings):
            events.append((building[0], building[2], 0, index))
            events.append((building[1], building[2], 1, index))

        events = sorted(events, key=lambda x: (x[0], x[2], -x[1] if x[2] == 0 else x[1]))

        height_heap = PriorityQueue()
        height_heap.put((0, -1))
        active_set = {-1}

        for event in events:
            x, y, event_type, index = event
            if event_type == 0:
                active_set.add(index)
            else:
                active_set.remove(index)

            queue_head = height_heap.queue[0]
            if event_type == 0:
                if y > -queue_head[0]:
                    intersections.append([x, y])
                height_heap.put((-y, index))
            else:
                if y == -queue_head[0]:
                    while not height_heap.empty() and height_heap.queue[0][1] not in active_set:
                        height_heap.get()
                queue_head = height_heap.queue[0]
                if -queue_head[0] != intersections[-1][1]:
                    intersections.append([x, -queue_head[0]])

        return intersections
