import pygame

class Espaco:
	def __init__(self, x, y, largura, altura):
		self.x = x
		self.y = y
		self.largura = largura
		self.altura = altura

		self.abs_x = x * largura
		self.abs_y = y * largura
		self.abs_pos = (self.abs_x, self.abs_y)
		self.pos = (x, y)
		self.cor = 'light' if (x + y) % 2 == 0 else 'dark'
		self.draw_cor = (241, 211, 170) if self.cor == 'light' else (180, 126, 82)
		self.highlight_cor = (150, 255, 100) if self.cor == 'light' else (50, 220, 0)
		self.occupying_piece = None
		self.coord = self.get_coord()
		self.highlight = False

		self.rect = pygame.Rect(
			self.abs_x,
			self.abs_y,
			self.largura,
			self.altura
		)


	def get_coord(self):
		columns = 'abcdefgh'
		return columns[self.x] + str(self.y + 1)


	def draw(self, display):
		if self.highlight:
			pygame.draw.rect(display, self.highlight_cor, self.rect)
		else:
			pygame.draw.rect(display, self.draw_cor, self.rect)

		if self.occupying_piece != None:
			centering_rect = self.occupying_piece.img.get_rect()
			centering_rect.center = self.rect.center
			display.blit(self.occupying_piece.img, centering_rect.topleft)