from collections import deque

children = input().split()
n = int(input())
circle = deque(children)

while len(circle) > 1:
    for _ in range(n - 1):
        circle.append(circle.popleft())
    removed_child = circle.popleft()
    print(f"Removed {removed_child}")

last_child = circle[0]
print(f"Last is {last_child}")
