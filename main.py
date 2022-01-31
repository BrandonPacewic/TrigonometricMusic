#! /usr/bin/python3

from typing import List, Tuple

import math
import pygame

class window:
    WIDTH = int(1820)
    HEIGHT = int(WIDTH/(16/9))
    DISPLAY = (WIDTH, HEIGHT)


FPS = int(30)
WIN = pygame.display.set_mode(window.DISPLAY)
pygame.display.set_caption('Trigonometric Music')

MAX_PIXELS = int(1000)

angle = 0
color = (0, 0, 0)


def cycle_colors(color: Tuple[int, int, int] = (0, 0, 0)) -> Tuple[int, int, int]:
    change = 5
    for val in color:
        val = (val + change) % 255

    return color


class box:
    def __init__(self, x: int, y: int, width: int, height: int) -> None:
        self.x = x
        self.y = y
        self.w = width
        self.h = height
        self.pyRect = pygame.Rect(x, y, width, height)

    def draw(self, win: Tuple[int, int]) -> None:
        pygame.draw.rect(win, (255, 255, 255), self.pyRect)


class round:
    def __init__(self, x: int, y: int, radi: int, velo: int = 1) -> None:
        self.x = x
        self.y = y
        self.center = (x, y)
        self.velo = velo
        self.radi = radi

    def update(self) -> None:
        self.center = (self.x, self.y)

    def draw(self, win: Tuple[int, int]) -> None:
        color = cycle_colors(color)
        pygame.draw.circle(win, color, self.center, self.radi)
        self.x += self.velo

    @staticmethod
    def createRound(xOffset: int, yOffset: int) -> Tuple[int, round]:
        change = 1
        size = 5
        muti = 100
        yPos = (math.sin(angle) * muti) + yOffset
        print(f'{yPos=}')

        return (angle + change) % 360, round(xOffset, yPos, size)


def _create_bounds(win: Tuple[int, int]) -> List[box]:
    THICKNESS = int(3)
    return [
        box(0, 0, win[0], THICKNESS),
        box(0, 0, THICKNESS, win[1]),
        box(THICKNESS, win[1] - THICKNESS, win[0], THICKNESS),
        box(win[0] - THICKNESS, 0, THICKNESS, win[1]),
    ]


def render(pixels: List[round], bounds: List[box]) -> None:
    WIN.fill((0, 0, 0))

    for bound in bounds:
        bound.draw(WIN)

    for pixel in pixels:
        pixel.draw(WIN)
        pixel.update()

    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    bounds = _create_bounds(window.DISPLAY)

    pixels = []

    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type is pygame.QUIT:
                exit()

        if len(pixels) > MAX_PIXELS:
            pixels.pop(0)

        angle, newRound = round.createRound(500, 300)
        pixels.append(newRound)
        print(f'{angle=}, {len(pixels)=}')
        render(pixels, bounds=bounds)


if __name__ == '__main__':
    main()