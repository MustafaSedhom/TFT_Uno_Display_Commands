class SEDHOMText:

    def __init__(self, serial_manager):
        self.serial = serial_manager

    @staticmethod
    def color(value):
        if isinstance(value, str):
            value = value.strip()

            if value.lower().startswith("0x"):
                value = int(value, 16)
            else:
                value = int(value)

        return f"0x{value & 0xFFFF:04X}"
    # Format: Text, x, y, txt, foreground_color, background_color, font_mode, font;
    def Text(
        self,
        x:int,
        y:int,
        text:str,
        foreground:int=0xFFFF,
        background:int=0x0000,
        mode:bool=1,
        font:int=0
    ):
        # The semicolon command protocol requires text without semicolons.
        safe_text = str(text).replace(";", ",")

        command = (
            f"Text, {x}, {y}, {str(safe_text)}, "
            f"{self.color(foreground)}, "
            f"{self.color(background)}, "
            f"{int(mode)}, {font} ;"
        )

        self.serial.send(command)
