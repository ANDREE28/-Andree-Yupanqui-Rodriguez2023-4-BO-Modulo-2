import random
from game.components.enemies.enemy import Enemy


class EnemyManager:
    def __init__(self):
        self.enemies = []
        self.slow_duration = 5  # Duración de la ralentización en segundos

    def update(self, game):
        self.add_enemy()

        for enemy in self.enemies:
            enemy.update(self.enemies, game)

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)

    def add_enemy(self):
        enemy_type = random.randint(1, 2)
        if enemy_type == 5:
            enemy = Enemy()
        else:
            x_speed = 5
            y_speed = 2
            move_x_for = [50, 120]
            enemy = Enemy(enemy_type, x_speed, y_speed, move_x_for)
        if len(self.enemies) < 3:
            self.enemies.append(enemy)

    def slow_enemies(self, duration):
        for enemy in self.enemies:
            enemy.slow_down(duration)

    def reset(self):
        self.enemies = []
