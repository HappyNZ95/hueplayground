import requests
import time
from lights import haydens_room
from scenes.ibiza import ibiza_colours
import json
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)




headers = {
    "hue-application-key": "IfFAxmMRJ9KwlVA4o0WgK7es-1o2xPDuxhG85j1U",
    "Content-Type": "application/json"
    }



def update_brightness(url, brightness):

    data = {
    "on":{"on":True},
    "dimming":{"brightness":brightness}
    }
    response = requests.put(url, json=data, headers=headers, verify=False)
    #print("Status Code:", response.status_code)
    #print("Response Body:", response.text)
    return response


def restore_scene_for_wake_up(
    room,
    ending_brightness,
    brightness_increment,
    duration_in_seconds,
    time_increment_in_seconds,
    brightness = 0
):
    seconds_passed = 0

    #check to see if lights are on
    response = requests.get("https://192.168.1.247/clip/v2/resource/light/61a7c89c-8043-4dfc-9e35-a07aa256f690", headers=headers, verify=False)
    light_initially_on = json.loads(response.text)["data"][0]["on"]["on"]

    # if the light isn't on, set the brightness to the lowest value (0), turning the light on
    if not light_initially_on:
        for light in haydens_room:
            update_brightness(light, brightness)
    brightness += brightness_increment

    # If the light is on, person might be awake so
    if light_initially_on:
        exit()

    while seconds_passed < duration_in_seconds:


            if brightness < ending_brightness:
                response = requests.get("https://192.168.1.247/clip/v2/resource/light/61a7c89c-8043-4dfc-9e35-a07aa256f690", headers=headers, verify=False)
                light_on = json.loads(response.text)["data"][0]["on"]["on"] #are lights on boolean
                print("light on:", light_on)
                if not light_on:
                    exit()

                print(f"{seconds_passed} seconds out of {duration_in_seconds}")

                for light in haydens_room:
                    update_brightness(light, brightness)
                    print("Brightness:", brightness)
                seconds_passed += time_increment_in_seconds
                time.sleep(time_increment_in_seconds)
                brightness += brightness_increment


            if brightness >= ending_brightness:
                for light in haydens_room:
                    update_brightness(light, ending_brightness)
                    exit()


def update_colour(url, colour_json):
    data = {"color": colour_json}
    response = requests.put(url, json=data, headers=headers, verify=False)
    print(response.status_code)
    print(response.text)
    return response

def change_scene(room, colour_list):
    for light, colour in zip(room, colour_list):
        update_colour(light, colour)

def main():
    #change_colour(haydens_room[0],ibiza_colours[0])
    change_scene(haydens_room, ibiza_colours)



if __name__ == "__main__":
    main()
