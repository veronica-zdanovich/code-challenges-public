class MinStack:

    def __init__(self):
        self.inner_list = list()
        self.value_prev_min_map = dict()

        self.duplicates = dict()
        self.min_item = None

    def push(self, val: int) -> None:
        self.inner_list.append(val)
        if self.value_prev_min_map.get(val) is not None:
            self.duplicates[val] = self.min_item
        else:
            self.value_prev_min_map[val] = self.min_item if self.min_item is not None else val
        self.min_item = min(self.min_item, val) if self.min_item is not None else val

    def pop(self) -> None:
        val = self.inner_list.pop()
        if self.duplicates.get(val) is not None:
            del self.duplicates[val]
        else:
            self.min_item = self.value_prev_min_map[val]
            del self.value_prev_min_map[val]
        if len(self.inner_list) == 0:
            self.min_item = None

    def top(self) -> int:
        return self.inner_list[-1]

    def getMin(self) -> int:
        return self.min_item
