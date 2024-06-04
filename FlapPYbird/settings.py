from os import walk
import pygame

WIDTH, HEIGHT = 600, 650

obstacle_pair_sizes = [
    (1, 7),
    (2, 6),
    (3, 5),
    (4, 4),
    (5, 3),
    (6, 2),
    (7, 1)
]
obstacleSize = HEIGHT // 10
obstacleGap = (obstacleSize * 2) + (obstacleSize // 2)
groundSpace = 50
def import_sprite(path):
    surfaceList = []
    for _, __, imgFile in walk(path):
        for image in imgFile:
            fullPath = f"{path}/{image}"
            imgSurface = pygame.image.load(fullPath).convert_alpha()
            surfaceList.append(imgSurface)
    return surfaceList
