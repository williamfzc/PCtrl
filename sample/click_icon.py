from PCtrl.api import click_target, find_target
from PCtrl import config

# 可以根据部署方式，修改配置。默认则不需要改
config.HOST = '127.0.0.1'
config.PORT = 9410

# 你的目标图片，需要存在于你的图片库
target_name = 'ij.png'

# 寻找目标，及是否存在
point, existed = find_target(target_name)
assert existed, 'target {} not existed'.format(target_name)

# 操作目标
print('point found: {}'.format(point))
click_target(target_name)
