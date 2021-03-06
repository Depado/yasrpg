CHARSET_DIR = '../res/charsets/'
MAPS_DIR = '../maps/'
FONTS_DIR = '../res/fonts/'
FONT = FONTS_DIR + "dos.ttf"
IMAGES_DIR = '../res/images/'
FONT_SIZE = 16
DIR_DOWN, DIR_LEFT, DIR_RIGHT, DIR_UP = 0, 1, 2, 3

def valid_dir(direction):
    direction = int(direction)
    if direction < 0 or direction > 3:
        return False
    return True
