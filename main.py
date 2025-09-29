# main.py
from utils import get_float, get_int

if __name__ == '__main__':
    x = get_float("x: ")
    y = get_int("y: ")
    z = x**y
    print(z)
