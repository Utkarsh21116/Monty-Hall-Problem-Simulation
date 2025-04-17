import random

stay = 0
switch = 0
i = 0
while i<10000:
    door = [0,0,0]
    door_no = [1,2,3]
    car = random.randrange(0,3,1)

    door[car] = 1

    choice = random.randrange(0,3,1)

    if choice == car:
        del door_no[car]
        open = random.choice(door_no)
    else:
        x = 0
        for j in door_no:
            if j== car+1 or j== choice+1:
                del door_no[x]
            x+=1
        open = door_no[0]

    if choice == car:
        stay = stay + 1
    else:
        switch = switch + 1

    i+=1

print(f"No switch Wins = {stay}  | {stay/(stay+switch)*100:.2f}%")
print(f"Switch Wins = {switch}   | {switch/(stay+switch)*100:.2f}%")
