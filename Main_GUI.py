#######################################################################################
# SEDHOM SMART HOME DASHBOARD
#######################################################################################

import time

from SEDHOM_Display.Display import SEDHOM_Display
from SEDHOM_Display.SEDHOM_Framework.Switch import Switch

#######################################################################################
# DISPLAY CONFIGURATION
#######################################################################################

SCREEN_WIDTH = 480
SCREEN_HEIGHT = 320

Display = SEDHOM_Display(
    port="COM3",
    boudrate=115200,
    width=SCREEN_WIDTH,
    height=SCREEN_HEIGHT,
    Display="SEDHOM TFT 3.5 inch shield",
    MCU="Arduino Uno"
)

#######################################################################################
# THEME CONFIGURATION
#######################################################################################

THEME = {
    "background": 0x1082,
    "panel": 0x2127,
    "panel_alt": 0x3188,
    "primary": 0x07FF,
    "secondary": 0x07E0,
    "warning": 0xFD20,
    "danger": 0xF800,
    "text": 0xFFFF,
    "muted": 0xBDF7,
    "border": 0x4A69,
    "black": 0x0000,
    "white": 0xFFFF,
}

#######################################################################################
# INITIALIZATION
#######################################################################################

Display.begin()

Display.set_mode(THEME["background"])

#######################################################################################
# SWITCH WIDGETS
#######################################################################################

Light_Switch = Switch(
    Display=Display,
    x=0,
    y=0,
    state=True,
    width=64,
    height=32,
    radius=12,
    padding=4
)

Fan_Switch = Switch(
    Display=Display,
    x=0,
    y=0,
    state=False,
    width=64,
    height=32,
    radius=12,
    padding=4
)

Light_Switch.set_colors(
    on=THEME["secondary"],
    off=THEME["panel_alt"],
    knob=THEME["white"]
)

Fan_Switch.set_colors(
    on=THEME["primary"],
    off=THEME["panel_alt"],
    knob=THEME["white"]
)

#######################################################################################
# HEADER
#######################################################################################

def Draw_Header():

    Display.shape.Rectangle(
        0, 0, 480, 48,
        0, THEME["panel"], True, 0
    )

    Display.text.Text(
        14, 30,
        "SEDHOM",
        THEME["primary"]
    )

    Display.text.Text(
        110, 30,
        "SMART HOME",
        THEME["text"]
    )

    Display.shape.Circle(
        423, 23, 5,
        THEME["secondary"], True
    )

    Display.text.Text(
        435, 28,
        "ON",
        THEME["text"]
    )

    Display.shape.Rectangle(
        0, 47, 480, 2,
        0, THEME["primary"], True, 0
    )

#######################################################################################
# STATUS CARDS
#######################################################################################

def Draw_Status_Cards():

    # Temperature card
    Display.shape.Rectangle(
        12, 60, 145, 84,
        8, THEME["panel"], True, 0
    )

    Display.shape.Circle(
        31, 80, 7,
        THEME["danger"], True
    )

    Display.shape.Line(
        31, 87, 31, 101,
        THEME["danger"]
    )

    Display.text.Text(
        46, 84,
        "TEMP",
        THEME["muted"]
    )

    Display.text.Text(
        24, 119,
        "24.5 C",
        THEME["text"]
    )

    # Humidity card
    Display.shape.Rectangle(
        167, 60, 145, 84,
        8, THEME["panel"], True, 0
    )

    Display.shape.Circle(
        188, 80, 7,
        THEME["primary"], True
    )

    Display.text.Text(
        203, 84,
        "HUMIDITY",
        THEME["muted"]
    )

    Display.text.Text(
        180, 119,
        "58 %",
        THEME["text"]
    )

    # Connectivity card
    Display.shape.Rectangle(
        322, 60, 146, 84,
        8, THEME["panel"], True, 0
    )

    Display.shape.Circle(
        343, 80, 6,
        THEME["secondary"], True
    )

    Display.text.Text(
        356, 84,
        "NETWORK",
        THEME["muted"]
    )

    Display.text.Text(
        336, 119,
        "CONNECTED",
        THEME["secondary"]
    )

#######################################################################################
# CONTROL PANEL
#######################################################################################

def Draw_Control_Panel():

    Display.text.Text(
        14, 170,
        "DEVICE CONTROL",
        THEME["text"]
    )

    # Light panel
    Display.shape.Rectangle(
        12, 184, 222, 112,
        8, THEME["panel"], True, 0
    )

    Display.shape.Circle(
        37, 211, 13,
        THEME["warning"], True
    )

    Display.shape.Circle(
        37, 211, 6,
        THEME["panel"], True
    )

    Display.text.Text(
        59, 209,
        "LIGHT",
        THEME["text"]
    )

    Display.text.Text(
        27, 246,
        "ROOM LIGHT",
        THEME["muted"]
    )

    Light_Switch.set_position(151, 225)
    Light_Switch.draw()

    # Fan panel
    Display.shape.Rectangle(
        246, 184, 222, 112,
        8, THEME["panel"], True, 0
    )

    Display.shape.Circle(
        272, 211, 13,
        THEME["primary"], True
    )

    Display.shape.Circle(
        272, 211, 4,
        THEME["panel"], True
    )

    Display.shape.Triangle(
        272, 197,
        266, 208,
        278, 208,
        THEME["primary"], True
    )

    Display.text.Text(
        294, 209,
        "FAN",
        THEME["text"]
    )

    Display.text.Text(
        261, 246,
        "VENTILATION",
        THEME["muted"]
    )

    Fan_Switch.set_position(385, 225)
    Fan_Switch.draw()

#######################################################################################
# FOOTER
#######################################################################################

def Draw_Footer():

    Display.shape.Rectangle(
        0, 305, 480, 15,
        0, THEME["panel"], True, 0
    )

    Display.text.Text(
        12, 316,
        "SEDHOM SYSTEM",
        THEME["muted"]
    )

    Display.text.Text(
        365, 316,
        "V1.0.0",
        THEME["primary"]
    )

#######################################################################################
# EXTRA SHAPES DEMO
#######################################################################################

def Draw_Decorations():

    # Small decorative ellipse
    Display.shape.Ellipse(
        450, 170,
        7, 3,
        THEME["primary"],
        True
    )

    # Help indicator
    # Display.shape.CircleHelper(
    #     458, 27, 8,
    #     THEME["muted"]
    # )

#######################################################################################
# HOME SCREEN
#######################################################################################

def Draw_Home_Screen():

    Display.fill_screen(THEME["background"])

    Draw_Header()
    time.sleep(2)
    Draw_Status_Cards()
    time.sleep(2)
    Draw_Control_Panel()
    time.sleep(2)
    Draw_Footer()
    time.sleep(2)
    Draw_Decorations()
    time.sleep(2)

    Display.flush()

#######################################################################################
# MAIN
#######################################################################################

try:

    Draw_Home_Screen()

    while True:

        time.sleep(1)

except KeyboardInterrupt:

    print("SEDHOM Smart Home stopped.")

finally:

    Display.close()

#######################################################################################
