import time
import random
import pygame


BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
ORANGE = (255,255,0)


width = 600
height = 600

enemy_speed = [-10, 10]

enemys = []
bullets = []

pygame.init()
screen = pygame.display.set_mode((width, height))

class Enemy:
    def __init__(self):
        self.x = random.randint(0, width)
        self.y = random.randint(0, height)-200
        self.speed = enemy_speed[random.randint(0, 1)]
        self.delay = 0.05
        self.begin = time.time()
        self.next_bullet = time.time()+5
    def draw(self):
        if time.time() >= self.begin + self.delay:
            self.x += self.speed
            self.begin = time.time()
        if self.x <= 0:
            self.speed = 10
        if self.x >= width:
            self.speed = -10
        pygame.draw.circle(screen, RED, (int(self.x), int(self.y)), 10)

class Player:
    def __init__(self):
        self.status = 1
        self.x = width/2
        self.y = height-100
        self.speed = 0
        self.delay = 0.05
        self.begin = time.time()
    def draw(self):
        if time.time() >= self.begin + self.delay:
            self.x += self.speed
            self.begin = time.time()
        if self.x + self.speed<= 0:
            self.speed = -self.speed
        if self.x + self.speed >= width:
            self.speed = -self.speed
        pygame.draw.circle(screen, WHITE, (int(self.x), int(self.y)), 10)

class Bullet:
    def __init__(self, x, y, owner):
        self.x = x
        self.y = y
        self.delay = 0.05
        self.begin = time.time()
        if owner == "player":
            self.speed = 10
        else:
            self.speed = -10
        self.owner = owner

    def draw(self):
        if time.time() >= self.begin + self.delay:
            self.y -= self.speed
            self.begin = time.time()
        pygame.draw.rect(screen, ORANGE, (int(self.x), int(self.y), 10, 10))
 

running = True
game_over = False

player = Player()
game_font = pygame.font.SysFont("Ubuntu", 40)
kills = 0
shooted = 0

def run():
    global player
    global kills
    global shooted
    global game_over
    if player.status == 1:
        screen.fill(BLACK)
        kills_message = game_font.render(f"Kills: {kills}", False, WHITE)
        screen.blit(kills_message, (10, 10))
        if shooted != 0:
            precision = round((kills/shooted)*100, 2)
        else:
            precision = 0
        precison_message = game_font.render(f"Precision: {precision}%", False, WHITE)
        screen.blit(precison_message, (10, 60))
        player.draw()
        for x in enemys:
            x.draw()
            if time.time() >= x.next_bullet:
                bullets.append(Bullet(x.x, x.y, "enemy"))
                x.next_bullet = time.time()+5
        print(len(bullets))
        for x in bullets:
            x.draw()
            for y in enemys:
                if x.x + x.speed >= y.x -15 and x.x +x.speed <= y.x + 15 and x.y >= y.y -15 and x.y <= y.y + 15 and x.owner == "player":
                    enemys.remove(y) 
                    bullets.remove(x) 
                    kills += 1
            if x.x + x.speed >= player.x -15 and x.x +x.speed <= player.x + 15 and x.y >= player.y -15 and x.y <= player.y + 15 and x.owner == "enemy":
                player.status = 0
                game_over = True
                break
            if x.y < 0 or x.y > width:
                bullets.remove(x)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bullets.append(Bullet(player.x - 5, player.y-20, "player"))
                    shooted += 1
                if event.key == pygame.K_LEFT:
                    player.speed = -10
                if event.key == pygame.K_RIGHT:
                    player.speed = 10
        pygame.display.update()

while running:
    begin = time.time()
    spawned = False
    target = 5
    while not game_over:
        current = time.time()-begin
        if int(current) %2 == 0 and not spawned:
            enemys.append(Enemy())
            spawned = True
        if int(current) %2 != 0 and spawned:
            spawned = False
        run()
    screen.fill(BLACK)
    message = game_font.render(f"GAME OVER!", False, RED)
    screen.blit(message, (10, 10))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
