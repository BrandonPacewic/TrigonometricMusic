#! /usr/bin/python3

from scipy.io.wavfile import read, write
from typing import List, Tuple

import logging
import math
import numpy as np
import pygame
import time

"""Should be removed after finished"""
def test(*values: object) -> None:
    logFile = 'consoleLog.txt'

    for value in values:
        logging.debug(value)

        try:
            with open(logFile, 'a') as file:
                file.write(f'{value}\n')
        except OSError:
            """If no write file just dont write"""
            pass

def clear_file(fname: str) -> None:
    try:
        with open(fname, 'w') as file:
            file.write(str(time.perf_counter()))
    except OSError:
        pass


class window:
    WIDTH = int(1820)
    HEIGHT = int(WIDTH/(16/9))
    DISPLAY = (WIDTH, HEIGHT)


FPS = int(60)
WIN = pygame.display.set_mode(window.DISPLAY)
pygame.display.set_caption('Trigonometric Music')

MAX_PIXELS = int(1000)


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
    def __init__(
        self, x: int, y: int, radi: int, velo: int = 1, 
        color: Tuple[int, int, int] = (255, 255, 255),
    ) -> None:
        self.x = x
        self.y = y
        self.center = (x, y)
        self.radi = radi
        self.velo = velo
        self.color = color

    def update(self) -> None:
        self.center = (self.x, self.y)
        self.color = round.cycle_colors(self.color)

    def draw(self, win: Tuple[int, int]) -> None:
        pygame.draw.circle(win, self.color, self.center, self.radi)
        self.x += self.velo

    @staticmethod
    def createRound(xOffset: int, yOffset: int, angle: int) -> Tuple[int, round]:
        change = 5
        size = 5
        muti = 5
        yPos = abs(int((math.degrees(math.sin(angle)) * muti) + yOffset))
        angle =  (angle + change) % 360

        test(f'{yPos=}')

        return angle, round(xOffset, yPos, size)

    @staticmethod
    def cycle_colors(color: Tuple[int, int, int]) -> Tuple[int, int, int]:
        change = 5
        basic = color[0]
        new = (basic + change) % 255
        return (new, new, new)


def create_bounds(win: Tuple[int, int]) -> List[box]:
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
    logging.basicConfig(
        level=logging.DEBUG,
        format='[INFO] - %(asctime)s - %(message)s',
    )
    clear_file('consoleLog.txt')

    clock = pygame.time.Clock()
    bounds = create_bounds(window.DISPLAY)

    pixels = []
    angle = int(0)

    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type is pygame.QUIT:
                exit()

        if len(pixels) > MAX_PIXELS:
            pixels.pop(0)

        angle, newRound = round.createRound(500, 500, angle)
        pixels.append(newRound)
        test(f'{angle=} {len(pixels)=}')
        render(pixels, bounds=bounds)


if __name__ == '__main__':
    main()