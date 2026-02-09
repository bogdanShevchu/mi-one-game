import pygame

clock = pygame.time.Clock()

pygame.init()
skreen = pygame.display.set_mode((736,414))
icon = pygame.image.load("png/puzzle_1006518.png")
pygame.display.set_icon(icon)
skreen.fill("blue")
graund = pygame.image.load("png/33f54d6856c9a5336a8f86df8743e240.jpg")

player = [
	pygame.image.load("png/Untitled 3.png"),
	pygame.image.load("png/Untitled 4.png")
]
player = [
	pygame.image.load("png/Untitled 3 l.png"),
	pygame.image.load("png/Untitled 4 l.png")
]

kadr = 0

player_x = 207
player_y = 368

bgx = 0

while True:
	pygame.display.update()

	skreen.blit(graund, (bgx, 0))
	skreen.blit(graund, (bgx + 736, 0))

	skreen.blit(player[kadr], (player_y, player_x,))

	if kadr == 1:#animation player
		kadr = 0
	else:
		kadr += 1

	if bgx == -736:#animation begraund
		bgx = 0
	bgx -= 2

	for q in pygame.event.get():#exit
		if q.type == pygame.QUIT:
			pygame.quit()
			break

	clock.tick(5)
