import os
from looplive.model.model import Model
from looplive.controller.config_controller import ConfigController
from looplive.controller.bili_controller import BiliController

if __name__ == '__main__':
    path = os.path.join(os.path.dirname(__file__), 'model/config.json')
    cc = ConfigController(path=path)
    if cc.check_config():
        BiliController(cc).stream()
    else:
        print("Please complete the configuration first!")