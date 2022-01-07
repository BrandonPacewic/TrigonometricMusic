import pygame

class window:
    HEIGHT = 900
    DISPLAY = (HEIGHT, HEIGHT/(16/9))


FPS = 60
WIN = pygame.display.set_mode(window.DISPLAY)

bounds = []

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