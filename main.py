import pygame
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *

def main():
    pygame.init()
    
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    
    clock = pygame.time.Clock()
    dt = 0
    
    #creating group
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updateable,drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable)
    
    #spawns player in the middle of the screen
    player1 = Player(SCREEN_WIDTH / 2 , SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    
    
    while True: 
        for event in pygame.event.get(): #checking if game is quit
            if event.type == pygame.QUIT:
                return
        
        
        updateable.update(dt)
        screen.fill("black")
        
        for d in drawable:
            d.draw(screen)
        pygame.display.flip()
        
        #pauses game loop for 1/60th of a second
        tick =  clock.tick(60)
        dt = tick / 1000
        
    
    #print("Starting Asteroids!")
    #print(f"Screen width: {SCREEN_WIDTH}")
    #print(f"Screen height: {SCREEN_HEIGHT}")
    

if __name__ == "__main__":
    main()