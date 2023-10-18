from collections import deque
queue = deque()

while True:
    customer = input()

    if customer == "PAID".lower():
        for person in queue:
            print(person)
        queue.clear()
    if customer == "END".lower():
        remaining = len(queue)
        print(f"{remaining} people remaining.")
        break
    else:
        queue.append(customer)