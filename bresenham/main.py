import arcade
from bresenham import get_line

# Definición de constantes
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Líneas con Bresenham"

class BresenhamWindow(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.BLACK)
        self.pixel_size = 20  
    def on_draw(self):
        arcade.start_render()
        self.draw_grid()
        center_x = 10
        center_y = 10

        octants = [
            (center_x, center_y, 15, 15),   # Octante 1
            (center_x, center_y, 10, 15),   # Octante 2
            (center_x, center_y, 5, 15),    # Octante 3
            (center_x, center_y, 5, 10),    # Octante 4
            (center_x, center_y, 5, 5),     # Octante 5
            (center_x, center_y, 10, 5),    # Octante 6
            (center_x, center_y, 15, 5),    # Octante 7
            (center_x, center_y, 15, 10)    # Octante 8
        ]

        colors = [
            arcade.color.RED,
            arcade.color.ORANGE,
            arcade.color.YELLOW,
            arcade.color.GREEN,
            arcade.color.BLUE,
            arcade.color.INDIGO,
            arcade.color.VIOLET,
            arcade.color.WHITE
        ]

        for i, (x0, y0, x1, y1) in enumerate(octants):
            points = get_line(x0, y0, x1, y1)
            self.draw_scaled_line(x0, y0, x1, y1, colors[i])

    def draw_grid(self):
        # Líneas verticales
        for v_l in range(0, SCREEN_WIDTH, self.pixel_size):
            arcade.draw_line(
                v_l, 
                0, 
                v_l, 
                SCREEN_HEIGHT, 
                arcade.color.DARK_GRAY
            )

        for h_l in range(0, SCREEN_HEIGHT, self.pixel_size):
            arcade.draw_line(
                0, 
                h_l, 
                SCREEN_WIDTH, 
                h_l, 
                arcade.color.LIGHT_GRAY
            )

    def draw_scaled_line(self, x0, y0, x1, y1, color):
        arcade.draw_line(
            x0 * self.pixel_size, 
            y0 * self.pixel_size, 
            x1 * self.pixel_size, 
            y1 * self.pixel_size,
            color,
            5  
        )


if __name__ == "__main__":
    app = BresenhamWindow()
    arcade.run()
