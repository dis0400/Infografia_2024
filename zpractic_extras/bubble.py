import arcade
from bresenham import get_circle
import math

class Bubble:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.change_x = 1
        self.change_y = 1

    def draw(self):
        
        for point in get_circle(self.x, self.y, self.radius):
            arcade.draw_point(point[0], point[1], self.color, 2)

        self.draw_parabolas()

    def draw_parabolas(self):
        num_parabolas = 5
        for i in range(num_parabolas):
            # parábola dentro 
            a = 0.01 * (i - 1)
            parabola_points = self.generate_parabola(a, -self.radius, self.radius)
            self.draw_parabola_line(parabola_points, i)

    def generate_parabola(self, a, x_min, x_max):
        """Genera puntos para una parábola de la forma y = a * (x^2)"""
        points = []
        for x in range(x_min, x_max + 1):
            y = a * (x ** 2)
            points.append((self.x + x, self.y + y))
        return points

    def draw_parabola_line(self, points, index):
        """Dibuja una línea usando los puntos generados por la parábola"""
        color = arcade.color.BLUE if index % 2 == 0 else arcade.color.PINK
        arcade.draw_line_strip(points, color, 2)

    def update(self):
        # Mueve 
        self.x += self.change_x
        self.y += self.change_y

        # Rebota
        if self.x - self.radius < 0 or self.x + self.radius > 800:
            self.change_x *= -1
        if self.y - self.radius < 0 or self.y + self.radius > 600:
            self.change_y *= -1


class MyWindow(arcade.Window):
    def __init__(self):
        super().__init__(800, 600, "Burbuja con Parábolas")
        arcade.set_background_color(arcade.color.BLACK)
        self.bubble = Bubble(400, 300, 100, arcade.color.WHITE)

    def on_draw(self):
        arcade.start_render()
        self.bubble.draw()

    def on_update(self, delta_time):
        self.bubble.update()

if __name__ == "__main__":
    window = MyWindow()
    arcade.run()
