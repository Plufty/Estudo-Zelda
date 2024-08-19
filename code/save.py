import json
from settings import *


class SaveManager:
    def __init__(self, player, level):
        self.player = player
        self.level = level

    def save_game(self, file_name="savefile.json"):
        game_state = {
            "player": {
                "position": (self.player.rect.x, self.player.rect.y),
                "health": self.player.health,
                "energy": self.player.energy,
                "exp": self.player.exp,
                "stats": self.player.stats,
                "max_stats": self.player.max_stats,
                "speed": self.player.speed,
                "upgrade_cost": self.player.upgrade_cost,
                "weapon_index": self.player.weapon_index,
                "magic_index": self.player.magic_index,
            },
            "level": {
                "dead_enemies": [enemy.id for enemy in self.level.enemies if enemy.health <= 0],
                "cut_grass": self.level.cut_grass
                # Outros detalhes do nível
            }

        }

        with open(file_name, 'w') as save_file:
            json.dump(game_state, save_file)

    def load_game(self, file_name="savefile.json"):
        try:
            with open(file_name, 'r') as save_file:
                game_state = json.load(save_file)

            # Player
            player_state = game_state["player"]
            self.player.rect.x, self.player.rect.y = player_state["position"]
            self.player.hitbox.center = self.player.rect.center
            self.player.health = player_state["health"]
            self.player.energy = player_state["energy"]
            self.player.exp = player_state["exp"]
            self.player.stats = player_state["stats"]            
            self.player.max_stats = player_state["max_stats"]
            self.player.speed = player_state["speed"]
            self.player.upgrade_cost = player_state["upgrade_cost"]
            self.player.weapon_index = player_state["weapon_index"]
            self.player.magic_index = player_state["magic_index"]
            self.player.weapon = list(weapon_data.keys())[self.player.weapon_index]
            self.player.magic = list(magic_data.keys())[self.player.magic_index]
            # Level
            cut_grass = game_state["level"].get("cut_grass", [])
            for grass in self.level.grass:
                if grass.id in cut_grass:
                    grass.kill()  # Remove grass


            dead_enemy_ids = game_state["level"].get("dead_enemies", [])
            for enemy in self.level.enemies:
                if enemy.id in dead_enemy_ids:
                    enemy.kill()  # Remove Dead Enemies

        except FileNotFoundError:
            print("Nenhum jogo salvo encontrado.")
