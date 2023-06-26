import pygame

pygame.init()

display = pygame.display.set_mode((1024, 1024))
display.fill((244, 220, 181))

pygame.display.set_caption("Checkers")

wChecker = pygame.image.load("./assets/White.png")
bChecker = pygame.image.load("./assets/Black.png")
wQueen = pygame.image.load("./assets/WhiteQ.png")
bQueen = pygame.image.load("./assets/BlackQ.png")

class WhiteChecker(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = wChecker
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class BlackChecker(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = bChecker
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class WhiteQueen(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = wQueen
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class BlackQueen(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = bQueen
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
CHECKER_empty = 0
CHECKER_black = 1
CHECKER_black_queen = 2
CHECKER_white = 3
CHECKER_white_queen = 4

board = [
    CHECKER_black,CHECKER_black,CHECKER_black,CHECKER_black,
    CHECKER_black,CHECKER_black,CHECKER_black,CHECKER_black,
    CHECKER_black,CHECKER_black,CHECKER_black,CHECKER_black,

    CHECKER_empty,CHECKER_empty,CHECKER_empty,CHECKER_empty,
    CHECKER_empty,CHECKER_empty,CHECKER_empty,CHECKER_empty,

    CHECKER_white,CHECKER_white,CHECKER_white,CHECKER_white,
    CHECKER_white,CHECKER_white,CHECKER_white,CHECKER_white,
    CHECKER_white,CHECKER_white,CHECKER_white,CHECKER_white
]

positions = [
    (128, 0), (384, 0), (640, 0), (896, 0),
    (0, 128), (256, 128), (512, 128), (768, 128),
    (128, 256), (384, 256), (640, 256), (896, 256),
    (0, 384), (256, 384), (512, 384), (768, 384),
    (128, 512), (384, 512), (640, 512), (896, 512),
    (0, 896), (256, 896), (512, 896), (768, 896),
    (128, 768), (384, 768), (640, 768), (896, 768),
    (0, 640), (256, 640), (512, 640), (768, 640)
]

all_sprites = pygame.sprite.Group()

# Create sprite instances based on board configuration
for i in range(len(board)):
    checker = board[i]
    x, y = positions[i]
    if checker == CHECKER_black:
        all_sprites.add(BlackChecker(x, y))
    elif checker == CHECKER_black_queen:
        all_sprites.add(BlackQueen(x, y))
    elif checker == CHECKER_white:
        all_sprites.add(WhiteChecker(x, y))
    elif checker == CHECKER_white_queen:
        all_sprites.add(WhiteQueen(x, y))

timer = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draws the board
    for y in range(1, 9):
        for x in range(4):
            if y % 2 == 0:
                xPos = 0
            else:
                xPos = 129
            pygame.draw.rect(display, (179, 136, 102), pygame.Rect(xPos + (256 * x), 128 * (y - 1), 128, 128))

    all_sprites.draw(display)  # Draws all the sprites

    pygame.display.flip()  # Update the display

    timer.tick(60)

pygame.quit()