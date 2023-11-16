count_of_people = int(input()) #Взимаме броя на поканите
invitation_numbers = set() #Сета в който ще запазваме номерата на поканите

for person in range(count_of_people):
    invitation_number = input() #Взимаме номера на поканата
    invitation_numbers.add(invitation_number) #Добавяме я към сета

while True:
    a = input() #Взимаме номера на поканите на тези които са дошли
    if a == "END":
        break
    if a in invitation_numbers:
        invitation_numbers.remove(a) #И ги премахваме от сета за да запазим в него хората които не са дошли

print(len(invitation_numbers)) #Принтираме държината на сета
print(*sorted(invitation_numbers)) #Ънпакваме сета и го сортираме за да започва от учителите

