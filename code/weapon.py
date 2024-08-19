import pygame 

class Weapon(pygame.sprite.Sprite):
	def __init__(self,player,groups):
		super().__init__(groups)
		self.sprite_type = 'weapon'
		direction = player.status.split('_')[0]

		# graphic
		full_path = f'../graphics/weapons/{player.weapon}/{direction}.png'
		self.image = pygame.image.load(full_path).convert_alpha()
		
		# placement
		if direction == 'right':
			self.rect = self.image.get_rect(midleft = player.rect.midright + pygame.math.Vector2(0,16))
		elif direction == 'left': 
			self.rect = self.image.get_rect(midright = player.rect.midleft + pygame.math.Vector2(0,16))
		elif direction == 'down':
			self.rect = self.image.get_rect(midtop = player.rect.midbottom + pygame.math.Vector2(-10,0))
		else:
			self.rect = self.image.get_rect(midbottom = player.rect.midtop + pygame.math.Vector2(-10,0))


# import pygame
# import math

# class Weapon(pygame.sprite.Sprite):
#     def __init__(self, player, groups):
#         super().__init__(groups)
#         self.sprite_type = 'weapon'
#         self.player = player
#         self.direction = player.status.split('_')[0]

#         # Graphic
#         full_path = f'../graphics/weapons/{player.weapon}/{self.direction}.png'
#         self.image = pygame.image.load(full_path).convert_alpha()

#         # Inicializa o swing
#         self.swing_offset = pygame.math.Vector2(0, 0)
#         self.swing_magnitude = 30  # Aumente para ver mais movimento
#         self.swing_duration = 300  # Duração do swing em milissegundos
#         self.swing_start_time = pygame.time.get_ticks()

#         # Placement
#         self.rect = self.image.get_rect()
#         self.update_position()

#     def update(self):
#         self.update_position()

#     def update_position(self):
#         # Verifica se a arma é sword ou axe para aplicar o swing
#         if self.player.weapon in ['sword', 'axe']:
#             elapsed_time = pygame.time.get_ticks() - self.swing_start_time
#             swing_progress = min(elapsed_time / self.swing_duration, 1)  # Progresso do swing (0 a 1)
            
#             # Calcula o arco do swing
#             swing_angle = swing_progress * 2 * math.pi
#             swing_arc = pygame.math.Vector2(self.swing_magnitude * math.sin(swing_angle), 0)
            
#             # Aplica o offset dependendo da direção
#             if self.direction == 'right':
#                 self.rect.midleft = self.player.rect.midright + pygame.math.Vector2(0, 16+self.swing_magnitude * math.sin(swing_angle))
#             elif self.direction == 'left':
#                 self.rect.midright = self.player.rect.midleft - pygame.math.Vector2(0, 16+self.swing_magnitude * math.sin(swing_angle))
#             elif self.direction == 'down':
#                 self.rect.midtop = self.player.rect.midbottom + pygame.math.Vector2(self.swing_magnitude * math.sin(swing_angle)-10, 0)
#             else:  # 'up'
#                 self.rect.midbottom = self.player.rect.midtop - pygame.math.Vector2(self.swing_magnitude * math.sin(swing_angle)-10, 0)
#         else:
#             # Para outras armas, mantém a posição fixa
#             if self.direction == 'right':
#                   self.rect = self.image.get_rect(midleft = self.player.rect.midright + pygame.math.Vector2(0,16))
#             elif self.direction == 'left':
#                   self.rect = self.image.get_rect(midright = self.player.rect.midleft + pygame.math.Vector2(0,16))
#             elif self.direction == 'down':
#                   self.rect = self.image.get_rect(midtop = self.player.rect.midbottom + pygame.math.Vector2(-10,0))
#             else:  # 'up'
#                    self.rect = self.image.get_rect(midbottom = self.player.rect.midtop + pygame.math.Vector2(-10,0))
                

# import pygame
# import math

# class Weapon(pygame.sprite.Sprite):
#     def __init__(self, player, groups):
#         super().__init__(groups)
#         self.sprite_type = 'weapon'
#         self.player = player
#         self.direction = player.status.split('_')[0]

#         # Graphic
#         full_path = f'../graphics/weapons/{player.weapon}/{self.direction}.png'
#         self.original_image = pygame.image.load(full_path).convert_alpha()
#         self.image = self.original_image.copy()

#         # Inicializa o swing
#         self.swing_magnitude = 90  # Aumente para ver mais movimento
#         self.swing_duration = 1000  # Duração do swing em milissegundos
#         self.swing_start_time = pygame.time.get_ticks()

#         # Placement
#         self.rect = self.image.get_rect()
#         self.update_position()

#     def update(self):
#         self.update_position()

