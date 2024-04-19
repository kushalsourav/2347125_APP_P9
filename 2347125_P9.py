import pygame
import random

# Initialize Pygame
pygame.init()

# Set up screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jet Plane Bombing Animation Game")

# Load images
jet_img = pygame.image.load('jett.png').convert_alpha()  # Load jet image with transparency
bomb_img = pygame.image.load('bomb.png').convert_alpha()  # Load bomb image with transparency
explosion_img = pygame.image.load('exp.png').convert_alpha()  # Load explosion image with transparency
house_img = pygame.image.load('house.png').convert_alpha()  # Load house image with transparency
jet_img = pygame.transform.scale(jet_img, (100, 100))
bomb_img = pygame.transform.scale(bomb_img, (60, 60))
house_img = pygame.transform.scale(house_img, (200, 200))
explosion_img = pygame.transform.scale(explosion_img, (140, 140))

# Jet attributes
jet_x = WIDTH // 2 - 50  # Start jet in the middle of the screen
jet_y = 50
jet_speed = 5

# Bomb attributes
bomb_x = 0
bomb_y = 0
bomb_speed = 10
bomb_dropped = False

# Explosion attributes
explosion_x = 0
explosion_y = 0
explosion_timer = 0

# Score
score = 0

# House position
house_x = random.randint(50, WIDTH - 250)  # Randomize the position of the house initially
house_y = HEIGHT - 250  # House always starts at the bottom

# Game loop
running = True
while running:
    # Fill the screen with white
    screen.fill((255, 255, 255))

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bomb_x = jet_x + 50
                bomb_y = jet_y + 100
                bomb_dropped = True

    # Continuous movement with key held down
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        jet_x -= jet_speed
    if keys[pygame.K_RIGHT]:
        jet_x += jet_speed

    # Ensure jet stays within the screen boundaries
    jet_x = max(0, min(WIDTH - 100, jet_x))

    # Move bomb
    if bomb_dropped:
        bomb_y += bomb_speed
        if bomb_y > HEIGHT:
            bomb_dropped = False

    # Check for collision with house
    if 200 < bomb_y < 400:
        # Simple collision detection, you can improve this
        if house_x < bomb_x < house_x + 200 and house_y < bomb_y < house_y + 200:
            explosion_x = bomb_x
            explosion_y = bomb_y
            explosion_timer = 30
            bomb_dropped = False
            score += 1  # Increment the score when bomb hits the house
            house_x = random.randint(50, WIDTH - 250)  # Randomize the position of the house after it's hit
            house_y = HEIGHT - 250  # House always appears at the bottom

    # Draw jet
    screen.blit(jet_img, (jet_x, jet_y))

    # Draw bomb
    if bomb_dropped:
        screen.blit(bomb_img, (bomb_x, bomb_y))

    # Draw explosion
    if explosion_timer > 0:
        screen.blit(explosion_img, (explosion_x, explosion_y))
        explosion_timer -= 1
    else:
        # Draw house if no explosion
        screen.blit(house_img, (house_x, house_y))

    # Display score
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    pygame.display.flip()

    # Set frame rate
    pygame.time.Clock().tick(30)

pygame.quit()
