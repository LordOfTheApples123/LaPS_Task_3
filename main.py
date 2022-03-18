from Triangle import Triangle
from Logic import solution
from Point import Point
if __name__ == '__main__':
    a = Point(int(input("Enter point x: ")), int(input("Enter point y: ")))
    b = Point(int(input("Enter point x: ")), int(input("Enter point y: ")))
    c = Point(int(input("Enter point x: ")), int(input("Enter point y: ")))
    triangle = Triangle(a, b, c)
    print(str(solution(triangle)))
