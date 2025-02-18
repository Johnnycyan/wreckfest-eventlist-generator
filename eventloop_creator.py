import random
import os
from random import randint

with open('./racing_maps.txt') as f:
    racing_maps = f.read().splitlines()

with open('./arena_maps.txt') as f:
    arena_maps = f.read().splitlines()

with open('./figure_8_maps.txt') as f:
    figure_8_maps = f.read().splitlines()


class_restrictions = ['a','b','c','a','b','c','special']
figure_8_class_restrictions = ['a','b','c','special']
arena_restrictions = ['school bus','lawn mower','bumper car','honey pot']
figure_8_restrictions = ['school bus','school bus','school bus','school bus','motor home','sofa car','big rig']
racing_restrictions = ['school bus','school bus','school bus','school bus','school bus','school bus','school bus','school bus','motor home','sofa car','bugzilla','big rig']
laps = ['5', '6', '7']
outputFile = 'output.txt'

if os.path.exists(outputFile):
    os.remove(outputFile)
x = 0
while x <= 100:
    y = randint(0,100)

    if y > 70:
        z_map = random.choice(arena_maps)

        z_class_restriction = random.choice(class_restrictions)
        z_car_restriction = ''
        if z_class_restriction == 'special':
            z_class_restriction = ''
            z_car_restriction = random.choice(arena_restrictions)
        with open(outputFile, 'a') as f:
            f.write("el_add=" + z_map + "\n")
            f.write('el_gamemode=derby deathmatch\n')
            f.write('el_bots=0\n')
            f.write('el_car_class_restriction=' + z_class_restriction + "\n")
            f.write('el_car_restriction=' + z_car_restriction + "\n")
            f.write('\n')
        print('el_add='+z_map)
        print('el_gamemode=derby deathmatch')
        #print('el_bots=',randint(1,8))
        print('el_bots=0')
        print('el_car_class_restriction='+z_class_restriction)
        print('el_car_restriction='+z_car_restriction)
        print('')
    
    elif y < 40:
        z_map = random.choice(figure_8_maps)

        z_class_restriction = random.choice(figure_8_class_restrictions)
        z_car_restriction = ''
        if z_class_restriction == 'special':
            z_class_restriction = ''
            z_car_restriction = random.choice(figure_8_restrictions)

        with open(outputFile, 'a') as f:
            f.write("el_add=" + z_map + "\n")
            f.write('el_gamemode=racing\n')
            f.write('el_laps=12\n')
            f.write('el_bots=0\n')
            f.write('el_car_class_restriction=' + z_class_restriction + "\n")
            f.write('el_car_restriction=' + z_car_restriction + "\n")
            f.write('\n')
        print("el_add="+z_map)
        print('el_gamemode=racing')
        print('el_laps=12')
        #print('el_bots=',randint(1,8))
        print('el_bots=0')
        print('el_car_class_restriction='+z_class_restriction)
        print('el_car_restriction='+z_car_restriction)
        print('')
    
    else:
        z_map = random.choice(racing_maps)

        z_class_restriction = random.choice(class_restrictions)
        z_car_restriction = ''
        if z_class_restriction == 'special':
            z_class_restriction = ''
            z_car_restriction = random.choice(racing_restrictions)
        
        with open(outputFile, 'a') as f:
            f.write("el_add=" + z_map + "\n")
            f.write('el_gamemode=racing\n')
            f.write('el_laps=5\n')
            f.write('el_bots=0\n')
            f.write('el_car_class_restriction=' + z_class_restriction + "\n")
            f.write('el_car_restriction=' + z_car_restriction + "\n")
            f.write('\n')
        print("el_add="+z_map)
        print('el_gamemode=racing')
        print('el_laps=5')
        #print('el_bots=',randint(1,8))
        print('el_bots=0')
        print('el_car_class_restriction='+z_class_restriction)
        print('el_car_restriction='+z_car_restriction)
        print('')
        
    x += 1