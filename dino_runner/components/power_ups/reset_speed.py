from dino_runner.utils.constants import RESET_SPEED, RESET_SPEED_TYPE
from dino_runner.components.power_ups.power_up import PowerUp


class ResetSpeed(PowerUp):
    def __init__(self):
        self.image = RESET_SPEED
        self.type = RESET_SPEED_TYPE
        super().__init__(self.image, self.type)