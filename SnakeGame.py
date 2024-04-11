import pygame
import cv2
import random
import time

pygame.init()

#Defining Colour
black=(0,0,0)
red =(255,0,0)
mustard =(255,200,100)
bluish=(100,75,125)
magenta=(255,0,255)
green=(100,255,100)


#DEFINING SCREEN WIDTH AND SCREEN HEIGHT
screen_width =1000
screen_height =700

#Setting up game intro


sound= pygame.mixer.Sound("sounds\\intro_video.mp3")
cap=cv2.VideoCapture("video\\Intro.mp4")
sound.play()
while True:
    ret,frame =cap.read()
    if ret == True:
        cv2.imshow("Narula Technologies",frame)
        if cv2.waitKey(25)==ord("q"):
            quit()
    else:
        break
cap.release()
cv2.destroyAllWindows()


#Creating Window
gameWindow =pygame.display.set_mode((screen_width,screen_height))

#CREATING CAPTION FOR GAME
pygame.display.set_caption(('Snake Game-:Narula Technologies'))



#DEFINING VARIABLE
run =True
ran_val=1
intro=1
snake_val=1
#Loading Image of frog
frog=pygame.image.load("photos\\frog.png")

#Loading Sounds
bye=pygame.mixer.Sound("sounds\\bye.mp3")
gameover=pygame.mixer.Sound("sounds\\gameover.mp3")
yummy=pygame.mixer.Sound("sounds\\yummy.mp3")
intro=pygame.mixer.Sound("sounds\\intro.mp3")
v_highest_score_m=pygame.mixer.Sound("sounds\\v_high_score.mp3")
SnakeHisses=pygame.mixer.Sound("sounds\\SnakeHisses.mp3")
back=pygame.mixer.music.load("sounds\\back.mp3")
clap=pygame.mixer.Sound("sounds\\clap.mp3")
#Play intro sound on game startup
intro.play()
#LOOP FOR GAME
while run:
    #gameWindow.blit(back_1,(0,0))
    
