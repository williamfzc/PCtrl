from pynput.mouse import Button, Controller
from collections import namedtuple

_mouse = Controller()
Point = namedtuple('Point', ('x', 'y'))


def left_click(target_point: Point, count: int = None):
    _mouse.move(*target_point)
    if not count:
        count = 1
    _mouse.click(Button.left, count)


def right_click(target_point: Point, count: int = None):
    _mouse.move(*target_point)
    _mouse.click(Button.right, count)


def current_point() -> Point:
    return _mouse.position
