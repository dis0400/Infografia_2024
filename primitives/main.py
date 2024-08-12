import arcade
from bresenham import get_line, get_circle

# Definición de constantes
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Figuras con Bresenham"

class BresenhamShapesWindow(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.BLACK)
        self.pixel_size = 3
        self.xc = 30
        self.yc = 40
        self.r = 15

    def on_update(self, delta_time: float):
        pass

    def on_draw(self):
        arcade.start_render()
        self.draw_grid()

        circle_points = get_circle(self.xc, self.yc, self.r)
        self.draw_circle_points(circle_points, arcade.color.DARK_YELLOW)
        self.draw_scaled_circle(self.xc, self.yc, self.r)

        self.draw_rectangle(70, 40, 20, 15, arcade.color.GREEN)

        self.draw_triangle_isosceles(100, 40, 30, 20, arcade.color.BLUE)

        self.draw_pentagon(150, 50, 20, arcade.color.PURPLE)

        self.draw_triangle(200, 50, 220, 80, 180, 100, arcade.color.RED)

    def draw_grid(self):
        for v_l in range(0, SCREEN_WIDTH, self.pixel_size):
            arcade.draw_line(
                v_l + self.pixel_size / 2, 
                0, 
                v_l + self.pixel_size / 2, 
                SCREEN_HEIGHT, 
                [50, 50, 50]
            )
        for h_l in range(0, SCREEN_HEIGHT, self.pixel_size):
            arcade.draw_line(
                0, 
                h_l + self.pixel_size / 2, 
                SCREEN_WIDTH, 
                h_l + self.pixel_size / 2, 
                [50, 50, 50]
            )

    def draw_circle_points(self, points, color):
        for p in points:
            arcade.draw_point(p[0] * self.pixel_size, p[1] * self.pixel_size, color, self.pixel_size)

    def draw_scaled_circle(self, xc, yc, r):
        arcade.draw_circle_outline(
            xc * self.pixel_size, 
            yc * self.pixel_size, 
            r * self.pixel_size, 
            [100, 255, 40, 150], 
            5
        )

    def draw_line_points(self, points, color):
        for p in points:
            arcade.draw_point(p[0] * self.pixel_size, p[1] * self.pixel_size, color, self.pixel_size)

    def draw_rectangle(self, x, y, width, height, color):
        points = []
        points.extend(get_line(x, y, x + width, y))  
        points.extend(get_line(x + width, y, x + width, y + height))  
        points.extend(get_line(x + width, y + height, x, y + height)) 
        points.extend(get_line(x, y + height, x, y))  
        self.draw_line_points(points, color)

    def draw_triangle_isosceles(self, x, y, width, height, color):
        points = []
        points.extend(get_line(x, y, x + width, y)) 
        points.extend(get_line(x, y, x + width // 2, y + height))  
        points.extend(get_line(x + width, y, x + width // 2, y + height)) 
        self.draw_line_points(points, color)

    def draw_pentagon(self, xc, yc, radius, color):
        import math
        points = []
        num_sides = 5
        for i in range(num_sides):
            angle1 = 2 * math.pi * i / num_sides
            angle2 = 2 * math.pi * (i + 1) / num_sides
            x1 = int(xc + radius * math.cos(angle1))
            y1 = int(yc + radius * math.sin(angle1))
            x2 = int(xc + radius * math.cos(angle2))
            y2 = int(yc + radius * math.sin(angle2))
            points.extend(get_line(x1, y1, x2, y2))
        self.draw_line_points(points, color)

    def draw_triangle(self, x1, y1, x2, y2, x3, y3, color):
        points = []
        points.extend(get_line(x1, y1, x2, y2))  
        points.extend(get_line(x2, y2, x3, y3))  
        points.extend(get_line(x3, y3, x1, y1))  
        self.draw_line_points(points, color)

if __name__ == "__main__":
    app = BresenhamShapesWindow()
    arcade.run()
