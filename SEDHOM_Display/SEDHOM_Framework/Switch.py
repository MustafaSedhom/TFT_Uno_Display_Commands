#######################################################################################
# SEDHOM GUI FRAMEWORK
# Switch Widget
#######################################################################################

import time
from ..Display import SEDHOM_Display

class Switch:

    ###################################################################################
    # Constructor
    ###################################################################################

    def __init__(
        self,
        Display:SEDHOM_Display,
        x: int = 100,
        y: int = 100,
        state: bool = False,
        width: int = 80,
        height: int = 40,
        radius: int = 15,
        padding: int = 5,
        animation_delay: float = 2.0,
        auto_draw: bool = False
    ):

        self.Display = Display

        ################################################################################
        # Position Settings
        ################################################################################

        self.x = x
        self.y = y

        ################################################################################
        # Size Settings
        ################################################################################

        self.width = width
        self.height = height
        self.radius = radius
        self.padding = padding

        ################################################################################
        # State Settings
        ################################################################################

        self.state = bool(state)

        ################################################################################
        # Animation Settings
        ################################################################################

        self.animation_delay = animation_delay

        ################################################################################
        # Color Settings
        ################################################################################

        self.Color_ON = Display.colors.Lime
        self.Color_OFF = Display.colors.Red
        self.Color_Knob = Display.colors.White

        ################################################################################
        # Appearance Settings
        ################################################################################

        self.Background_ON = self.Color_ON
        self.Background_OFF = self.Color_OFF

        self.Knob_Color = self.Color_Knob

        ################################################################################
        # Drawing Settings
        ################################################################################

        self.Filled = True
        self.Flush_After_Draw = True

        ################################################################################
        # Initialization
        ################################################################################

        if auto_draw:
            self.draw()

    ###################################################################################
    # Color Settings
    ###################################################################################

    def set_colors(
        self,
        on=None,
        off=None,
        knob=None
    ):

        if on is not None:
            self.Color_ON = on
            self.Background_ON = on

        if off is not None:
            self.Color_OFF = off
            self.Background_OFF = off

        if knob is not None:
            self.Color_Knob = knob
            self.Knob_Color = knob

        return self

    ###################################################################################
    # Position Settings
    ###################################################################################

    def set_position(self, x: int, y: int):

        self.x = x
        self.y = y

        return self

    ###################################################################################
    # Size Settings
    ###################################################################################

    def set_size(
        self,
        width: int,
        height: int
    ):

        self.width = width
        self.height = height

        return self

    ###################################################################################
    # Knob Settings
    ###################################################################################

    def set_knob(self, radius: int = None, padding: int = None):

        if radius is not None:
            self.radius = radius

        if padding is not None:
            self.padding = padding

        return self

    ###################################################################################
    # State Settings
    ###################################################################################

    def set_state(self, state: bool, draw: bool = True):

        self.state = bool(state)

        if draw:
            self.draw()

        return self

    def toggle(self, draw: bool = True):

        self.state = not self.state

        if draw:
            self.draw()

        return self

    def is_on(self) -> bool:

        return self.state

    def is_off(self) -> bool:

        return not self.state

    ###################################################################################
    # Animation Settings
    ###################################################################################

    def set_animation_delay(self, delay: float):

        self.animation_delay = max(0.0, delay)

        return self

    ###################################################################################
    # GUI Drawing Function
    ###################################################################################

    def draw(self):

        background_color = (
            self.Background_ON
            if self.state
            else self.Background_OFF
        )

        self.Display.shape.Rectangle(
            self.x,
            self.y,
            self.width,
            self.height,
            50,
            background_color
        )

        if self.animation_delay > 0:
            time.sleep(self.animation_delay)

        knob_x = (
            self.x + self.width - self.radius - self.padding
            if self.state
            else self.x + self.radius + self.padding
        )

        knob_y = self.y + self.height // 2

        self.Display.shape.Circle(
            knob_x,
            knob_y,
            self.radius,
            self.Knob_Color,
            self.Filled
        )

        if self.Flush_After_Draw:
            self.Display.flush()

        return True

    ###################################################################################
    # Update Settings
    ###################################################################################

    def update(self):

        return self.draw()

    ###################################################################################
    # End Of Class
    ###################################################################################
