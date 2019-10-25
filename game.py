import sys,pygame,math,time,random
def square(x,y,color,pix):
    for i in range(x-10,x+10):
        for j in range (y-10,y+10):
            pix[i][j]=color
white=(255,255,255)
black=(0,0,0)
red=(150,0,0)
green=(0,150,0)
bleu=(0,0,150)
yellow=(150,150,0)
pink=(200,0,200)
bright_yellow=(255,255,0)
bright_bleu=(0,0,255)
bright_red=(255,0,0)
bright_green=(0,255,0)
bright_pink=(255,0,255)
pygame.init()
pygame.mixer.music.load("m.mp3")
display_width=800
display_height=600
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("snake")
clock= pygame.time.Clock ()
gameDisplay.fill(white)
def text_objects(text,font,cou=black):
    textSurface=font.render(text,True,cou)
    return textSurface,textSurface.get_rect()
def botton(msg,x,y,w,h,ic,ac,action=None,t=(),cou=black):
    mouse = pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    if x+w>mouse[0]>x and y+h>mouse[1]>y:
        pygame.draw.rect(gameDisplay,ac,(x,y,w,h))
        if click[0]==1 and action!=None :
            if action=='one':
                one()
            elif action=='quit':
                pygame.quit()
                sys.exit()
            elif action=='two':
                two()
            elif action=='help':
                help()
            elif action=='back':
                time.sleep(1)
                intro()
            elif action=="continue":
                return(True)
            elif action=="pc":
                pc()
    else:
        pygame.draw.rect(gameDisplay,ic,(x,y,w,h))
    smallText=pygame.font.SysFont("comicsansms",20)
    textSurf,textRect=text_objects(msg,smallText,cou)
    textRect.center=((x+(w/2),(y+(h/2))))
    gameDisplay.blit(textSurf,textRect)
def pause():
    pygame.mixer.music.pause()
    while True :
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN :
                if event.key==pygame.K_ESCAPE:
                    pygame.mixer.music.unpause()
                    return(0)
        gameDisplay.fill(white)
        largeText=pygame.font.SysFont("comicsansms",115)
        TextSurf,TextRect=text_objects('paused',largeText)
        TextRect.center=((display_width/2),(display_height/8))
        gameDisplay.blit(TextSurf,TextRect)
        t=botton('continue',350,325,150,50,bleu,bright_bleu,'continue')
        botton('quit!',350,525,150,50,red,bright_red,'quit')
        botton('main menu',350,425,150,50,yellow,bright_yellow,'back')
        if t==True:
            pygame.mixer.music.unpause()
            return(0)
        pygame.display.update()
        clock.tick(15)
    
def help():
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
        gameDisplay.fill(white)
        largeText=pygame.font.SysFont("comicsansms",20)
        TextSurf,TextRect=text_objects("1/avoide the edges or lose",largeText)
        TextRect.center=((display_width/2),(100))
        gameDisplay.blit(TextSurf,TextRect)
        TextSurf,TextRect=text_objects("2/eat circels to increase score",largeText)
        TextRect.center=((display_width/2),(150))
        gameDisplay.blit(TextSurf,TextRect)
        TextSurf,TextRect=text_objects("3/as your score increase your speed increases ",largeText)
        TextRect.center=((display_width/2),(200))
        gameDisplay.blit(TextSurf,TextRect)
        botton('return',350,325,150,50,yellow,bright_yellow,'back')
        pygame.display.update()
        pygame.event.pump()
def intro():
    while True :
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
        gameDisplay.fill(white)
        largeText=pygame.font.SysFont("comicsansms",115)
        TextSurf,TextRect=text_objects('snake',largeText)
        TextRect.center=((display_width/2),(display_height/8))
        gameDisplay.blit(TextSurf,TextRect)
        botton('one player',100,225,200,50,green,bright_green,'one')
        botton('two players',100,325,200,50,bleu,bright_bleu,'two')
        botton('quit!',300,425,200,50,red,bright_red,'quit')
        botton('help!',500,325,200,50,yellow,bright_yellow,'help')
        botton('VS PC!',500,225,200,50,pink,bright_pink,'pc')
        pygame.display.update()
        clock.tick(15)
