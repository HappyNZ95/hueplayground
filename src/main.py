import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

import argparse

from controllers import headers
from controllers import update_brightness, update_colour, update_scene, restore_scene_for_wake_up

from lights import haydens_room
from scenes.ibiza import ibiza_colours



def main():
    #change_colour(haydens_room[0],ibiza_colours[0])
    update_scene(haydens_room, ibiza_colours)



if __name__ == "__main__":
    main()
