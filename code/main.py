import pygame, sys
from settings import *
from level import Level
from menu import Menu
from debug import * 
from enemy import Enemy
from tile import Tile

class Game:
	def __init__(self):
		self.reset_game()		
		self.running = True

	def reset_game(self):
		# general 
		Enemy.next_id = 1
		Tile.next_id = 1
		pygame.init()
		self.screen = pygame.display.set_mode((WIDTH, HEIGTH))
		pygame.display.set_caption('Zelda')
		self.clock = pygame.time.Clock()

		self.level = Level(self.game_over)

		# sound 
		self.main_sound = pygame.mixer.Sound('../audio/main.ogg')
		self.main_sound.set_volume(0.5)
		self.main_sound.play(loops = -1)

		# Menus    
		self.paused = False
		self.running = True

	def game_over(self):
		menu = Menu(self.screen, "Game Over", ["Restart", "Exit"])
		action = menu.run()  # Exibe o menu de Game Over e espera uma ação

		if action == 'restart':
			self.main_sound.stop()
			self.reset_game()
		elif action == 'exit':
			self.running = False
			self.main_sound.stop()


	def run(self):
		action = ''
		while self.running:
			if not self.paused:
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						pygame.quit()
						sys.exit()
					if event.type == pygame.KEYDOWN:
						if event.key == pygame.K_k:
							self.level.toggle_menu()
						if event.key == pygame.K_ESCAPE:
							self.paused = True

			else:
				menu = Menu(self.screen, "Paused", ["Resume", "Save", "Exit"])
				action = menu.run()  # Exibe o menu de pausa e espera uma ação
				# if action == 'back':
				# 	continue
				if action == 'resume':
					self.paused = False  # Retoma o jogo
				if action == 'save':
					self.level.save_game()
					self.paused = False  # Retoma o jogo
				elif action == 'exit':
					self.main_sound.stop()
					self.running = False

			self.screen.fill(WATER_COLOR)
			self.level.run()
			pygame.display.update()
			self.clock.tick(FPS)

		if not self.running:
			action = 'exit_to_menu'

		return action

if __name__ == '__main__':
	running = True
	while running:
		game = Game()
		main_menu = Menu(game.screen, "Main Menu", ["New Game", "Load Game", "Exit"])
		action = main_menu.run()
		if action == 'new_game':
			game_result = game.run()
			if game_result == 'exit_to_menu':
				continue  # Volta para o menu principal		
		elif action == 'load_game':
			game.level.load_game()
			game_result = game.run()
			if game_result == 'exit_to_menu':
				continue  # Volta para o menu principal		
		elif action == 'exit':				
			pygame.quit()
			sys.exit()
