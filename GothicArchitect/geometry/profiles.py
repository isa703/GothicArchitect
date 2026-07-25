import math


def circle_points(radius, count):

    pts = []

    for i in range(count):

        a = math.radians(i * 360 / count)

        pts.append((
            math.cos(a) * radius,
            math.sin(a) * radius,
        ))

    return pts