#Game variable
    exit_game = False
    game_over = False
    snake_x   = 45
    snake_y   = 55
    fps =25        #Frames Per Seconds
    food_x =random.randint(20,screen_width//3)
    food_y =random.randint(20,screen_height//3)
    score=0
    snake_size= 30
    snake_velocity_x =0
    snake_velocity_y=0
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("comicsans",60)
    running= False
    
    
    def text_screen(text,color,x,y):
        screen_text = font.render(text,True,color)
        gameWindow.blit(screen_text,[x,y])
    def text_screen1(text,color,x,y):
        screen_text = font.render(text,True,color)
        gameWindow.blit(screen_text,[x,y])
    def text_screen2(text,color,x,y):
        screen_text2 = font.render(text,True,color)
        gameWindow.blit(screen_text2,[x,y])   
    def plot_snake(gameWindow,color,snake_x,snake_y, snake_size):
        
        for x,y in list_1:
            pygame.draw.rect(gameWindow,color,[x,y,snake_size,snake_size])

    #SNAKE BODY
    list_1=[]
    snake_length =1
    collide_diff_x=0
    collide_diff_y=0

    #INNER LOOP FOR GAME.
    pygame.mixer.music.play(-1)
    runit=True
    while not exit_game:
        
        #USER QUITING
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                
                bye.play()
                time.sleep(2.5)
                exit_game =True
                run=False

            if game_over == True:
                exit_game=True
            if event.type == pygame.KEYDOWN and runit==True:
                
                if event.key == pygame.K_RIGHT:
                    if snake_length==1 or snake_velocity_x==0:
                        snake_velocity_x=12
                        snake_velocity_y=0
                

                if event.key == pygame.K_LEFT:
                    if snake_length==1 or snake_velocity_x==0:
                        snake_velocity_x=-12
                        snake_velocity_y=0
                    
                if event.key == pygame.K_DOWN:
                    if snake_length==1 or snake_velocity_y==0:
                        snake_velocity_x=0
                        snake_velocity_y=12

                if event.key == pygame.K_UP:
                    if snake_length==1 or snake_velocity_y==0:
                        snake_velocity_x=0
                        snake_velocity_y=-12
            
        runit=True
        #fOR RUNNING SNAKE ON SCREEN
        snake_x+=snake_velocity_x
        snake_y+=snake_velocity_y
        
        #WHEN SNAKE TOUCHES FOOD.
        if (abs(snake_x-food_x)<25 and abs(snake_y-food_y)<30)  :
            text_screen1('Yummy!!!',magenta,screen_width//2,screen_height//2)
            pygame.display.update()
            score+=1
            SnakeHisses.stop()
            SnakeHisses.play()
            yummy.play()
            #GENERATING FOOD RANDOM ON SCREEN
            food_x =random.randint(20,screen_width//2)
            food_y =random.randint(20,screen_height//2)
            #INCREASING SNAKE LENGTH
            snake_length+=2
        if snake_x==food_x+100 and snake_y==food_y+100 :
            text_screen1('Yummy!!!',magenta,screen_width//2,screen_height//2)
            pygame.display.update()
            score+=1
            yummy.play()
            #GENERATING FOOD RANDOM ON SCREEN
            food_x =random.randint(20,screen_width/2)
            food_y =random.randint(20,screen_height/2)
                
        #FILLING COLOR TO WINDOW
        if ran_val==1:
            gameWindow.fill(mustard)
        if ran_val==2:
            gameWindow.fill(bluish)
        #DISPLAYING SCORE ON WINDOW
        text_screen('Score-:'+str(score*10),magenta,5,5)
        
        #MAKING BODY OF SNAKE ON SCREEN
        head=[]
        head.append(snake_x)
        head.append(snake_y)
        list_1.append(head)

        #DELEATING EXTRA LENGTH PRODUCE BY SNAKE
        if len(list_1) > snake_length:
            del list_1[0]
        
        #PLOTING SNAKE ON SCREEN.
        plot_snake(gameWindow,green,snake_x,snake_y,snake_size)

        #DRAWING FOOD OF SNAKE ON SCREEN
        if snake_val==1:
            gameWindow.blit(frog,(food_x,food_y))
        if snake_val == 2:
            pygame.draw.rect(gameWindow,red,[food_x,food_y,snake_size,snake_size])
        
        #WHEN SNAKE TOUCHES BOUNDARY.GAME OVER!!!
        if snake_x > screen_width or snake_x <0 or snake_y > screen_height or snake_y <0:
            running=True
        if head in list_1[:-1]:
            running=True
        if running==True:  
            text_screen1('Game Over!!!',magenta,509,320)
            pygame.display.update()
            gameover.play()
            if ran_val ==1:
                ran_val=2
            elif ran_val ==2:
                ran_val=1
            gameWindow.fill(green)
            
            text_screen("Your Score-:",black,screen_width//4,screen_height//4)
            text_screen(str(score*10),red,screen_width//4+500,screen_height//4)
            text_screen("Highest Score-:",black,screen_width//4,screen_height//4+100)
            try:
                high_score=open("highest_score.txt","r")
                read_score=high_score.read()
                read_score=int(read_score)
            except:
                high_score=open("highest_score.txt","w")
                read_score=0
                high_score.write("0")
            if read_score < score*10:
                gameover.stop()
                high_score1=open("highest_score.txt","w")
                high_score1.write(str(score*10))           
                read_score=score*10
                clap.play()
                v_highest_score_m.play()
                high_score1.close()

            text_screen(str(read_score),red,screen_width//4+500,screen_height//4+100)
            high_score.close()
            pygame.display.update()           
            exit_game=True
            SnakeHisses.stop()
            time.sleep(3)
            clap.stop()
            snake_velocity_x=12

        pygame.display.update()
        clock.tick(fps)
        if intro ==1:            
            intro+=1
        
    
    
