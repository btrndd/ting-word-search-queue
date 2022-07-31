class Queue:
    def __init__(self):
        self._data = list()

    def __len__(self):
        return len(self._data)

    def enqueue(self, value):
        self._data.append(value)

    def dequeue(self):
        return self._data.pop(0)

    def search(self, index):
        if (index > self.__len__() - 1 or index < 0):
            raise IndexError()
        else:
            return self._data[index]
