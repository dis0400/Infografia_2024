def get_line(x0, y0, x1, y1):
    points = []
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    err = dx - dy

    while True:
        points.append((x0, y0))
        if x0 == x1 and y0 == y1:
            break
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x0 += sx
        if e2 < dx:
            err += dx
            y0 += sy

    return points


if __name__ == "__main__":
    # OCTANTE 1
    print("Octante 1:")
    points = get_line(3, 2, 15, 10)
    print(points)

    # OCTANTE 2
    print("Octante 2:")
    points = get_line(3, 2, 10, 15)
    print(points)

    # OCTANTE 3
    print("Octante 3:")
    points = get_line(10, 15, 3, 2)
    print(points)

    # OCTANTE 4
    print("Octante 4:")
    points = get_line(15, 10, 3, 2)
    print(points)

    # OCTANTE 5
    print("Octante 5:")
    points = get_line(15, 2, 3, 10)
    print(points)

    # OCTANTE 6
    print("Octante 6:")
    points = get_line(10, 3, 3, 15)
    print(points)

    # OCTANTE 7
    print("Octante 7:")
    points = get_line(3, 15, 10, 3)
    print(points)

    # OCTANTE 8
    print("Octante 8:")
    points = get_line(2, 10, 15, 3)
    print(points)


