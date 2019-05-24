# PCtrl

pc controller, based on findit.

## 目的

基于图像识别技术的 pc自动化工具！

## 依赖

- [pyautogui](https://github.com/asweigart/pyautogui)
- [findit](https://github.com/williamfzc/findit)

## 使用

图片识别服务依赖于[findit](https://github.com/williamfzc/findit)，所以你需要先启动它：

- 用[docker](https://williamfzc.github.io/findit/#/usage/client+server)启动
- 或者，直接用命令行 `python -m findit.server --dir YOUR_PICTURE_DIR --port YOUR_PORT` 
    - `YOUR_PICTURE_DIR` 换成你的图片根目录
    - `YOUR_PORT` 服务端口，默认9410

如果你需要在屏幕上 寻找并点击 目标图片 `aaa.png`，你需要：

- 将图片放在 `YOUR_PICTURE_DIR` 下，即你的图片根目录下；
- 然后运行三行脚本

    ```python
    from PCtrl.api import click_target
    target_name = 'aaa.png'
    click_target(target_name)
    ```

- 完成！

更复杂的例子可参考 [这里](sample/click_icon.py)

## LICENCE

[MIT](LICENSE)