def one():
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(-1)
    l=[[display_width//2,display_height//2,1]]
    score=0
    dead=False
    x=random.randint(110,685)
    y=random.randint(115,490)
    while (dead==False):
        pix=pygame.PixelArray(gameDisplay)
        gameDisplay.fill(white)
        square(l[0][0],l[0][1],black,pix)
        pygame.draw.line(gameDisplay,black,((95,100)),(95,500),10)
        pygame.draw.line(gameDisplay,black,((91,100)),(695,100),10)
        pygame.draw.line(gameDisplay,black,((91,500)),(695,500),10)
        pygame.draw.line(gameDisplay,black,((695,96)),(695,505),10)
        pygame.draw.circle(gameDisplay,black,(x,y),8)
        if (abs(l[0][0]-x)<10) and (abs(l[0][1]-y)<10):
            score=score+1
            x=random.randint(110,685)
            y=random.randint(115,490)
        pix=None
        scoremsg="score="+str(score)
        botton(scoremsg,0,0,80,30,white,white)
        for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type==pygame.KEYDOWN :
                    if event.key==pygame.K_ESCAPE:
                        adjnsjdn=pause()
                    if (event.key==pygame.K_RIGHT) and (l[0][2]!=2):
                        l[0][2]=1
                    elif (event.key==pygame.K_LEFT) and (l[0][2]!=1):
                        l[0][2]=2
                    elif (event.key==pygame.K_UP) and (l[0][2]!=3):
                        l[0][2]=4
                    elif (event.key==pygame.K_DOWN) and (l[0][2]!=4):
                        l[0][2]=3
        if l[0][2]==1:
            l[0][0]=l[0][0]+5
        elif l[0][2]==2:
            l[0][0]=l[0][0]-5
        elif l[0][2]==3:
            l[0][1]=l[0][1]+5
        elif l[0][2]==4:
            l[0][1]=l[0][1]-5
        pygame.event.pump()
        clock.tick(10+2*score)
        pygame.display.update()
        if (l[0][0]<110) or(l[0][0]>685) or (l[0][1]<115) or(l[0][1]>490):
            dead=True
            time.sleep(2)
            pygame.mixer.music.stop()
def pc():
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(-1)
    wait=0
    l=[[display_width//4,display_height//2,1]]
    l2=[[(3*display_width)//4,display_height//2,2]]
    score=0
    score2=0
    dead=False
    dead2=False
    x=random.randint(110,685)
    y=random.randint(115,490)
    while (dead==False) or (dead2==False):
        pix=pygame.PixelArray(gameDisplay)
        gameDisplay.fill(white)
        square(l[0][0],l[0][1],red,pix)
        square(l2[0][0],l2[0][1],bleu,pix)
        pygame.draw.line(gameDisplay,black,((95,100)),(95,500),10)
        pygame.draw.line(gameDisplay,black,((91,100)),(695,100),10)
        pygame.draw.line(gameDisplay,black,((91,500)),(695,500),10)
        pygame.draw.line(gameDisplay,black,((695,96)),(695,505),10)
        pygame.draw.circle(gameDisplay,black,(x,y),8)
        if (abs(l[0][0]-x)<10) and (abs(l[0][1]-y)<10):
            score=score+1
            x=random.randint(110,685)
            y=random.randint(115,490)
        elif (abs(l2[0][0]-x)<10) and (abs(l2[0][1]-y)<10):
            score2=score2+1
            x=random.randint(110,685)
            y=random.randint(115,490)
            wait=math.trunc(score2)
        pix=None
        scoremsg="score="+str(score)
        botton(scoremsg,0,0,80,30,white,white,None,(),red)
        scoremsg2="score="+str(score2)
        botton(scoremsg2,710,0,80,30,white,white,None,(),bleu)
        for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type==pygame.KEYDOWN :
                    if event.key==pygame.K_ESCAPE:
                        adjnsjdn=pause()
                    if (event.key==pygame.K_RIGHT) and (l[0][2]!=2):
                        l[0][2]=1
                    elif (event.key==pygame.K_LEFT) and (l[0][2]!=1):
                        l[0][2]=2
                    elif (event.key==pygame.K_UP) and (l[0][2]!=3):
                        l[0][2]=4
                    elif (event.key==pygame.K_DOWN) and (l[0][2]!=4):
                        l[0][2]=3
        if (wait<=0) and (dead2==False):
            if (l2[0][0]-x<-10) and (l2[0][2]!=2):
                l2[0][2]=1
            if (l2[0][0]-x>10) and (l2[0][2]!=1):
                l2[0][2]=2
            if (l2[0][1]-y<-10) and (l2[0][2]!=4):
                l2[0][2]=3
            if (l2[0][1]-y>10) and (l2[0][2]!=3):
                l2[0][2]=4
            if (l2[0][0]-x<-10) and (l2[0][2]==2):
                l2[0][2]=3
            if (l2[0][0]-x>10) and (l2[0][2]==1):
                l2[0][2]=4
            if (l2[0][1]-y<-10) and (l2[0][2]==4):
                l2[0][2]=1
            if (l2[0][1]-y>10) and (l2[0][2]==3):
                l2[0][2]=2
        wait=wait-1
        if (l[0][2]==1) and (dead==False):
            l[0][0]=l[0][0]+5
        elif (l[0][2]==2) and (dead==False):
            l[0][0]=l[0][0]-5
        elif (l[0][2]==3) and (dead==False):
            l[0][1]=l[0][1]+5
        elif (l[0][2]==4) and (dead==False):
            l[0][1]=l[0][1]-5
        if (l2[0][2]==1) and (dead2==False):
            l2[0][0]=l2[0][0]+5
        elif (l2[0][2]==2) and (dead2==False):
            l2[0][0]=l2[0][0]-5
        elif (l2[0][2]==3) and (dead2==False):
            l2[0][1]=l2[0][1]+5
        elif (l2[0][2]==4) and (dead2==False):
            l2[0][1]=l2[0][1]-5
        pygame.event.pump()
        clock.tick(10+2*(score+score2))    
        pygame.display.update()
        if (l[0][0]<110) or(l[0][0]>685) or (l[0][1]<115) or(l[0][1]>490):
            dead=True
        if (l2[0][0]<110) or(l2[0][0]>685) or (l2[0][1]<115) or(l2[0][1]>490):
            dead2=True
    time.sleep(2)
    pygame.mixer.music.stop()
def two():
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(-1)
    l=[[display_width//4,display_height//2,1]]
    l2=[[(3*display_width)//4,display_height//2,2]]
    score=0
    score2=0
    dead=False
    dead2=False
    x=random.randint(110,685)
    y=random.randint(115,490)
    while (dead==False) or (dead2==False):
        pix=pygame.PixelArray(gameDisplay)
        gameDisplay.fill(white)
        square(l[0][0],l[0][1],red,pix)
        square(l2[0][0],l2[0][1],bleu,pix)
        pygame.draw.line(gameDisplay,black,((95,100)),(95,500),10)
        pygame.draw.line(gameDisplay,black,((91,100)),(695,100),10)
        pygame.draw.line(gameDisplay,black,((91,500)),(695,500),10)
        pygame.draw.line(gameDisplay,black,((695,96)),(695,505),10)
        pygame.draw.circle(gameDisplay,black,(x,y),8)
        if (abs(l[0][0]-x)<10) and (abs(l[0][1]-y)<10):
            score=score+1
            x=random.randint(110,685)
            y=random.randint(115,490)
        elif (abs(l2[0][0]-x)<10) and (abs(l2[0][1]-y)<10):
            score2=score2+1
            x=random.randint(110,685)
            y=random.randint(115,490)
        pix=None
        scoremsg="score="+str(score)
        botton(scoremsg,0,0,80,30,white,white,None,(),red)
        scoremsg2="score="+str(score2)
        botton(scoremsg2,710,0,80,30,white,white,None,(),bleu)
        for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type==pygame.KEYDOWN :
                    if event.key==pygame.K_ESCAPE:
                        adjnsjdn=pause()
                    if (event.key==pygame.K_RIGHT) and (l[0][2]!=2):
                        l[0][2]=1
                    elif (event.key==pygame.K_LEFT) and (l[0][2]!=1):
                        l[0][2]=2
                    elif (event.key==pygame.K_UP) and (l[0][2]!=3):
                        l[0][2]=4
                    elif (event.key==pygame.K_DOWN) and (l[0][2]!=4):
                        l[0][2]=3
                    if (event.key==pygame.K_d) and (l2[0][2]!=2):
                        l2[0][2]=1
                    elif (event.key==pygame.K_a) and (l2[0][2]!=1):
                        l2[0][2]=2
                    elif (event.key==pygame.K_w) and (l2[0][2]!=3):
                        l2[0][2]=4
                    elif (event.key==pygame.K_s) and (l2[0][2]!=4):
                        l2[0][2]=3
        if (l[0][2]==1) and (dead==False):
            l[0][0]=l[0][0]+5
        elif (l[0][2]==2) and (dead==False):
            l[0][0]=l[0][0]-5
        elif (l[0][2]==3) and (dead==False):
            l[0][1]=l[0][1]+5
        elif (l[0][2]==4) and (dead==False):
            l[0][1]=l[0][1]-5
        if (l2[0][2]==1) and (dead2==False):
            l2[0][0]=l2[0][0]+5
        elif (l2[0][2]==2) and (dead2==False):
            l2[0][0]=l2[0][0]-5
        elif (l2[0][2]==3) and (dead2==False):
            l2[0][1]=l2[0][1]+5
        elif (l2[0][2]==4) and (dead2==False):
            l2[0][1]=l2[0][1]-5
        pygame.event.pump()
        clock.tick(10+2*(score+score2))    
        pygame.display.update()
        if (l[0][0]<110) or(l[0][0]>685) or (l[0][1]<115) or(l[0][1]>490):
            dead=True
        if (l2[0][0]<110) or(l2[0][0]>685) or (l2[0][1]<115) or(l2[0][1]>490):
            dead2=True
    time.sleep(2)
    pygame.mixer.music.stop()
intro()
