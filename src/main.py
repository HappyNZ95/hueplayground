import requests
import time
from lights import haydens_room


def update_brightness(url, brightness):
    data = {
    "on":{"on":True},
    "dimming":{"brightness":brightness}
    }
    headers = {
    "hue-application-key": "IfFAxmMRJ9KwlVA4o0WgK7es-1o2xPDuxhG85j1U",
    "Content-Type": "application/json"
    }

    response = requests.put(url, json=data, headers=headers, verify=False)
    print("Status Code:", response.status_code)
    print("Response Body:", response.text)
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

    while seconds_passed < duration_in_seconds:
        for light in haydens_room:
            update_brightness(light, brightness)
        seconds_passed += time_increment_in_seconds
        print("Brightness:", brightness)
        print(f"{seconds_passed} seconds out of {duration_in_seconds}")
        time.sleep(time_increment_in_seconds)
        brightness += brightness_increment
def main():
    restore_scene_for_wake_up(haydens_room, 100, 5, 60, 2)




if __name__ == "__main__":
    main()
