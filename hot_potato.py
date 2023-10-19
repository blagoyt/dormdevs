
players_names = input().split(" ")     # Четем имената на всичките играчи и го записваме в списък
n_throwing = int(input())   #  Четем на кое хвърляне играча изгаря
current_player = 0       #  Записваме индекса на играча който ще изгори
while True:
    if len(players_names) == 1:   #  Проверяваме дали в players_names има само 1 играч
        break
    current_player = (n_throwing + current_player - 1) % len(players_names)   #  Изчисляваме индекса на който ще гоним играч: хвърлянето на играча който ще изгори + индекса на играча в момента - 1 защото да изчислим на кой индекс сенамира и това цялото го делим с остатък на дължината на имената на играчите
    removed_player = players_names.pop(current_player)  #  Тук махаме от списъке играча от гония ред
    print(f"Removed {removed_player}") 

print(f"Last is {players_names[0]}")

