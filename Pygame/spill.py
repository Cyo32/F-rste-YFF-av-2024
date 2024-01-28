import pygame
import sys
 
pygame.init()
 
WIDTH, HEIGHT = 800, 600
FPS = 60
 
bg = r"C:\Users\fredr\OneDrive - Viken fylkeskommune\1IMA\YFF\Pygame\IMG\bakgrunn.png"
img = r"C:\Users\fredr\OneDrive - Viken fylkeskommune\1IMA\YFF\Pygame\IMG\karakter.png"
img2 = r"C:\Users\fredr\OneDrive - Viken fylkeskommune\1IMA\YFF\Pygame\IMG\eksplosjon.png"
landmine = r"C:\Users\fredr\OneDrive - Viken fylkeskommune\1IMA\YFF\Pygame\IMG\mine.png"
player_transformed = False
collision_time = 0
 
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        ogimg = pygame.image.load(img).convert_alpha()
        self.image = pygame.transform.scale(ogimg, (25, 40))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, 490)
        self.move = True
 
    def update(self):
        if self.rect.top == 0:
            print("Du greide å komme deg ut!")
            pygame.quit()
            sys.exit()
 
        global img
        if self.move == True:
            keys = pygame.key.get_pressed()
            previous_rect = self.rect.copy()
            if keys[pygame.K_a] and self.rect.left > 0:
                self.rect.x -= 5
            if keys[pygame.K_d] and self.rect.right < WIDTH:
                self.rect.x += 5
            if keys[pygame.K_w] and self.rect.top > 0:
                self.rect.y -= 5
            if keys[pygame.K_s] and self.rect.bottom < HEIGHT:
                self.rect.y += 5
       
        collisions = pygame.sprite.spritecollide(self, collidable_sprites, False)
        if collisions:
            self.rect = previous_rect
 
        explode = pygame.sprite.spritecollide(self, land_mines, False)
        global img2
        global collision_time
        global player_transformed
 
        if explode and not player_transformed:
            player_transformed = True
            self.move = False
            self.image = pygame.image.load(img2).convert_alpha()
            self.image = pygame.transform.scale(self.image, (150, 200))
            collision_time = pygame.time.get_ticks()
 
        if player_transformed and pygame.time.get_ticks() - collision_time > 1000:
            print("Du tapte!")
            pygame.quit()
            sys.exit()
 
class CollidableRectangle(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color, alpha=0):
        super().__init__()
        self.image = pygame.Surface((width, height), pygame.SRCALPHA)
        self.image.fill((color[0], color[1], color[2], alpha))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
 
rect1 = CollidableRectangle(140, 135, 135, 60, (255, 0, 0))  
rect2 = CollidableRectangle(290, 40, 94, 30, (0, 255, 0))
rect3 = CollidableRectangle(550, 45, 100, 30, (0, 0, 255))
rect4 = CollidableRectangle(32, 318, 83, 20, (0, 0, 2))
rect5 = CollidableRectangle(695, 318, 90, 10, (0, 0, 2))
rect6 = CollidableRectangle(535, 180, 93, 20, (0, 0, 2))
rect7 = CollidableRectangle(312, 170, 112, 20, (0, 0, 2))
rect8 = CollidableRectangle(306, 120, 45, 50, (0, 0, 2))
rect9 = CollidableRectangle(384, 120, 45, 50, (0, 0, 2))
rect10 = CollidableRectangle(350, 420, 90, 50, (0, 0, 2))
rect11 = CollidableRectangle(150, 255, 48, 24, (0, 0, 2))
rect12 = CollidableRectangle(0, 160, 90, 30, (0, 0, 2))
rect13 = CollidableRectangle(450, 30, 44, 45, (0, 0, 2))
rect14 = CollidableRectangle(575, 120, 55, 70, (0, 0, 2))
rect15 = CollidableRectangle(476, 120, 55, 70, (0, 0, 2))
rect16 = CollidableRectangle(520, 145, 55, 55, (0, 0, 2))
rect17 = CollidableRectangle(607, 250, 450, 20, (0, 0, 2))
rect18 = CollidableRectangle(678, 130, 450, 20, (0, 0, 2))
rect19 = CollidableRectangle(0, 510, 800, 110, (0, 0, 2))
collidable_rect1 = CollidableRectangle(0, 0, 180, 70, (255, 0, 0))
collidable_rect2 = CollidableRectangle(180, 0, 200, 30, (0, 255, 0))
collidable_rect3 = CollidableRectangle(416, 0, 400, 30, (0, 0, 255))
collidable_rect4 = CollidableRectangle(127, 420, 165, 15, (0, 255, 255))
collidable_rect5 = CollidableRectangle(475, 419, 165, 15, (255, 0, 255))
collidable_rect6 = CollidableRectangle(230, 252, 340, 100, (255, 255, 255))
 
class mines(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, landmine):
        super().__init__()
        self.image = pygame.image.load(landmine)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
 
mine1 = mines(10, 100, 20, 20, landmine)
mine2 = mines(400, 100, 20, 20, landmine)
mine3 = mines(670, 420, 20, 20, landmine)
mine4 = mines(580, 250, 20, 20, landmine)
mine5 = mines(310, 420, 20, 20, landmine)
mine6 = mines(200, 300, 20, 20, landmine)
 
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Røm fra Nord Korea!")
clock = pygame.time.Clock()
 
all_sprites = pygame.sprite.Group()
collidable_sprites = pygame.sprite.Group()
land_mines = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
 
collidable_sprites.add(rect1, rect2, rect3, rect4, rect5, rect6, rect7, rect8, rect9, rect10, rect11, rect12, rect13, rect14, rect15, rect16, rect17, rect18, rect19, collidable_rect1, collidable_rect2, collidable_rect3, collidable_rect4, collidable_rect5, collidable_rect6)
all_sprites.add(collidable_sprites)
 
 
land_mines.add(mine1, mine2, mine3, mine4, mine5, mine6)
all_sprites.add(land_mines)
 
bg_image = pygame.image.load(bg).convert()
bg_image = pygame.transform.scale(bg_image, (WIDTH, HEIGHT))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
 
    all_sprites.update()
    screen.blit(bg_image, (0, 0))
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(FPS)