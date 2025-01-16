from scenes.ibiza import ibiza_colours
class Scene:
    def __init__(self, name, brightness, colours):
        self.name = name
        self.brightness = brightness
        self.colours = colours

    def print(self):
        print(self.name, self.brightness, self.colours)

#to be continued....
ibiza = Scene("ibiza", 49, ibiza_colours)

scenes = [ibiza]
