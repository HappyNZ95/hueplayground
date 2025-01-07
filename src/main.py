import requests
import time

def updateBrightness(url, brightness):
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

    brightness = 0
    updateBrightness("https://192.168.1.247/clip/v2/resource/light/61a7c89c-8043-4dfc-9e35-a07aa256f690", brightness)
    time.sleep(3)
    brightness += 5
    updateBrightness("https://192.168.1.247/clip/v2/resource/light/61a7c89c-8043-4dfc-9e35-a07aa256f690", brightness)

    time.sleep(3)
    brightness += 5
    updateBrightness("https://192.168.1.247/clip/v2/resource/light/61a7c89c-8043-4dfc-9e35-a07aa256f690", brightness)

    time.sleep(3)
    brightness += 5
    updateBrightness("https://192.168.1.247/clip/v2/resource/light/61a7c89c-8043-4dfc-9e35-a07aa256f690", brightness)

    time.sleep(3)
    brightness += 5
    updateBrightness("https://192.168.1.247/clip/v2/resource/light/61a7c89c-8043-4dfc-9e35-a07aa256f690", brightness)
if __name__ == "__main__":
    main()
