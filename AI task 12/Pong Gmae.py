import pygame
import random

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Game Variables
PADDLE_WIDTH, PADDLE_HEIGHT = 15, 100
BALL_SIZE = 20

# Paddle positions
player_y = HEIGHT // 2 - PADDLE_HEIGHT // 2
opponent_y = HEIGHT // 2 - PADDLE_HEIGHT // 2
paddle_speed = 5

# Ball position and speed
ball_x = WIDTH // 2 - BALL_SIZE // 2
ball_y = HEIGHT // 2 - BALL_SIZE // 2
ball_speed_x = 5 * random.choice((1, -1))
ball_speed_y = 5 * random.choice((1, -1))

# Font for score
font = pygame.font.SysFont("Arial", 30)
player_score = 0
opponent_score = 0

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and player_y > 0:
        player_y -= paddle_speed
    if keys[pygame.K_DOWN] and player_y < HEIGHT - PADDLE_HEIGHT:
        player_y += paddle_speed

    # Opponent AI
    if opponent_y + PADDLE_HEIGHT // 2 < ball_y:
        opponent_y += paddle_speed
    if opponent_y + PADDLE_HEIGHT // 2 > ball_y:
        opponent_y -= paddle_speed

    # Move ball
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Collision with top and bottom
    if ball_y <= 0 or ball_y >= HEIGHT - BALL_SIZE:
        ball_speed_y *= -1

    # Collision with paddles
    if (ball_x <= PADDLE_WIDTH and player_y < ball_y < player_y + PADDLE_HEIGHT) or \
    (ball_x >= WIDTH - PADDLE_WIDTH - BALL_SIZE and opponent_y < ball_y < opponent_y + PADDLE_HEIGHT):
        ball_speed_x *= -1

    # Score update
    if ball_x < 0:
        opponent_score += 1
        ball_x, ball_y = WIDTH // 2, HEIGHT // 2
        ball_speed_x *= random.choice((1, -1))
        ball_speed_y *= random.choice((1, -1))

    if ball_x > WIDTH:
        player_score += 1
        ball_x, ball_y = WIDTH // 2, HEIGHT // 2
        ball_speed_x *= random.choice((1, -1))
        ball_speed_y *= random.choice((1, -1))

    # Drawing
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, (0, player_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.rect(screen, WHITE, (WIDTH - PADDLE_WIDTH, opponent_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.ellipse(screen, WHITE, (ball_x, ball_y, BALL_SIZE, BALL_SIZE))
    pygame.draw.aaline(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))

    # Display scores
    player_text = font.render(f"Player: {player_score}", True, WHITE)
    opponent_text = font.render(f"Opponent: {opponent_score}", True, WHITE)
    screen.blit(player_text, (50, 20))
    screen.blit(opponent_text, (WIDTH - 200, 20))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
