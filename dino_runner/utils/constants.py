import pygame
import os

pygame.init()
# Global Constants
TITLE = "Dino Runner"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
FONT_STYLE = "freesansbold.ttf"

IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")
MUSIC_DIR = os.path.join(os.path.dirname(__file__), "..", "assets/Other/fundoMusic.mp3")

SMALL_CACTUS_Y_POS = 325
LARGE_CACTUS_Y_POS = 300
BIRD_Y_POS = 260

DEFAULT_TYPE = "default"
SHIELD_TYPE = "shield"
HAMMER_TYPE = "hammer"

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "Other/shield.png"))

RUNNING = [
    pygame.image.load(os.path.join(IMG_DIR, "mario/run1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "mario/run2.png")),
]

RUNNING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "mario/shield1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "mario/shield2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "mario/shield3.png")),
]

RUNNING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "mario/run_hammer.png")),
    pygame.image.load(os.path.join(IMG_DIR, "mario/run_hammer2.png")),
]

JUMPING = pygame.image.load(os.path.join(IMG_DIR, "mario/jump_default.png"))
JUMPING_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "mario/jump_shield.png"))
JUMPING_HAMMER = pygame.image.load(os.path.join(IMG_DIR, "mario/jump_hammer.png"))

DUCKING = [
    pygame.image.load(os.path.join(IMG_DIR, "mario/duck.png")),
    pygame.image.load(os.path.join(IMG_DIR, "mario/duck2.png")),
]

DUCKING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "mario/duck_shield.png")),
    pygame.image.load(os.path.join(IMG_DIR, "mario/duck_shield.png")), #retirar esse
]

DUCKING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "mario/duck_hammer.png")),
    pygame.image.load(os.path.join(IMG_DIR, "mario/duck_hammer.png")), #esse tbm
]

SMALL_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus3.png")),
]
LARGE_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus3.png")),
]

BIRD = [
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird2.png")),
]

CLOUD = pygame.image.load(os.path.join(IMG_DIR, 'Other/Cloud.png'))
SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))
HAMMER = pygame.image.load(os.path.join(IMG_DIR, 'Other/hammer.png'))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))

# DINO_DEAD = pygame.image.load(os.path.join(IMG_DIR, 'Dino/DinoStart.png')) 

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

DEFAULT_TYPE = "default"
