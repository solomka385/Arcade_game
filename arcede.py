from pygame import *
from random import *
from time import *
score1 = 0
class pyle(sprite.Sprite):
    def __init__(self, image1, x, y):
        sprite.Sprite.__init__(self) 
        self.image =transform.scale(image.load('C://Users/alex1/Desktop/arcade/pylew.png'),(80,80))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y  
    def update(self):
        if self.rect.y>30:
            self.rect.y= self.rect.y-4
                
        if self.rect.y<50:
            self.kill()            

class hero(pyle,sprite.Sprite):
    def __init__(self, image1, x, y,pyle):
        sprite.Sprite.__init__(self) 
        self.image =transform.scale(image.load('C://Users/alex1/Desktop/arcade/rocket.png'),(80,80))
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 500
    
    def go(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
        
        keys = key.get_pressed()
        if keys[K_LEFT]:
            if self.rect.x<10: 
                self.rect.x = self.rect.x 
            else: 
                self.rect.x -= 5
                
        elif keys[K_RIGHT]:
                
            if self.rect.x > 930:
                self.rect.x = self.rect.x
            else:
                self.rect.x += 5
                
        elif keys[K_UP]:
            if self.rect.y<15:
                self.rect.y = self.rect.y
            else:

                self.rect.y -= 10
            
        elif keys[K_DOWN]:
            if self.rect.y>710:
                self.rect.y = self.rect.y
            else:
                self.rect.y += 10
        
        window.blit(self.image,(self.rect.x,self.rect.y))
    def fire(self):
            k = pyle('C://Users/alex1/Desktop/arcade/pylew.png', self.rect.x, self.rect.y)
            pyles.add(k)

class enemy(sprite.Sprite):
    def __init__(self, image1, x, y):
        sprite.Sprite.__init__(self) 
        self.image =transform.scale(image.load('C://Users/alex1/Desktop/arcade/vragi2.png'),(80,80))
        self.rect = self.image.get_rect()
        self.rect.x = randint(20,950)
        
        self.rect.y = 5
    def update(self):
        global score1
        if self.rect.y>800:
            score1 += 1
            self.rect.y=2
            self.rect.x = randint(20,950)
            self.kill
            
        self.rect.y +=1
        window.blit(self.image,(self.rect.x,self.rect.y))
                
c = pyle('C://Users/alex1/Desktop/arcade/pylew.png',1,1)        

window = display.set_mode((1000,800 ))

# fon
background = image.load("C://Users/alex1/Desktop/arcade/cosmos.jpg")
background = transform.scale(background, (1000, 800))
display.set_caption("Шутер")
window.blit(background,(0,0))               
# hero
rocket = hero('C://Users/alex1/Desktop/arcade/rocket.png',400,500,c)
window.blit(rocket.image,(400,500))


#vrag
monsters = sprite.Group()
for i in range(1,6):
    
    monster = enemy('vragi2.png',randint(1,950),5)
    monsters.add(monster)

pyles = sprite.Group()





score = 0

font.init()
font = font.Font(None,36)



text = font.render('Счет: '+ str(score),1,(255,255,255))
window.blit(text,(10,20))
text1 = font.render('Счет: '+ str(score1),1,(255,255,255))
window.blit(text1,(10,70))



finish = False
run = True
while run:
    
    for e in event.get():
        if e.type == QUIT:
            run=False
        if e.type == KEYDOWN:
            if e.key == K_SPACE:
                rocket.fire()
    collides = sprite.groupcollide(monsters,pyles,True,True)
    for c in collides:
        monster = enemy('vragi2.png',randint(1,950),5)
        monsters.add(monster) 
        score += 1
    window.blit(background,(0,0)) 
    if not finish: 
                     
        rocket.go()
        

        
        text = font.render('Счет: '+ str(score),1,(255,255,255))
        
        text1 = font.render('Пропущено: '+ str(score1),1,(255,255,255))
        window.blit(text1,(10,70))
        window.blit(text,(10,20))
        s = sprite.spritecollide(rocket, monsters, True)
        pyles.update()
        monsters.update()
        
        monsters.draw(window)
        pyles.draw(window)
        
        
    if s or score1 == 5:
        background = image.load("lose1.png")
        background = transform.scale(background, (1000, 800))
        window.blit(background,(0,0))
        finish = True
        
        
    if score == 10:
        background = image.load("win1.jpg")
        background = transform.scale(background, (1000, 800))
        window.blit(background,(0,0))
        finish = True
    display.update()
        
         
            
    
