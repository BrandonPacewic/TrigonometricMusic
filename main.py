from typing import List, Tuple
import pygame

class window:
    HEIGHT = int(1920)
    DISPLAY = (HEIGHT, int(HEIGHT/(16/9)))


FPS = 60
WIN = pygame.display.set_mode(window.DISPLAY)
pygame.display.set_caption("Trigonometric Music")


class box:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.w = width
        self.h = height
        self.pyRect = pygame.Rect(x, y, width, height)

    def draw(self, win):
        pygame.draw.rect(win, (255, 255, 255), self.pyRect)


def _create_bounds(win: Tuple[int, int]) -> List[box]:
    THICKNESS = 10

    bounds = [
        box(0, 0, win[0], THICKNESS),
        box(0, 0, THICKNESS, win[1]),
        box(0, win[1], win[0], THICKNESS),
        box(win[0] - THICKNESS, 0, THICKNESS, win[1]),
    ]

    return bounds

bounds = _create_bounds(window.DISPLAY)


def render():
    WIN.fill((0, 0, 0))
    for bound in bounds:
        bound.draw(WIN)


def main():
    clock = pygame.time.Clock()
    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type is pygame.QUIT:
                exit()

        render()


if __name__ == '__main__':
    main()