from pygame import *
from random import randint

init()

width = 1000
height = 700
window = display.set_mode((width, height))
display.set_caption("Pac-Man")
screen = display.get_surface()

walls = [Rect(0,0,1000,6), Rect(0,694,1000,6),  #horizontal
         Rect(0,0,6,300), Rect(994,0,6,300),  #vertical top
         Rect(0,400,6,300), Rect(994,400,6,300),  #vertical bottom

         Rect(80,70,220,2), Rect(80,70,2,195),  #top left corner(1.1)
         Rect(95,85,205,2), Rect(95,85,2,180),  #top corner(1.2)
         Rect(300,70,2,17), Rect(80,265,17,2),  #top corner(1.2)

         Rect(150,140,80,2), Rect(150,220,80,2),  #top left corner(2.1.1)
         Rect(165,155,50,2), Rect(165,205,50,2),  #top left corner(2.1.1)
         Rect(150,140,2,80), Rect(230,140,2,82),  #top left corner(2.2.1)
         Rect(165,155,2,50), Rect(215,155,2,52),  #top left corner(2.2.1)

         Rect(700,70,220,2), Rect(920,70,2,196),  #top right corner(1.1)
         Rect(700,85,205,2), Rect(905,85,2,180),  #top right corner(1.2)
         Rect(700,70,2,17), Rect(905,265,17,2),  #top right corner(1.2)

         Rect(770, 140, 80, 2), Rect(770, 220, 80, 2),  # top right corner(2.1.1)
         Rect(785, 155, 50, 2), Rect(785, 205, 50, 2),  # top right corner(2.1.1)
         Rect(770, 140, 2, 80), Rect(850, 140, 2, 82),  # top right corner(2.2.1)
         Rect(785, 155, 2, 50), Rect(835, 155, 2, 52),  # top right corner(2.2.1)

         Rect(80, 630, 220, 2), Rect(80, 435, 2, 195),  # bottom left corner(1.1)
         Rect(95, 615, 205, 2), Rect(95, 435, 2, 180),  # bottom corner(1.2)
         Rect(300, 615, 2, 17), Rect(80, 435, 17, 2),  # bottom corner(1.2)

         Rect(150, 480, 80, 2), Rect(150, 560, 80, 2),  # bottom left corner(2.1.1)
         Rect(165, 495, 50, 2), Rect(165, 545, 50, 2),  # bottom left corner(2.1.1)
         Rect(150, 480, 2, 80), Rect(230, 480, 2, 82),  # bottom left corner(2.2.1)
         Rect(165, 495, 2, 50), Rect(215, 495, 2, 52),  # bottom left corner(2.2.1)

         Rect(700, 630, 220, 2), Rect(920, 435, 2, 196),  # bottom right corner(1.1)
         Rect(700, 615, 206, 2), Rect(905, 435, 2, 180),  # bottom right corner(1.2)
         Rect(700, 615, 2, 17), Rect(905, 435, 17, 2),  # bottom right corner(1.2)

         Rect(770, 480, 80, 2), Rect(770, 560, 80, 2),  # bottom right corner(2.1.1)
         Rect(785, 495, 50, 2), Rect(785, 545, 50, 2),  # bottom right corner(2.1.1)
         Rect(770, 480, 2, 80), Rect(850, 480, 2, 82),  # bottom right corner(2.2.1)
         Rect(785, 495, 2, 50), Rect(835, 495, 2, 52),  # bottom right corner(2.2.1)

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
Pacman = Rect(450, 350, 40, 40)
RGhost = Rect(300, 350, 30, 40)
BGhost = Rect(400, 350, 30, 40)
PGhost = Rect(500, 350, 30, 40)
OGhost = Rect(200, 350, 30, 40)
exitProg = False

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
        if py <= 300 or py >= 400:
            Pacman.x = 953
            px = 0
    if Pacman.x + px >= width - 45:
        px = 0
        if py <= 300 or py >= 400:
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

    #if Pacman.colliderect(RGhost):
    #    exitProg = True
    #if Pacman.colliderect(BGhost):
    #    exitProg = True
    #if Pacman.colliderect(PGhost):
    #    exitProg = True
    #if Pacman.colliderect(OGhost):
    #    exitProg = True

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

    display.flip()

quit()
