import pygame

pygame.init()

# Creating pygame window
window = pygame.display.set_mode((1200, 400))

# Initializing track no 1
track = pygame.image.load('track1.png')

# loading the car
car = pygame.image.load('tesla.png')
car = pygame.transform.scale(car, (30, 60))  # resizing the car
car_x = 150
car_y = 300
# clock
clock = pygame.time.Clock()

# Displaying window
while True:
    clock.tick(60)
    cam_x = car_x+15 # initializing camera cordinates
    cam_y = car_y+15
    # car_y = car_y-2
    window.blit(track, (0, 0))
    window.blit(car, (car_x, car_y))
    pygame.draw.circle(window, (0, 255, 0), (cam_x, cam_y), 5, 5)
    pygame.display.update()
