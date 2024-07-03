import pygame.locals
import time
import pygame

sheetx = 1920/4 - 147
sheety = 100
pianoy = 300
pianox = 1920/4
def draw_sheet(screen: pygame.Surface, clef: int, notes:int, accidental:int):
    screen.blit(img_clefs[clef], (sheetx,sheety))
    pass

def draw_piano(screen: pygame.Surface, width = 13):
    black_row = [1,1,0,1,1,1,0]
    for x in range(width):
        x -= width//2
        screen.blit(white_key, (x * 31 + pianox ,pianoy))
    for x in range(width):
        x -= width//2
        if black_row[x % 7]:
            screen.blit(black_key, (x * 31 + pianox + 21,pianoy + 5))
pygame.init()
screen = pygame.display.set_mode((1920/2,1080/2))
pygame.display.set_caption("learn_note")
screen.fill((255,255,255))
img_clefs = [pygame.image.load(filepath).convert_alpha()for filepath in ['img/bass_clef.png', 'img/treble_clef.png']]
downNote =  pygame.image.load("img/note_down.png").convert_alpha()
upNote =    pygame.image.load("img/note_up.png").convert_alpha()
sharp =     pygame.image.load("img/sharp.png").convert_alpha()
flat =      pygame.image.load("img/flat.png").convert_alpha()
black_key = pygame.image.load("img/black.png").convert_alpha()
white_key = pygame.image.load("img/white.png").convert_alpha()
draw_sheet(screen, 1, 1, 0)
draw_piano(screen)
pygame.display.update()
while True:
    # 迭代整個事件迴圈，若有符合事件則對應處理
    for event in pygame.event.get():
        # 當使用者結束視窗，程式也結束
        if event.type == pygame.locals.QUIT:
            pygame.quit()
            print("exit")
            exit()
    time.sleep(1)