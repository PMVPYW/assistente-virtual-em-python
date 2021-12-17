import pygame

#constants and variables
WHITE = (255,255,255)
BLACK = (0,0,0)

WIDTH = 600
HEIGHT = 600

pygame.init()
game_font = pygame.font.SysFont("Ubuntu", 40)

delay = 30

paddle_speed = 20
paddle_width = 10
paddle_height = 100

p1_x_pos = 10
p1_y_pos = HEIGHT/2-paddle_height

p2_x_pos = WIDTH - paddle_width - 10
p2_y_pos = HEIGHT / 2 - paddle_height

p1_score = 0
p2_score = 0

p1_up = False
p1_down = False
p2_up = False
p2_down = False

ball_x_pos = WIDTH/2 
ball_y_pos = HEIGHT/2
ball_width = 8
ball_x_speed = -10
ball_y_speed = 0

screen = pygame.display.set_mode((WIDTH, HEIGHT))

#Drawing objects
def draw_objects():
    pygame.draw.rect(screen, WHITE, (int(p1_x_pos), int(p1_y_pos), paddle_width, paddle_height))
    pygame.draw.rect(screen, WHITE, (int(p2_x_pos), int(p2_y_pos), paddle_width, paddle_height))
    pygame.draw.circle(screen, WHITE, (ball_x_pos, ball_y_pos), ball_width)
    score = game_font.render(f"{str(p1_score)} - {str(p2_score)}", False, WHITE)
    screen.blit(score, (WIDTH/2, 30))

def apply_player_movement():
    global p1_y_pos
    global p2_y_pos
    
    if p1_up:
        p1_y_pos = max(p1_y_pos - paddle_speed, 0)
    elif p1_down:
        p1_y_pos = min(p1_y_pos + paddle_speed, HEIGHT)

    if p2_up:
        p2_y_pos = max(p2_y_pos - paddle_speed, 0)
    elif p2_down:
        p2_y_pos = min(p2_y_pos + paddle_speed, HEIGHT)

def apply_ball_movement():
    global ball_x_pos
    global ball_y_pos
    global ball_x_speed
    global ball_y_speed
    global p1_score
    global p2_score

    if (ball_x_pos + ball_x_speed < p1_x_pos + paddle_width) and (p1_y_pos < ball_y_pos + ball_y_speed + ball_width < p1_y_pos + paddle_height):
        ball_x_speed = -ball_x_speed
        ball_y_speed = (p1_y_pos + paddle_height / 2 - ball_y_pos) / 15
        ball_y_speed = -ball_y_speed
    elif ball_x_pos + ball_x_speed < 0:
        p2_score +=1
        ball_x_pos = WIDTH / 2
        ball_y_pos = HEIGHT / 2
        ball_x_speed = 10
        ball_y_speed = 0

    if (ball_x_pos + ball_x_speed > p2_x_pos - paddle_width) and (p2_y_pos < ball_y_pos + ball_y_speed + ball_width < p2_y_pos + paddle_height):
        ball_x_speed = -ball_x_speed
        ball_y_speed = (p2_y_pos + paddle_height / 2 - ball_y_pos) / 15
        ball_y_speed = -ball_y_speed
    elif ball_x_pos + ball_x_speed > HEIGHT:
        p1_score +=1
        ball_x_pos = WIDTH / 2
        ball_y_pos = HEIGHT / 2
        ball_x_speed = -10
        ball_y_speed = 0

    if ball_y_pos + ball_y_speed > HEIGHT or ball_y_pos + ball_y_speed < 0:
        ball_y_pos = -ball_y_speed

    ball_x_pos += ball_x_speed
    ball_y_pos += ball_y_speed

pygame.display.set_caption("Pong Game 1.0")
screen.fill(BLACK)
pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_w:
                p1_up = True
            if event.key == pygame.K_s:
                p1_down = True
            if event.key == pygame.K_UP:
                p2_up = True
            if event.key == pygame.K_DOWN:
                p2_down = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                p1_up = False
            if event.key == pygame.K_s:
                p1_down = False
            if event.key == pygame.K_UP:
                p2_up = False
            if event.key == pygame.K_DOWN:
                p2_down = False

    screen.fill(BLACK)
    apply_player_movement()
    apply_ball_movement()
    draw_objects()
    pygame.display.flip()
    pygame.time.wait(delay)