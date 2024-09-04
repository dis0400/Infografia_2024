import arcade
from bubble import Bubble

# Definición de constantes
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Burbuja en Movimiento"

class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.BLACK)

        # Crear la burbuja
        self.bubble = Bubble(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, 50, arcade.color.WHITE)

    def on_draw(self):
        arcade.start_render()
        self.bubble.draw()

    def on_update(self, delta_time):
        self.bubble.update()

if __name__ == "__main__":
    game = MyGame()
    arcade.run()
