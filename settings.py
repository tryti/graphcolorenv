import enum

COLOR = "color"


class Color(enum.Enum):
    RED = 1
    BLUE = 2
    GREEN = 3
    YELLOW = 4
    NOCOLOR = 5

    @classmethod
    def all_colors(cls):
        """
        Returns a list of all color values
        :return:
        """
        return [i for i in range(1, cls.NOCOLOR)]

    @classmethod
    def rgb(cls, color):
        rgb_values = {1: (255, 0, 0),
                      2: (0, 0, 255),
                      3: (0, 255, 0),
                      4: (255, 255, 0)}
        return rgb_values[color]
