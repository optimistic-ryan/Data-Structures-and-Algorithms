class FenwickTree:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (size + 1)

    def _least_significant_bit(self, i):
        return i & -i

    def update(self, index, value):
        while index <= self.size:
            self.tree[index] += value
            index += self._least_significant_bit(index)

    def query(self, index):
        result = 0
        while index:
            result += self.tree[index]
            index -= self._least_significant_bit(index)
        return result

    def range_query(self, left, right):
        return self.query(right) - self.query(left - 1)


