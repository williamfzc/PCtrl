import pyautogui
from collections import namedtuple

from PCtrl import config

Point = namedtuple('Point', ('x', 'y'))


def fix_point(old_point: Point) -> Point:
    offset_x, offset_y = config.OFFSET
    return Point(old_point.x + offset_x, old_point.y + offset_y)


def left_click(target_point: Point):
    target_point = fix_point(target_point)
    pyautogui.moveTo(*target_point)
    pyautogui.click()


def right_click(target_point: Point):
    target_point = fix_point(target_point)
    pyautogui.moveTo(*target_point)
    pyautogui.click()


def current_point() -> Point:
    return Point(*pyautogui.position())
