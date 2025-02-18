# Wreckfest Event List Generator

A Python script that generates random event lists for Wreckfest game servers. The generator creates a mix of racing, figure-8, and arena events with various vehicle class and car restrictions.

## Features

- Generates racing events with customizable laps
- Creates arena derby events
- Includes figure-8 racing events
- Randomizes car class restrictions (A, B, C, or special vehicles)
- Supports specific vehicle restrictions for special events

## Requirements

- Python 3.x
- Text files containing map lists:
  - `racing_maps.txt`
  - `arena_maps.txt`
  - `figure_8_maps.txt`

## Usage

1. Ensure you have the required map list files in the same directory as the script
2. Run the script:
```bash
python eventloop_creator.py
```
3. The script will generate an `output.txt` file containing the event list

## Output Format

The generated file uses the following format for each event:
```
el_add=map_name
el_gamemode=gamemode_type
el_laps=number_of_laps
el_bots=number_of_bots
el_car_class_restriction=class_restriction
el_car_restriction=specific_car_restriction
```

## Configuration

You can modify the following variables in the script to adjust the event generation:

- `ARENA_THRESHOLD`: Controls the frequency of arena events (default: 70)
- `FIGURE_8_THRESHOLD`: Controls the frequency of figure-8 events (default: 40)
- `RACING_LAPS`: Default number of laps for racing events (default: 5)
- `FIGURE_8_LAPS`: Default number of laps for figure-8 events (default: 12)
- Various vehicle restriction lists for different event types