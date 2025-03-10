from pygame import *

init()

width = 1200
height = 700
window = display.set_mode((width, height))
display.set_caption("Pac-Man")
screen = display.get_surface()

walls = [Rect(0,0,1200,6), Rect(0,694,1200,6),#horizontal
         Rect(0,0,6,300), Rect(1194,0,6,300),#vertical top
         Rect(0,400,6,300), Rect(1194,400,6,300),#vertical bottom

        Rect(80,70,220,2), Rect(80,70,2,195),#top corner(1.1)
        Rect(95,85,205,2), Rect(95,85,2,180),#top corner(1.2)
        Rect(300,70,2,17), Rect(80,265,17,2),#top corner(1.2)
         # Rect(0,340,6,260), Rect(794,340,6,260),#top corner(2)
         # Rect(0,340,6,260), Rect(794,340,6,260),#top corner(3)
         # Rect(0,340,6,260), Rect(794,340,6,260),
         # Rect(0,340,6,260), Rect(794,340,6,260)

         #Rect(0,250,0,4), Rect(0,0,800,4),#box(top)
         #Rect(0,340,4,260), Rect(794,340,4,260),#box(sides)
         #Rect(0,340,6,4),#box(bottom)
         #Rect(0,340,6,260), Rect(0,0,6,300),#box(bottom)


        ]

#Characters
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
#Pacman, RGhost, BGhost, PGhost, OGhost
PacmanImg = image.load("pacman.png")
PacmanImg = transform.scale(PacmanImg, (60, 60))
dx = 2
RGhostImg = image.load("redGhost.png")
RGhostImg = transform.scale(RGhostImg, (50, 60))
BGhostImg = image.load("blueGhost.png")
BGhostImg = transform.scale(BGhostImg, (50, 60))
PGhostImg = image.load("pinkGhost.png")
PGhostImg = transform.scale(PGhostImg, (50, 60))
OGhostImg = image.load("orangeGhost.png")
OGhostImg = transform.scale(OGhostImg, (50, 60))
Pacman = Rect(450, 350, 40, 50)
RGhost = Rect(300, 450, 40, 50)
BGhost = Rect(400, 450, 40, 50)
PGhost = Rect(500, 450, 40, 50)
OGhost = Rect(200, 450, 40, 40)

exitProg = False

# Game loop
dx=2
px=0
py=0
while exitProg == False:
    time.delay(5)
    screen.fill((0, 0, 0))
    screen.blit(RGhostImg, RGhost)
    screen.blit(BGhostImg, BGhost)
    screen.blit(PGhostImg, PGhost)
    screen.blit(OGhostImg, OGhost)
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
            if e.key == K_LEFT or e.key == K_RIGHT or e.key == K_UP or e.key == K_DOWN:
                py = 0
                px = 0
    if Pacman.x + px <= 0:
        px = 0
    if Pacman.x + px >= width:
        px = 0
    if Pacman.y + py <= 0:
        py = 0
    if Pacman.y + py >= height:
        py = 0

    Pacman.move_ip(px, py)
    screen.blit(PacmanImg, Pacman)

    display.flip()

quit()
