import os
import random

"""
Maps Files
"""
RACING_MAPS = './racing_maps.txt'
ARENA_MAPS = './arena_maps.txt'
FIGURE_8_MAPS = './figure_8_maps.txt'

"""
Config
"""
CLASS_RESTRICTIONS = ['a', 'b', 'c'] * 2 + ['special']
FIGURE_8_CLASS_RESTRICTIONS = ['a', 'b', 'c', 'special']
ARENA_RESTRICTIONS = ['school bus', 'lawn mower', 'bumper car', 'honey pot']
FIGURE_8_RESTRICTIONS = ['school bus'] * 4 + ['motor home', 'sofa car', 'big rig']
RACING_RESTRICTIONS = ['school bus'] * 8 + ['motor home', 'sofa car', 'bugzilla', 'big rig']
OUTPUT_FILE = 'output.txt'

ARENA_THRESHOLD = 70
FIGURE_8_THRESHOLD = 40
DEFAULT_BOTS = 0
RACING_LAPS = 5
FIGURE_8_LAPS = 12

GAMEMODE_RACING = 'racing'
GAMEMODE_DERBY = 'derby deathmatch'

def outputRace(z_map, z_class_restriction, z_car_restriction, gamemode, bots, laps=None):
    with open(OUTPUT_FILE, 'a') as f:
        f.write(f"el_add={z_map}\n")
        f.write(f'el_gamemode={gamemode}\n')
        if gamemode == GAMEMODE_RACING:
            f.write(f'el_laps={laps}\n')
        f.write(f'el_bots={bots}\n')
        f.write(f'el_car_class_restriction={z_class_restriction}\n')
        f.write(f'el_car_restriction={z_car_restriction}\n')
        f.write('\n')

def load_maps(file_path):
    with open(file_path) as f:
        return f.read().splitlines()

def select_restrictions(class_restrictions, specific_restrictions):
    z_class_restriction = random.choice(class_restrictions)
    z_car_restriction = ''
    if z_class_restriction == 'special':
        z_class_restriction = ''
        z_car_restriction = random.choice(specific_restrictions)
    return z_class_restriction, z_car_restriction

def main():
    if os.path.exists(OUTPUT_FILE):
        os.remove(OUTPUT_FILE)

    arena_maps = load_maps(ARENA_MAPS)
    racing_maps = load_maps(RACING_MAPS)
    figure_8_maps = load_maps(FIGURE_8_MAPS)

    for _ in range(100):
        y = random.randint(0, 100)

        if y > ARENA_THRESHOLD:
            z_map = random.choice(arena_maps)
            z_class_restriction, z_car_restriction = select_restrictions(CLASS_RESTRICTIONS, ARENA_RESTRICTIONS)
            outputRace(z_map, z_class_restriction, z_car_restriction, GAMEMODE_DERBY, DEFAULT_BOTS)

        elif y < FIGURE_8_THRESHOLD:
            z_map = random.choice(figure_8_maps)
            z_class_restriction, z_car_restriction = select_restrictions(FIGURE_8_CLASS_RESTRICTIONS, FIGURE_8_RESTRICTIONS)
            outputRace(z_map, z_class_restriction, z_car_restriction, GAMEMODE_RACING, DEFAULT_BOTS, FIGURE_8_LAPS)

        else:
            z_map = random.choice(racing_maps)
            z_class_restriction, z_car_restriction = select_restrictions(CLASS_RESTRICTIONS, RACING_RESTRICTIONS)
            outputRace(z_map, z_class_restriction, z_car_restriction, GAMEMODE_RACING, DEFAULT_BOTS, RACING_LAPS)

if __name__ == "__main__":
    main()