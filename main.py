from typing import List, Tuple
import pygame

class window:
    WIDTH = int(1600)
    HEIGHT = int(WIDTH/(16/9))
    DISPLAY = (WIDTH, HEIGHT)


FPS = int(60)
WIN = pygame.display.set_mode(window.DISPLAY)
pygame.display.set_caption("Trigonometric Music")


class box:
    def __init__(self, x: int, y: int, width: int, height: int) -> None:
        self.x = x
        self.y = y
        self.w = width
        self.h = height
        self.pyRect = pygame.Rect(x, y, width, height)

    def draw(self, win: Tuple[int, int]) -> None:
        COLOR = (255, 255, 255)
        pygame.draw.rect(win, COLOR, self.pyRect)


def _create_bounds(win: Tuple[int, int]) -> List[box]:
    THICKNESS = int(3)
    return [
        box(0, 0, win[0], THICKNESS),
        box(0, 0, THICKNESS, win[1]),
        box(THICKNESS, win[1] - THICKNESS, win[0], THICKNESS),
        box(win[0] - THICKNESS, 0, THICKNESS, win[1]),
    ]


def render(bounds: List[box]) -> None:
    WIN.fill((0, 0, 0))
    for bound in bounds:
        bound.draw(WIN)

    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    BOUNDS = _create_bounds(window.DISPLAY)

    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type is pygame.QUIT:
                exit()

        render(BOUNDS)


if __name__ == '__main__':
    main()