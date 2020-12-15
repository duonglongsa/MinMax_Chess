import pygame as p 

piece = 'wp'
image =  p.image.load("images/" + piece  + ".png")


p.init()
running = True
while running:
    for e in p.event.get():
            if e.type == p.QUIT:
                running = False
    screen = p.display.set_mode((512, 512))
    screen.blit(image, p.Rect(64, 64, 0, 0))
    p.display.flip()