#     def update_position(self):
#         # Verifica se a arma é sword ou axe para aplicar o swing
#         if self.player.weapon in ['sword', 'axe']:
#             elapsed_time = pygame.time.get_ticks() - self.swing_start_time
#             swing_progress = min(elapsed_time / self.swing_duration, 1)  # Progresso do swing (0 a 1)
            
#             # Calcula o arco do swing
#             swing_angle = swing_progress * 2 * math.pi
#             swing_arc = self.swing_magnitude * math.sin(swing_angle)
            
#             # Calcula a nova rotação
#             if self.direction in ['right', 'left']:
#                 angle = swing_arc / 2
#                 rotation_center = (self.rect.midleft[0], self.rect.midleft[1] + swing_arc)
#             else:
#                 angle = -swing_arc / 2
#                 rotation_center = (self.rect.midtop[0] + swing_arc, self.rect.midtop[1])
            
#             # Ajusta a posição da arma com base na rotação
#             self.image = pygame.transform.rotate(self.original_image, angle)
#             self.rect = self.image.get_rect(center=rotation_center)
            
#             if self.direction == 'right':
#                 self.rect.midleft = self.player.rect.midright
#             elif self.direction == 'left':
#                 self.rect.midright = self.player.rect.midleft
#             elif self.direction == 'down':
#                 self.rect.midtop = self.player.rect.midbottom
#             else:  # 'up'
#                 self.rect.midbottom = self.player.rect.midtop
#         else:
#             # Para outras armas, mantém a posição fixa
#             if self.direction == 'right':
#                 self.rect = self.image.get_rect(midleft=self.player.rect.midright)
#             elif self.direction == 'left':
#                 self.rect = self.image.get_rect(midright=self.player.rect.midleft)
#             elif self.direction == 'down':
#                 self.rect = self.image.get_rect(midtop=self.player.rect.midbottom)
#             else:  # 'up'
#                 self.rect = self.image.get_rect(midbottom=self.player.rect.midtop)


# import pygame
# import math

# class Weapon(pygame.sprite.Sprite):
#     def __init__(self, player, groups):
#         super().__init__(groups)
#         self.sprite_type = 'weapon'
#         self.player = player
#         self.direction = player.status.split('_')[0]

#         # Gráficos
#         full_path = f'../graphics/weapons/{player.weapon}/{self.direction}.png'
#         self.image = pygame.image.load(full_path).convert_alpha()
#         self.original_image = self.image.copy()  # Mantenha uma cópia da imagem original

#         # Inicializa o swing
#         self.swing_magnitude = 30  # Aumente para ver mais movimento
#         self.swing_duration = 300  # Duração do swing em milissegundos
#         self.swing_start_time = pygame.time.get_ticks()

#         # Configuração de posição
#         self.rect = self.image.get_rect()
#         self.update_position()

#     def update(self):
#         self.update_position()

#     def update_position(self):
#         if self.player.weapon in ['sword', 'axe']:
#             elapsed_time = pygame.time.get_ticks() - self.swing_start_time
#             swing_progress = min(elapsed_time / self.swing_duration, 1)  # Progresso do swing (0 a 1)

#             # Limitar o ângulo de swing
#             max_swing_angle = math.radians(90)  # Limite de 90 graus
#             swing_angle = swing_progress * 2 * max_swing_angle - max_swing_angle
#             swing_offset = pygame.math.Vector2(self.swing_magnitude * math.sin(swing_angle), 0)

#             # Atualiza a posição da arma
#             if self.direction == 'right':
#                 self.rect.midleft = self.player.rect.midright + pygame.math.Vector2(0, -16) + swing_offset
#             elif self.direction == 'left':
#                 self.rect.midright = self.player.rect.midleft - pygame.math.Vector2(0, 16) - swing_offset
#             elif self.direction == 'down':
#                 self.rect.midtop = self.player.rect.midbottom - pygame.math.Vector2(0, -10) + swing_offset
#             else:  # 'up'
#                 self.rect.midbottom = self.player.rect.midtop + pygame.math.Vector2(0, 10) - swing_offset

#             # Aplica a rotação para o efeito de swing
#             angle = math.degrees(swing_angle)
#             self.image = pygame.transform.rotate(self.original_image, angle)
#             self.rect = self.image.get_rect(center=self.rect.center)
#         else:
#             # Para outras armas, mantém a posição fixa
#             if self.direction == 'right':
#                 self.rect = self.image.get_rect(midleft=self.player.rect.midright + pygame.math.Vector2(0, 16))
#             elif self.direction == 'left':
#                 self.rect = self.image.get_rect(midright=self.player.rect.midleft + pygame.math.Vector2(0, 16))
#             elif self.direction == 'down':
#                 self.rect = self.image.get_rect(midtop=self.player.rect.midbottom + pygame.math.Vector2(-10, 0))
#             else:  # 'up'
#                 self.rect = self.image.get_rect(midbottom=self.player.rect.midtop + pygame.math.Vector2(-10, 0))