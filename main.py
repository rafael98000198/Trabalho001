import pygame

print('Setup Start')
pygame.get_init()
window = pygame.display.set_mode(size=(800, 600))
print('Setup End')
a
print('Loop Start')
while True:
    # Check for all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  # Close window
            quit()  # End pygame
