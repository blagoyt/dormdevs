bites = int(input())
stack = []
while True:
    command = input()
    if command == "Start":
        break
    else:
        stack.append(command)
while stack:
    person = stack.pop(0)
    if person == "refill":
        bites += int(input())
    else:
        bites -= int(input())
        if bites >= 0:
            print(f"{person} take bites")
        else:
            print(f"{person} must wait")
print(f"{bites} bites left")