from pygame import *
from random import randint
#NCT_127-Orange_Seoul_Instrumental

init()

mixer.init()
print("Choose between: ")
print("1. NCT127- Orange Seoul,")
print("2. Aespa- Drama,")
print("3. Eve- Kaikai Kitan.")
music_choice = int(input(">>>"))
if music_choice == 1:
    music = "NCT_127-Orange_Seoul_Instrumental.mp3"
    exitProg = False
elif music_choice == 2:
    music = "aespa-Drama_Instrumental.mp3"
    exitProg = False
elif music_choice == 3:
    music = "Kaikai_Kitan-Eve_Instrumental.mp3"
    exitProg = False

mixer.music.load(music)
mixer.music.set_volume(0.3)
mixer.music.play(-1)


width = 700
height = 600
window = display.set_mode((width, height))
display.set_caption("Pac-Man")
screen = display.get_surface()

ghost_change_timer = 0

pointTotal = 0
maxPoints = 880

deathTotal = 0
maxDeaths = 4

walls = [Rect(0,0,700,6), Rect(0,594,700,6),  #horizontal
         Rect(0,0,6,250), Rect(694,0,6,250),  #vertical top
         Rect(0,350,6,250), Rect(694,350,6,250),  #vertical bottom

         Rect(80,70,220,2), Rect(80,70,2,195),  #top left corner(1.1)
         Rect(95,85,205,2), Rect(95,85,2,180),  #top corner(1.2)
         Rect(300,70,2,17), Rect(80,265,17,2),  #top corner(1.2)

         Rect(150,140,80,2), Rect(150,220,80,2),  #top left corner(2.1.1)
         Rect(165,155,50,2), Rect(165,205,50,2),  #top left corner(2.1.1)
         Rect(150,140,2,80), Rect(230,140,2,82),  #top left corner(2.2.1)
         Rect(165,155,2,50), Rect(215,155,2,52),  #top left corner(2.2.1)

         Rect(400,70,220,2), Rect(620,70,2,196),  #top right corner(1.1)
         Rect(400,85,205,2), Rect(605,85,2,180),  #top right corner(1.2)
         Rect(400,70,2,17), Rect(605,265,17,2),  #top right corner(1.2)

         Rect(470, 140, 80, 2), Rect(470, 220, 80, 2),  # top right corner(2.1.1)
         Rect(485, 155, 50, 2), Rect(485, 205, 50, 2),  # top right corner(2.1.1)
         Rect(470, 140, 2, 80), Rect(550, 140, 2, 82),  # top right corner(2.2.1)
         Rect(485, 155, 2, 50), Rect(535, 155, 2, 52),  # top right corner(2.2.1)

         Rect(80, 530, 220, 2), Rect(80, 335, 2, 195),  # bottom left corner(1.1)
         Rect(95, 515, 205, 2), Rect(95, 335, 2, 180),  # bottom corner(1.2)
         Rect(300, 515, 2, 17), Rect(80, 335, 17, 2),  # bottom corner(1.2)

         Rect(150, 380, 80, 2), Rect(150, 460, 80, 2),  # bottom left corner(2.1.1)
         Rect(165, 395, 50, 2), Rect(165, 445, 50, 2),  # bottom left corner(2.1.1)
         Rect(150, 380, 2, 80), Rect(230, 380, 2, 82),  # bottom left corner(2.2.1)
         Rect(165, 395, 2, 50), Rect(215, 395, 2, 52),  # bottom left corner(2.2.1)

         Rect(400, 530, 220, 2), Rect(620, 335, 2, 196),  # bottom right corner(1.1)
         Rect(400, 515, 206, 2), Rect(605, 335, 2, 180),  # bottom right corner(1.2)
         Rect(400, 515, 2, 17), Rect(605, 335, 17, 2),  # bottom right corner(1.2)

         Rect(470, 380, 80, 2), Rect(470, 460, 80, 2),  # bottom right corner(2.1.1)
         Rect(485, 395, 50, 2), Rect(485, 445, 50, 2),  # bottom right corner(2.1.1)
         Rect(470, 380, 2, 80), Rect(550, 380, 2, 82),  # bottom right corner(2.2.1)
         Rect(485, 395, 2, 50), Rect(535, 395, 2, 52),  # bottom right corner(2.2.1)
         ]
