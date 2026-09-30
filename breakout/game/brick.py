"""
Brick: a single block with a type and hit count.
"""

import pygame


class Brick:
    def __init__(
        self,
        x,
        y,
        width,
        height,
        hits_remaining=1,
        color=(200, 90, 90),
        brick_type="normal"
    ):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hits_remaining = hits_remaining
        self.color = color
        self.brick_type = brick_type

    def get_rect(self):
        return pygame.Rect(int(self.x), int(self.y), self.width, self.height)
