import os
import threading
from looplive.model.model import Model
from looplive.controller.config_controller import ConfigController
from looplive.controller.bili_controller import BiliController
from looplive.controller.ytb_controller import YtbController
if __name__ == '__main__':
    path = os.path.join(os.path.dirname(__file__), 'model/config.json')
    cc = ConfigController(path=path)
    if cc.check_bili_config() and cc.check_ytb_config():
        bili_thread = threading.Thread(target=lambda: BiliController(cc).stream())
        ytb_thread = threading.Thread(target=lambda: YtbController(cc).stream())

        bili_thread.start()
        ytb_thread.start()

        bili_thread.join()
        ytb_thread.join()
    elif cc.check_bili_config():
        BiliController(cc).stream()
    elif cc.check_ytb_config():
        YtbController(cc).stream()
    else:
        print("Please complete the configuration first!")