points = [Rect(32,30,16,16), Rect(32,104,16,16), Rect(32,178,16,16), Rect(32,252,16,16),
          Rect(32,326,16,16), Rect(32,400,16,16), Rect(32,474,16,16), Rect(32,548,16,16),
          Rect(652, 30, 16, 16), Rect(652, 104, 16, 16), Rect(652, 178, 16, 16), Rect(652, 252, 16, 16),
          Rect(652, 326, 16, 16), Rect(652, 400, 16, 16), Rect(652, 474, 16, 16), Rect(652, 548, 16, 16),

          Rect(122,30,16,16), Rect(212,30,16,16), Rect(302,30,16,16),
          Rect(392,30,16,16), Rect(482,30,16,16), Rect(572,30,16,16),
          Rect(122, 548, 16, 16), Rect(212, 548, 16, 16), Rect(302, 548, 16, 16),
          Rect(392, 548, 16, 16), Rect(482, 548, 16, 16), Rect(572, 548, 16, 16),

          Rect(32,30,16,16), Rect(32,104,16,16), Rect(32,178,16,16), Rect(32,252,16,16),
          Rect(32,326,16,16), Rect(32,400,16,16), Rect(32,474,16,16), Rect(32,548,16,16),
          Rect(652, 30, 16, 16), Rect(652, 104, 16, 16), Rect(652, 178, 16, 16), Rect(652, 252, 16, 16),
          Rect(652, 326, 16, 16), Rect(652, 400, 16, 16), Rect(652, 474, 16, 16), Rect(652, 548, 16, 16)
          ]
#Characters
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
#Pacman, RGhost, BGhost, PGhost, OGhost
PacmanImg = image.load("pacman.png")
PacmanImg = transform.scale(PacmanImg, (40, 40))
RGhostImg = image.load("redGhost.png")
RGhostImg = transform.scale(RGhostImg, (30, 40))
BGhostImg = image.load("blueGhost.png")
BGhostImg = transform.scale(BGhostImg, (30, 40))
PGhostImg = image.load("pinkGhost.png")
PGhostImg = transform.scale(PGhostImg, (30, 40))
OGhostImg = image.load("orangeGhost.png")
OGhostImg = transform.scale(OGhostImg, (30, 40))
Pacman = Rect(400, 200, 40, 40)
RGhost = Rect(400, 330, 30, 40)
BGhost = Rect(450, 330, 30, 40)
PGhost = Rect(500, 330, 30, 40)
OGhost = Rect(550, 330, 30, 40)

