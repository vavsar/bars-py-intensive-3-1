from day_12.actions import MasterPack
from day_12.controller import main_controller


def register_actions():
    """
    Регистрация паков
    """
    main_controller.packs.extend([
        MasterPack(),
    ])
