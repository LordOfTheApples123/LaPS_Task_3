from Point import Point
from itertools import combinations
from Triangle import Triangle


def get_axis_points(p1, p2):
    a = p1.y - p2.y
    b = p2.x - p1.x
    c = p1.x * p2.y - p2.x * p1.y
    # уравнение прямой Ax + By + C = 0
    if b == 0:
        with_oy = max(p1.y, p2.y) + 1
    else:
        with_oy = -c / b
    if a == 0:
        with_ox = max(p1.x, p2.x) + 1
    else:
        with_ox = -c / a
    return Point(with_ox, with_oy)


def solution(triangle):
    ox_pos = False
    ox_neg = False
    oy_pos = False
    oy_neg = False

    points = [triangle.a, triangle.b, triangle.c]
    comb = list(combinations(points, 2))

    for couple in comb:
        a = couple[0]
        b = couple[1]
        ab = get_axis_points(a, b)
        if min(a.x, b.x) <= ab.x <= max(a.x, b.x):
            if ab.x > 0:
                ox_pos = True
            else:
                ox_neg = True
        if min(a.y, b.y) <= ab.y <= max(a.y, b.y):
            if ab.y > 0:
                oy_pos = True
            else:
                oy_neg = True
    return ox_neg & ox_pos & oy_pos & oy_neg
