class LinkedList:
    def __init__(self, collection=None):
        self.head = None
        if collection:
            for item in reversed(collection):
                self.insert(item)

    def __iter__(self):
        def value_generator():
            current = self.head
            while current:
                yield current.value 
                current = current.next
        return value_generator()

    def __str__(self):
        out = ""
        for value in self:
            out += f"[ {value} ] -> "
        return out + "None"

    def __len__(self):
      return len(list(iter(self)))

    def __eq__(self, other):
        return list(self) == list(other)

    def __getitem__(self, index):
        if index < 0:
            raise IndexError
        for i, item in enumerate(self):
            if i == index:
                return item
        raise IndexError


    def insert(self, value):
        self.head = Node(value, self.head)

    def append(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = node

class Node:
    def __init__(self, value, next_ = None):
        self.value = value
        self.next = next_


if __name__ == "__main__":
  
    foods = LinkedList(["apple","banana","cucumber"])

    first_food = foods[0]

    for food in foods:
        print(food)

    def gen():
        i = 0
        while True:
            yield i
            i += 1


    num_gtr = gen()

    for i in range(100):
        print(next(num_gtr))