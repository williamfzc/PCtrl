from pynput.mouse import Button, Controller
from collections import namedtuple

from PCtrl import config

_mouse = Controller()
Point = namedtuple('Point', ('x', 'y'))


def fix_point(old_point: Point) -> Point:
    offset_x, offset_y = config.OFFSET
    return Point(old_point.x + offset_x, old_point.y + offset_y)


def left_click(target_point: Point, count: int = None):
    target_point = fix_point(target_point)
    _mouse.move(*target_point)
    if not count:
        count = 1
    _mouse.click(Button.left, count)


def right_click(target_point: Point, count: int = None):
    target_point = fix_point(target_point)
    _mouse.move(*target_point)
    _mouse.click(Button.right, count)


def current_point() -> Point:
    return _mouse.position
