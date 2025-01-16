from scenes.ibiza import ibiza_colours

class Scene:
    def __init__(self, name, colours, brightness):
        self.name = name
        self.colours = colours
        self.brightness = brightness

    def print(self):
        print(self.name, self.colours, self.brightness)

ibiza = Scene("ibiza", ibiza_colours, 49)

scenes = [ibiza]
