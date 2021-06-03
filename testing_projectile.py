'''
So. This is going to be a Game.

'''

# imports
import pygame
pygame.init()

# pygame init
WIN_SIZE = WIDTH, HEIGHT  = 1000, 600
win = pygame.display.set_mode(WIN_SIZE)
pygame.display.set_caption("First Game")

# vars 
red = (255, 0, 0)

x = WIDTH/6
y = HEIGHT/1.5
player_size = player_width, player_height = (40,64)
vel = 5

isJump = False
jumpCount = 10

shot = False




# mainloop
def main():
    #global playerpos
    global x
    global y
    global jumpCount
    global isJump
    global shot
    
    running = True
    while running:
        pygame.time.delay(20)
        
        # quitting the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # general movement
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_a] and x > 0:
            print("a pressed...")
            x -= vel
        if keys[pygame.K_d] and x < WIDTH - player_width:
            print("d pressed...")
            x +=  vel
        if not(isJump):
            if keys[pygame.K_w] and y > 0:
                print("w pressed...")
                y -= vel
            if keys[pygame.K_s] and y < HEIGHT - player_height:
                print("s pressed...")
                y += vel

            
            
            # jumping key
            if keys[pygame.K_SPACE]:
                print("space pressed...")
                isJump = True
        # jumping mechanic
        else:
            print("jumping...")
            if jumpCount >= -10:
                neg = 1 
                if jumpCount < 0:
                    neg = -1
                y -= (jumpCount ** 2) * 0.38 * neg
                jumpCount -= 1
            else:    
                isJump = False
                jumpCount = 10
                print("Jumped..")
        
        
        # shooting mechanic
        if keys[pygame.K_q]:
            shot = True
            print("q pressed")        
        
        
        
        # updating the screen
        win.fill((0,0,0))
        pygame.draw.rect(win, red, ((x,y), player_size))
        if shot == True:
            (ballX, ballY) = (int(x), int(y))
            pygame.draw.circle(win, red, (ballX, ballY), 8)
            
        pygame.display.update()    
    
        


main()
pygame.quit()

