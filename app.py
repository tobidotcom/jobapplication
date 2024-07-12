import streamlit as st
import pygame
import random
import numpy as np
from pygame.locals import *

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Load images
player_img = pygame.image.load('player.png')
player_img = pygame.transform.scale(player_img, (50, 50))

enemy_img = pygame.image.load('enemy.png')
enemy_img = pygame.transform.scale(enemy_img, (50, 50))

bullet_img = pygame.image.load('bullet.png')
bullet_img = pygame.transform.scale(bullet_img, (10, 20))

# Initialize Pygame screen
screen = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))

# Game variables
player_x = SCREEN_WIDTH // 2
player_y = SCREEN_HEIGHT - 100
player_speed = 5

bullets = []
bullet_speed = 8

enemies = []
enemy_speed = 2
enemy_count = 6

# Initialize enemies
for i in range(enemy_count):
    enemy_x = random.randint(50, SCREEN_WIDTH - 100)
    enemy_y = random.randint(50, 200)
    enemies.append([enemy_x, enemy_y])

# Function to handle game logic and drawing
def run_game():
    global player_x, bullets, enemies, running, score

    clock = pygame.time.Clock()
    running = True
    score = 0

    while running:
        screen.fill(BLACK)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Player movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x < SCREEN_WIDTH - 50:
            player_x += player_speed

        # Shooting bullets
        if keys[pygame.K_SPACE]:
            bullets.append([player_x + 20, player_y])

        # Move bullets
        for bullet in bullets:
            bullet[1] -= bullet_speed

        # Move enemies and check collisions
        for enemy in enemies:
            enemy[1] += enemy_speed

            # Check collision with player
            if (player_x < enemy[0] < player_x + 50 and
                player_y < enemy[1] < player_y + 50):
                running = False

            # Check collision with bullets
            for bullet in bullets:
                if (bullet[0] < enemy[0] < bullet[0] + 10 and
                    bullet[1] < enemy[1] < bullet[1] + 20):
                    bullets.remove(bullet)
                    enemies.remove(enemy)
                    score += 1

        # Draw player
        screen.blit(player_img, (player_x, player_y))

        # Draw bullets
        for bullet in bullets:
            screen.blit(bullet_img, (bullet[0], bullet[1]))

        # Draw enemies
        for enemy in enemies:
            screen.blit(enemy_img, (enemy[0], enemy[1]))

        # Display score
        font = pygame.font.SysFont(None, 36)
        text = font.render(f'Score: {score}', True, WHITE)
        screen.blit(text, (10, 10))

        pygame.display.flip()
        clock.tick(30)

# Streamlit interface
def streamlit_interface():
    st.title("Space Invaders")
    st.write("Defeat the enemies and show your skills!")

    # Pygame canvas in Streamlit
    pygame_thread = st.empty()
    with pygame_thread:
        run_game()

    # After the game ends, display "HIRE ME! I'M TALENTED!"
    st.markdown("---")
    st.header("HIRE ME! I'M TALENTED!")
    st.write("Let's work together to create awesome things!")

# Run Streamlit interface
if __name__ == '__main__':
    streamlit_interface()

