import constants

class Cell:

    def __init__(self, value):
        self.value = value
        self.bg = constants.BACKGROUND_COLOR_DICT(self.value)
        self.fg = constants.FOREGROUND_COLOR_DICT(self.value)

        