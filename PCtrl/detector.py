from findit_client import FindItStandardClient
from PIL import ImageGrab
import tempfile
import os
import typing

from PCtrl import config
from PCtrl import controller

fi_client = FindItStandardClient(
    config.HOST,
    config.PORT,
)

# no log by default
fi_client.switch_log(False)


def get_screen_png() -> str:
    """ screen shot, save it, and return its path """
    img = ImageGrab.grab()
    png_object = tempfile.NamedTemporaryFile('w+', suffix='.png', delete=False)
    png_path = png_object.name
    img.save(png_path)
    png_object.close()
    return png_path


def find_target(target_name: str) -> typing.Tuple[controller.Point, bool]:
    screen = get_screen_png()
    result = fi_client.analyse_with_path(screen, target_name, pro_mode=True)
    response = result['response']
    point = controller.Point(*fi_client.get_target_point_with_resp(response))
    existed: bool = fi_client.check_exist_with_resp(response, 0.95)
    os.remove(screen)
    return point, existed


def click_target(target_name: str):
    point, existed = find_target(target_name)
    assert existed, 'target {} not existed'.format(target_name)
    controller.left_click(point)
