import requests
import time
from lights import hayden_lantern, hayden_hue_desk, hayden_under_bed, hayden_hue_bookshelf, hayden_bedside_lamp


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


def main():

    starting_brightness = 0
    ending_brightness = 100
    brightness_increment = 3
    duration_in_seconds = 60
    sleep_time = 3
    seconds = 0
    brightness = starting_brightness

    update_brightness(hayden_lantern, brightness)
    update_brightness(hayden_hue_desk, brightness)
    update_brightness(hayden_under_bed, brightness)
    update_brightness(hayden_hue_bookshelf, brightness)
    update_brightness(hayden_bedside_lamp, brightness)
    time.sleep(sleep_time)
    brightness += brightness_increment

    while seconds < duration_in_seconds:
        update_brightness(hayden_lantern, brightness)
        update_brightness(hayden_hue_desk, brightness)
        update_brightness(hayden_under_bed, brightness)
        update_brightness(hayden_hue_bookshelf, brightness)
        update_brightness(hayden_bedside_lamp, brightness)
        print("Brightness:", brightness)
        seconds += sleep_time
        print(f"{seconds} seconds out of {duration_in_seconds}")
        time.sleep(sleep_time)
        brightness += brightness_increment

if __name__ == "__main__":
    main()
