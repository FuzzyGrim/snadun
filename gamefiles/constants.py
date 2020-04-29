import tcod as libtcod
import pygame

pygame.init()

#  ____                           
# / ___|  ___ _ __ ___  ___ _ __  
# \___ \ / __| '__/ _ \/ _ \ '_ \ 
#  ___) | (__| | |  __/  __/ | | |
# |____/ \___|_|  \___|\___|_| |_|

# Game sizes
CAMERA_WIDTH = 1280
CAMERA_HEIGHT = 720
CELL_WIDTH = 32
CELL_HEIGHT =32

# FPS LIMIT
GAME_FPS = 63

# Map limitations
MAP_WIDTH = 20
MAP_HEIGHT = 20
MAP_MAX_NUM_ROOMS = 10
MAP_NUM_LEVELS = 2

# Room limitations
ROOM_MAX_HEIGHT = 7
ROOM_MAX_WIDTH = 5
ROOM_MIN_HEIGHT = 3
ROOM_MIN_WIDTH = 3

# Color definitions
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_GREY = (100, 100, 100)
COLOR_DGREY = (50, 50, 50)
COLOR_DARKERGREY = (25, 25, 25)
COLOR_RED = (255, 0, 0)
COLOR_GREEN = (0, 255, 0)

# Game colors
COLOR_DEFAULT_BG = COLOR_GREY

# FOV SETTINGS
FOV_ALGO = libtcod.FOV_BASIC  # Algorithm for FOV Calculation
FOV_LIGHT_WALLS = True        # Does the FOV shine on the walls?
TORCH_RADIUS = 10             # Sight radius for FOV

# MESSAGE DEFAULT
NUM_MESSAGES = 6

# FONTS #
FONT_DEBUG_MESSAGE = pygame.font.Font("data/joystix.ttf", 16)
FONT_MESSAGE_TEXT = pygame.font.Font("data/terminus.ttf", 12)
FONT_CURSOR_TEXT = pygame.font.Font("data/joystix.ttf", CELL_HEIGHT)
FONT_INVENTORY = pygame.font.Font("data/joystix.ttf", 12)
FONT_TITLE_SCREEN = pygame.font.Font("data/joystix.ttf", 25)