# Game loop
px=0
py=0
grx=0
gry=0
gbx=0
gby=0
gpx=0
gpy=0
gox=0
goy=0
directions = [-1, 0, 1]
while exitProg == False:
    time.delay(5)
    screen.fill((100, 100, 100))
    for wall in walls:
        draw.rect(screen, BLUE, wall)
    for point in points:
        draw.rect(screen, YELLOW, point)
    for e in event.get():
        if e.type == QUIT:
            exitProg = True
        if e.type == KEYDOWN:  # if someone presses a key down
            if e.key == K_LEFT:
                px = -1
            elif e.key == K_RIGHT:
                px = 1
            elif e.key == K_UP:
                py = -1
            elif e.key == K_DOWN:
                py = 1
        if e.type == KEYUP:
            if e.key == K_LEFT or e.key == K_RIGHT:
                px = 0
            elif e.key == K_UP or e.key == K_DOWN:
                py = 0

    ghost_change_timer += 1
    if ghost_change_timer > 30:
        ghost_change_timer = 0
        grx = randint(-1,1)
        gry = randint(-1,1)
        gbx = randint(-1,1)
        gby = randint(-1,1)
        gpx = randint(-1,1)
        gpy = randint(-1,1)
        gox = randint(-1,1)
        goy = randint(-1,1)


    if Pacman.x + px <= 0:
        px = 0
        if py <= 350 or py >= 250:
            Pacman.x = 654
            px = 0
    if Pacman.x + px >= width - 45:
        px = 0
        if py <= 250 or py >= 350:
            Pacman.x = 0
            px = 1
    if Pacman.y + py <= 0:
        py = 0
    if Pacman.y + py >= height -45:
        py = 0



    if RGhost.x + grx <= 0:
        grx = randint(-1,1)
        if gry <= 300 or gry >= 400:
            RGhost.x = 955
            grx = -1
    if RGhost.x + grx >= width - 45:
        grx = randint(-1,1)
        if gry <= 300 or gry >= 400:
            RGhost.x = 0
            grx = 1
    if RGhost.y + gry <= 0:
        gry = randint(-1,1)
    if RGhost.y + gry >= height -45:
        gry = randint(-1,1)



    if BGhost.x + gbx <= 0:
        gbx = 0
        if gby <= 300 or gby >= 400:
            BGhost.x = 955
            gbx = -1
    if BGhost.x + gbx >= width - 45:
        gbx = 0
        if gby <= 300 or gby >= 400:
            BGhost.x = 0
            gbx = 1
    if BGhost.y + gby <= 0:
        gby = 0
    if BGhost.y + gby >= height -45:
        gby = 0


    if PGhost.x + gpx <= 0:
        gpx = 0
        if gpy <= 300 or gpy >= 400:
            PGhost.x = 955
            gpx = -1
    if PGhost.x + gpx >= width - 45:
        gpx = 0
        if gpy <= 300 or gpy >= 400:
            PGhost.x = 0
            gpx = 1
    if PGhost.y + gpy <= 0:
        gpy = 0
    if PGhost.y + gpy >= height -45:
        gpy = 0


    if OGhost.x + gox <= 0:
        gox = 0
        if goy <= 300 or goy >= 400:
            OGhost.x = 955
            gox = -1
    if OGhost.x + gox >= width - 45:
        gox = 0
        if goy <= 300 or goy >= 400:
            OGhost.x = 0
            gox = 1
    if OGhost.y + goy <= 0:
        goy = 0
    if OGhost.y + goy >= height -45:
        goy = 0

    if Pacman.colliderect(RGhost):
        Pacman.x, Pacman.y = 20, 20
        deathTotal = deathTotal + 1
        print(deathTotal)
    if Pacman.colliderect(BGhost):
        Pacman.x, Pacman.y = 20, 20
        deathTotal = deathTotal + 1
        print(deathTotal)
    if Pacman.colliderect(PGhost):
        Pacman.x, Pacman.y = 20, 20
        deathTotal = deathTotal + 1
        print(deathTotal)
    if Pacman.colliderect(OGhost):
        Pacman.x, Pacman.y = 20, 20
        deathTotal = deathTotal + 1
        print(deathTotal)


    next_pos_PAC_x = Pacman.move(px, 0)
    next_pos_PAC_y = Pacman.move(0, py)
    next_pos_RG_x = RGhost.move(grx, 0)
    next_pos_RG_y = RGhost.move(0, gry)
    next_pos_BG_x = BGhost.move(gbx, 0)
    next_pos_BG_y = BGhost.move(0, gby)
    next_pos_PG_x = PGhost.move(gpx, 0)
    next_pos_PG_y = PGhost.move(0, gpy)
    next_pos_OG_x = OGhost.move(gox, 0)
    next_pos_OG_y = OGhost.move(0, goy)


    for wall in walls:
        if next_pos_PAC_x.colliderect(wall):
            px = 0
            break

    for wall in walls:
        if next_pos_PAC_y.colliderect(wall):
            py = 0
            break

    for wall in walls:
        if next_pos_RG_x.colliderect(wall):
            grx = 0
            break
        if next_pos_BG_x.colliderect(wall):
            gbx = 0
            break
        if next_pos_PG_x.colliderect(wall):
            gpx = 0
            break
        if next_pos_OG_x.colliderect(wall):
            gox = 0
            break

    for wall in walls:
        if next_pos_RG_y.colliderect(wall):
            gry = 0
            break
        if next_pos_BG_y.colliderect(wall):
            gby = 0
            break
        if next_pos_PG_y.colliderect(wall):
            gpy = 0
            break
        if next_pos_OG_y.colliderect(wall):
            goy = 0
            break

    for point in points:
        if next_pos_PAC_x.colliderect(point):
            points.remove(point)
            pointTotal = pointTotal + 20
            print (pointTotal)



    Pacman.move_ip(px, py)
    screen.blit(PacmanImg, Pacman)
    RGhost.move_ip(grx, gry)
    screen.blit(RGhostImg, RGhost)
    BGhost.move_ip(gbx, gby)
    screen.blit(BGhostImg, BGhost)
    PGhost.move_ip(gpx, gpy)
    screen.blit(PGhostImg, PGhost)
    OGhost.move_ip(gox, goy)
    screen.blit(OGhostImg, OGhost)

    if maxPoints == pointTotal:
        exitProg = True
        print("You Win!!!")

    if maxDeaths == deathTotal:
        exitProg = True
        print("You lost:(")

    display.flip()

quit()