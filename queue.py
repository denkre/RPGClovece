# Fronta (queue)


# Queue(memory) - konstruktor
# enqueue(item) - prida prvek na konec fronty
# dequeue(item) - odebere prvek z fronty
# front() - kdo je na rade?
# back() - kdo je posledni?
# is_empty() - je fronta prazdna?
# size() - kolik je prvku ve fronte?


class Queue:
    def __init__(self, memory, items=None):
        self._memory = memory
        self._items = []
        if items:
            if len(items) > memory:
                raise Exception('Items count bigger then allocated memory!')
            for i in items:
                self._items.append(i)

    def enqueue(self, item):
        if self._memory_available() > 0:
            self._items.append(item)
        else:
            print(f"Queue is full. Item ${item}$ wasn't enqueued!")

    def dequeue(self):
        if not self._is_empty():
            return self._items.pop(0)
        else:
            print("Queue es empty. No item was dequeued!")

    def sort(self):
        # Insertion sort
        for i in range(1, self._size()):
            tmp = self._items[i]
            j = i-1
            while j >= 0 and self._items[j].priority < tmp.priority:
                self._items[j + 1] == self._items[j]
                j -= 1
            self._items[j + i] = tmp

    def front(self):
        if not self._is_empty():
            return self._items[0]
        else:
            print("Queue es empty. No item in front!")

    def back(self):
        if not self._is_empty():
            return self._items[-1]
        else:
            print("Queue es empty. No item in back!")

    def _memory_available(self):
        return self._memory - self._size()

    def _size(self):
        return len(self._items)

    def _is_empty(self):
        return self._size == 0

    def __str__(self):
        return str(self._items)

    def __iter__(self):
        self.iter_index = 0
        return self

    def __next__(self):
        if(self.iter_index >= self._size()):
            raise StopIteration
        self.iter_index += 1
        return self._items[self.iter_index-1]


def main():
    fronticka = Queue(5, [0, 5])
    print(fronticka)
    fronticka.enqueue("Alena")
    fronticka.enqueue(True)
    fronticka.enqueue(0)
    fronticka.enqueue("Pavel")
    fronticka.enqueue(5.6)
    print(fronticka)
    fronticka.dequeue()
    fronticka.dequeue()
    print(fronticka)
    print(fronticka.front())
    print(fronticka.back())


if __name__ == "__main__":
    main()