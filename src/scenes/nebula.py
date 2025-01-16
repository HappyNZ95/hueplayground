from model.scene import Scene
nebula_colours = [

    {
        "xy": {
                            "x": 0.2712,
                            "y": 0.1723
                        }
    },

    {
        "xy": {
                            "x": 0.1911,
                            "y": 0.0673
                        }
    },

    {
        "xy": {
                            "x": 0.3743,
                            "y": 0.2727
                        }
    },

    {
        "xy": {
                            "x": 0.232,
                            "y": 0.2056
                        }
    },

    {
        "xy": {
                            "x": 0.3161,
                            "y": 0.2306
                        }
    },
]

nebula_default_brightness = 35

nebula = Scene("nebula", nebula_colours, 35)
