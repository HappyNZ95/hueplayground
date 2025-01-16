class Scene:
    def __init__(self, name, colours, brightness):
        self.name = name
        self.colours = colours
        self.brightness = brightness

    def print(self):
        print(self.name, self.colours, self.brightness)
