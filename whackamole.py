import pygame
import random

def mole_touched(event_loc,mole_loc):
    mol_loc = list(mole_loc)
    event_loc = list(event_loc)
    event_loc[0] = event_loc[0]//32
    event_loc[1] = event_loc[1]//32
    mol_loc[0] = mol_loc[0]//32
    mol_loc[1] = mol_loc[1]//32
    #if int(mol_loc[0]) == int(event_loc[0]) and int(mole_loc[1]) == int(event_loc[1]):
    if int(mol_loc[0]) == int(event_loc[0]) and int(mol_loc[1]) == int(event_loc[1]):
        return True
    else:
        print(f"mol: {mol_loc} != {event_loc}")
        print(mol_loc[0] == event_loc[0])
        print(mol_loc[1] == event_loc[1])
        print(mol_loc[1], " ", event_loc[1])

        return False

def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        screen.fill("light green")
        mol_pos = (0, 0)



        while running:
            screen.fill("light green")
            for y in range(0, 16):
                pygame.draw.line(screen, "blue", (0, y * 32), (640, y*32))
            for x in range(0,20):
                pygame.draw.line(screen, "blue", (32*x,0), (x*32,512))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    print (mole_touched(event.pos,mol_pos))
                    print(mol_pos)
                    print(mol_pos[0]//32,mol_pos[1]//32)
                    print(event.pos)
                    print(f"square{event.pos[0]//32},{event.pos[1]//32}")
                    if event.pos[0]//32 == mol_pos[0]//32 and event.pos[1]//32 == mol_pos[1]//32:
                        print("Hey")
                    if mole_touched(event.pos,mol_pos):
                        #mol_pos = (random.randrange(0, 512)//32, random.randrange(0, 640)//32)
                        mol_pos = (random.randrange(0, 20) * 32, random.randrange(0, 16) * 32)
                        #pass

            screen.blit(mole_image, mole_image.get_rect(topleft=(mol_pos)))
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
