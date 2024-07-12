import pygame
import random
import streamlit as st
from threading import Thread
import time
from PIL import Image

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Load images
elon_img = pygame.image.load('elon.png')
doge_img = pygame.image.load('dogecoin.png')

# Resize images
elon_img = pygame.transform.scale(elon_img, (80, 80))
doge_img = pygame.transform.scale(doge_img, (40, 40))

# Set up the display
screen = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))

# Game variables
elon_x = SCREEN_WIDTH // 2
elon_y = SCREEN_HEIGHT - 100
elon_speed = 5

doges = []
for i in range(5):
    x = random.randint(0, SCREEN_WIDTH - 40)
    y = random.randint(-100, -40)
    doges.append([x, y])

doge_speed = 2
score = 0

# Function to run the game loop
def game_loop():
    global elon_x, elon_y, score, running

    clock = pygame.time.Clock()
    while running:
        screen.fill(BLACK)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and elon_x > 0:
            elon_x -= elon_speed
        if keys[pygame.K_RIGHT] and elon_x < SCREEN_WIDTH - 80:
            elon_x += elon_speed
        
        for doge in doges:
            doge[1] += doge_speed
            if doge[1] > SCREEN_HEIGHT:
                doge[1] = random.randint(-100, -40)
                doge[0] = random.randint(0, SCREEN_WIDTH - 40)
            
            if elon_x < doge[0] < elon_x + 80 and elon_y < doge[1] < elon_y + 80:
                score += 1
                doge[1] = random.randint(-100, -40)
                doge[0] = random.randint(0, SCREEN_WIDTH - 40)
            
            screen.blit(doge_img, (doge[0], doge[1]))
        
        screen.blit(elon_img, (elon_x, elon_y))
        
        font = pygame.font.SysFont(None, 55)
        text = font.render(f'Score: {score}', True, WHITE)
        screen.blit(text, (10, 10))
        
        pygame.display.flip()
        clock.tick(30)

# Function to capture the Pygame screen as an image
def capture_frame():
    global running
    while running:
        time.sleep(0.1)
        pygame.image.save(screen, 'screenshot.jpg')

# Streamlit interface
def streamlit_interface():
    st.title("Elon Musk Eats Dogecoin")

    # Display the game screen in Streamlit
    while running:
        img = Image.open('screenshot.jpg')
        st.image(img)
        time.sleep(0.1)

if __name__ == '__main__':
    running = True
    
    # Start Pygame loop and screen capture in separate threads
    game_thread = Thread(target=game_loop)
    capture_thread = Thread(target=capture_frame)
    
    game_thread.start()
    capture_thread.start()
    
    # Run Streamlit interface
    streamlit_interface()
    
    # Clean up threads and Pygame resources
    running = False
    game_thread.join()
    capture_thread.join()
    pygame.quit()
