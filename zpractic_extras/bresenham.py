def get_circle(x_center, y_center, radius):
    points = []
    x = 0
    y = radius
    d = 3 - 2 * radius

    def plot_circle_points(x_center, y_center, x, y):
        points.append((x_center + x, y_center + y))
        points.append((x_center - x, y_center + y))
        points.append((x_center + x, y_center - y))
        points.append((x_center - x, y_center - y))
        points.append((x_center + y, y_center + x))
        points.append((x_center - y, y_center + x))
        points.append((x_center + y, y_center - x))
        points.append((x_center - y, y_center - x))

    while y >= x:
        plot_circle_points(x_center, y_center, x, y)
        x += 1
        if d > 0:
            y -= 1
            d = d + 4 * (x - y) + 10
        else:
            d = d + 4 * x + 6

    return points
