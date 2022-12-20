# Aoc 2022 - Day 20

from utils import get_data

part1 = False

lines = get_data(20).strip().split("\n")

order = []

class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
    self.prev = None

head = None
current = None
zero = None

for line in lines:
    line = int(line)
    if not part1:
      line *= 811589153
    n = Node(line)
    order.append(n)
    if head == None:
        head = n
        current = n
    else:
        n.prev = current
        current.next = n
        current = n

    if line == 0:
        zero = n


current.next = head
head.prev = current

for _ in range((1 if part1 else 10)):
  for order_index in range(len(order)):
      head = order[order_index]

      new_position = head

      amount = head.data%(len(order)-1)

      head.prev.next = head.next
      head.next.prev = head.prev

      x = head.prev
      y = head.next


      for _ in range(amount):
            x = x.next
            y = y.next
          
      x.next = head
      head.prev = x
      y.prev = head
      head.next = y


head = zero

ans = 0

for _ in range(3):
    for _ in range(1000):
        head = head.next
       
    ans += head.data
    

print(ans)




