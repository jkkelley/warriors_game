import pygame
import os

pygame.init()

win = pygame.display.set_mode((500, 480))

pygame.display.set_caption("Warrior Games")

# walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
# walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
# bg = pygame.image.load('bg.jpg')
# char = pygame.image.load('standing.png')

walkRight = [pygame.image.load(os.path.join('charModel', 'R1.png')),
             pygame.image.load(os.path.join('charModel', 'R2.png')),
             pygame.image.load(os.path.join('charModel', 'R3.png')),
             pygame.image.load(os.path.join('charModel', 'R4.png')),
             pygame.image.load(os.path.join('charModel', 'R5.png')),
             pygame.image.load(os.path.join('charModel', 'R6.png')),
             pygame.image.load(os.path.join('charModel', 'R7.png')),
             pygame.image.load(os.path.join('charModel', 'R8.png')),
             pygame.image.load(os.path.join('charModel', 'R9.png'))]

walkLeft = [pygame.image.load(os.path.join('charModel', 'L1.png')),
            pygame.image.load(os.path.join('charModel', 'L2.png')),
            pygame.image.load(os.path.join('charModel', 'L3.png')),
            pygame.image.load(os.path.join('charModel', 'L4.png')),
            pygame.image.load(os.path.join('charModel', 'L5.png')),
            pygame.image.load(os.path.join('charModel', 'L6.png')),
            pygame.image.load(os.path.join('charModel', 'L7.png')),
            pygame.image.load(os.path.join('charModel', 'L8.png')),
            pygame.image.load(os.path.join('charModel', 'L9.png'))]

bg = pygame.image.load(os.path.join('charModel', 'bg.jpg'))
char = pygame.image.load(os.path.join('charModel', 'standing.png'))

clock = pygame.time.Clock()


class PlayerModel(object):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.walCount = 0
        self.standing = True

    def draw(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if not self.standing:
            if self.left:
                win.blit(walkLeft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(walkRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
        else:
            if self.right:
                win.blit(walkRight[0], (self.x, self.y))
            else:
                win.blit(walkLeft[0], (self.x, self.y))


class Projectile(object):
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)


def redrawGameWindow():
    win.blit(bg, (0, 0))
    warrior.draw(win)
    for bullet in bullets:
        bullet.draw(win)

    pygame.display.update()


# mainloop
warrior = PlayerModel(200, 410, 64, 64)
bullets = []
run = True
while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets:
        if bullet.x < 500 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.remove(bullet)

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        if warrior.left:
            facing = -1
        else:
            facing = 1
        if len(bullets) < 5:
            bullets.append(Projectile(round(warrior.x + warrior.width // 2), round(warrior.y + warrior.height // 2), 6, (0, 0, 0), facing))

    if keys[pygame.K_LEFT] and warrior.x > warrior.vel:
        warrior.x -= warrior.vel
        warrior.left = True
        warrior.right = False
        warrior.standing = False
    elif keys[pygame.K_RIGHT] and warrior.x < 500 - warrior.width - warrior.vel:
        warrior.x += warrior.vel
        warrior.right = True
        warrior.left = False
        warrior.standing = False
    else:
        warrior.standing = True
        warrior.walkCount = 0

    if not warrior.isJump:
        if keys[pygame.K_UP]:
            warrior.isJump = True
            warrior.right = False
            warrior.left = False
            warrior.walkCount = 0
    else:
        if warrior.jumpCount >= -10:
            neg = 1
            if warrior.jumpCount < 0:
                neg = -1
            warrior.y -= (warrior.jumpCount ** 2) * 0.5 * neg
            warrior.jumpCount -= 1
        else:
            warrior.isJump = False
            warrior.jumpCount = 10

    redrawGameWindow()

pygame.quit()


