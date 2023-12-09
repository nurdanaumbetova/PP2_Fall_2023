import pygame
import os

pygame.font.init()
pygame.mixer.init()

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Game')

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

HEALTH_FONT = pygame.font.SysFont('comicsans', 20)
BULLETS_FONT = pygame.font.SysFont('comicsans', 20)
WINNER_FONT = pygame.font.SysFont('comicsans', 100)

FPS = 60
VEL = 10
BULLET_VEL = 25
MAX_BULLETS = 15

BORDER = pygame.Rect(WIDTH // 2 - 5, 0, 10, HEIGHT)

BULLET_HIT_SOUND = pygame.mixer.Sound(os.path.join('Music', 'Grenade+1.mp3'))
BULLET_FIRE_SOUND1 = pygame.mixer.Sound(os.path.join('Music', 'Gun+Silencer.mp3'))
BULLET_FIRE_SOUND2 = pygame.mixer.Sound(os.path.join('Music', 'Gun+Silencer.mp3'))

PRINCE_WIDTH = 150
PRINCE_HEIGHT = 130

YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2


PrinceArnee_pic = pygame.image.load(os.path.join('Assets', 'king.png'))
PrinceArnee = pygame.transform.rotate(pygame.transform.scale(
    PrinceArnee_pic, (PRINCE_WIDTH, PRINCE_HEIGHT)), 0)

SecondPrince_pic = pygame.image.load(os.path.join('Assets', 'prince2.png'))
SecondPrince = pygame.transform.rotate(pygame.transform.scale(
    SecondPrince_pic, (PRINCE_WIDTH, PRINCE_HEIGHT)), 0)

SPACE_PIC = pygame.image.load(os.path.join('Assets', 'backphoto.jpg'))

PLAYER1_WINS_IMAGE = pygame.image.load(os.path.join('Assets', 'winprincess.png'))
PLAYER2_WINS_IMAGE = pygame.image.load(os.path.join('Assets', 'loserprincess.png'))

def draw_winner(text, winner_image):
    draw_text = WINNER_FONT.render(text, 1, WHITE)
    WIN.blit(draw_text, (WIDTH // 2 - draw_text.get_width() // 2, HEIGHT // 2 - draw_text.get_height() // 2))
    pygame.display.update()
    pygame.time.delay(3000)

    WIN.blit(winner_image, (0, 0))
    pygame.display.update()
    pygame.time.delay(3000)

def draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health):
    WIN.blit(SPACE_PIC, (0, 0))
    pygame.draw.rect(WIN, BLACK, BORDER)

    red_health_txt = HEALTH_FONT.render('HEALTH: ' + str(red_health), 1, WHITE)
    yellow_health_txt = HEALTH_FONT.render('HEALTH: ' + str(yellow_health), 1, WHITE)

    red_bullets_display = BULLETS_FONT.render('BULLETS: ' + str(len(red_bullets)), 1, WHITE)
    yellow_bullets_display = BULLETS_FONT.render('BULLETS: ' + str(len(yellow_bullets)), 1, WHITE)

    WIN.blit(red_health_txt, (WIDTH - red_health_txt.get_width() - 10, 10))
    WIN.blit(yellow_health_txt, (10, 10))

    WIN.blit(red_bullets_display, (WIDTH - red_bullets_display.get_width() - 12, 30))
    WIN.blit(yellow_bullets_display, (10, 30))

    WIN.blit(PrinceArnee, (yellow.x, yellow.y))
    WIN.blit(SecondPrince, (red.x, red.y))

    for bullet in red_bullets:
        pygame.draw.rect(WIN, RED, bullet)

    for bullet in yellow_bullets:
        pygame.draw.rect(WIN, YELLOW, bullet)

    pygame.display.update()

def movement(keys_pressed, yellow, red):
    if keys_pressed[pygame.K_a] and yellow.x - VEL >= 0:
        yellow.x -= VEL
    if keys_pressed[pygame.K_d] and yellow.x + VEL <= 430:
        yellow.x += VEL
    if keys_pressed[pygame.K_w] and yellow.y - VEL >= 0:
        yellow.y -= VEL
    if keys_pressed[pygame.K_s] and yellow.y + VEL <= 450:
        yellow.y += VEL

    if keys_pressed[pygame.K_j] and red.x - VEL >= 430:
        red.x -= VEL
    if keys_pressed[pygame.K_l] and red.x + VEL <= 850:
        red.x += VEL
    if keys_pressed[pygame.K_i] and red.y - VEL >= 0:
        red.y -= VEL
    if keys_pressed[pygame.K_k] and red.y + VEL <= 450:
        red.y += VEL

def handle_bullets(red_bullets, yellow_bullets, red, yellow):
    for bullet in yellow_bullets:
        bullet.x += BULLET_VEL
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)

    for bullet in red_bullets:
        bullet.x -= BULLET_VEL
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet)

def main():
    red = pygame.Rect(700, 300, PRINCE_WIDTH, PRINCE_HEIGHT)
    yellow = pygame.Rect(100, 300, PRINCE_WIDTH, PRINCE_HEIGHT)

    red_bullets = []
    yellow_bullets = []

    red_health = 10
    yellow_health = 10

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e and len(yellow_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height // 2 - 2, 10, 5)
                    yellow_bullets.append(bullet)
                    BULLET_FIRE_SOUND1.play()

                if event.key == pygame.K_o and len(red_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(red.x, red.y + red.height // 2 - 2, 10, 5)
                    red_bullets.append(bullet)
                    BULLET_FIRE_SOUND2.play()

            if event.type == RED_HIT:
                red_health -= 1
                BULLET_HIT_SOUND.play()

            if event.type == YELLOW_HIT:
                yellow_health -= 1
                BULLET_HIT_SOUND.play()

            winner_txt = ""
            winner_image = None

            if red_health <= 0:
                winner_txt = "ARNEE WINS"
                winner_image = PLAYER1_WINS_IMAGE

            if yellow_health <= 0:
                winner_txt = "ARNEE LOSES"
                winner_image = PLAYER2_WINS_IMAGE

            if winner_txt:
                draw_winner(winner_txt, winner_image)
                red_health = 10
                yellow_health = 10
                run = False

        keys_pressed = pygame.key.get_pressed()

        handle_bullets(red_bullets, yellow_bullets, red, yellow)

        movement(keys_pressed, yellow, red)

        draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health)

    pygame.quit()

if __name__ == "__main__":
    main()
