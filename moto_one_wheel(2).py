import pygame,sys,math
pygame.init()
screen = pygame.display.set_mode([1000,800])
img = pygame.image.load('hoop1.png')
background=pygame.image.load('background6.png')

arrow_img=pygame.image.load('arrow.png')
arrow_img=pygame.transform.scale(arrow_img,(90,30))

img1=pygame.transform.scale(img,(75,75))# заявляю изображение
rect=screen.get_rect()
clock = pygame.time.Clock()
X,Y=102,681
delta=5

pi=math.pi
i=-1
angle=0
while True:
    i=i+1
    i1=i%220
    #i2=math.sqrt(i1)
    i2=math.pow(i1,1/2)
    angle=angle+5
    screen.blit(background,(-105,-65))
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    X=170+i1*delta
        
    if i1<120:
        Y=360-200*math.cos(pi*i1*delta/700)
        YY=360-200*math.cos(pi*(i1+1)*delta/700)
        angle1=(YY-Y)*9
        if i1==119:
            angle1=0
        #print('dY=',dY)
        
        Y1=Y
        arrow_img1=pygame.transform.scale(arrow_img,((1+i1),30))
        arrow_img2=pygame.transform.rotate(arrow_img1,-angle1)
        rect_arrow=arrow_img2.get_rect(center=(X,Y))
        i3=1+i1
        
    if i1>118:
        Y=Y1
        angle1=0
        #arrow_img2=pygame.transform.rotate(arrow_img2,-angle1)
        rect_arrow=arrow_img2.get_rect(center=(X,Y1))
        
    img2=pygame.transform.rotate(img1,-angle*(1+i2)/5)
    rect=img2.get_rect(center=(X,Y))
    screen.blit(img2,rect)
    screen.blit(arrow_img2,rect_arrow)
    if i1==219:
        angle=0
    #pygame.draw.rect(screen,'gold',rect,4)
    pygame.display.update()
    clock.tick(60)
    



    
    


 
 
