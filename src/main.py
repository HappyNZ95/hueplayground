import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

import argparse

from controllers import headers
from controllers import update_brightness, update_colour, update_scene, restore_scene_for_wake_up

from lights import haydens_room
from scenes.ibiza import ibiza_colours


def is_int(value):
    try:
        return int(value), True
    except ValueError:
        return value, False


parser = argparse.ArgumentParser(description="A controller for Phillips hue")

parser.add_argument("input", help="Enter a scene or a brightness value i.e. ibiza or 57")
args=parser.parse_args()

value, is_number = is_int(args.input)




def main():
    #change_colour(haydens_room[0],ibiza_colours[0])
    update_scene(haydens_room, ibiza_colours)



if __name__ == "__main__":
    main()
