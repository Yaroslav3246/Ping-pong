from pygame import *




class GameSprite(sprite.Sprite):
    def __init__(self, hero_image, hero_x, hero_y, width, height, hero_speed):
        super().__init__()
        self.image = transform.scale(image.load(hero_image), (width, height))
        self.speed = hero_speed
        self.rect = self.image.get_rect()
        self.rect.x = hero_x
        self.rect.y = hero_y

    

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update_L(self):
        
        Keys = key.get_pressed()
        if Keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if Keys[K_s] and self.rect.y < Win_height -80:
            self.rect.y += self.speed
        

    def update_R(self):
        
        Keys = key.get_pressed()
        if Keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if Keys[K_DOWN] and self.rect.y < Win_height -80:
            self.rect.y += self.speed


    
    


        



back = (255, 220, 178)
Win_width = 580
Win_height = 500
window = display.set_mode((Win_width, Win_height))
window.fill(back)

display.set_caption('Ping-pong ')
















game = True
finish = False
clock = time.Clock()
FPS = 90

ball = GameSprite('SHAR.png', 200, 200,40,50,5)
platforma1 = Player('IGROK.png', 30, 200, 20, 140, 7)
platforma2 = Player('IGROK.png', 520, 200, 20, 140, 7)

font.init()
font1 = font.Font(None, 40)

lose1 = font1.render("Player1 lose!!", True, (180, 0,0))
lose2 = font1.render("Player2 lose!!", True, (180, 0,0))


speed_x = 3
speed_y = 3


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False   
        
                    

                    

           
    if finish != True:
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        
        ball.reset()
        ball.update()
        
        platforma1.reset()
        platforma1.update_L()
        platforma2.reset()
        platforma2.update_R()

    if ball.rect.y > Win_height -40  or ball.rect.y < 0:   
        speed_y *= -1
    if sprite.collide_rect(platforma1, ball) or sprite.collide_rect(platforma2, ball):
        speed_x *= -1

    if ball.rect.x < 0:
        finish = True
        window.blit(lose1, (200,200)) 
    if ball.rect.x < 0:
        finish = True
        window.blit(lose1, (200,200)) 
        
        
    

    clock.tick(FPS)

    display.update()
    

        
