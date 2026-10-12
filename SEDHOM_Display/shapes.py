class SEDHOMShapes:

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
    # Format: Pixel, x, y, color;
    def Pixel(self, x, y, color):
        command = (
            f"Pixel, {x}, {y}, "
            f"{self.color(color)}"
        )

        self.serial.send(command)
    # Format: Line, x1, y1, x2, y2, color;
    def Line(self, x1, y1, x2, y2, color):
        command = (
            f"Line, {x1}, {y1}, {x2}, {y2}, "
            f"{self.color(color)}"
        )

        self.serial.send(command)
    # Format: Rect, x, y, h, w, r, color, fill, rotate;
    def Rectangle(
        self,
        x:int,
        y:int,
        width:int,
        height:int,
        radius:int = 0,
        color:int = 0xffff,
        filled:bool = True,
        rotate:int = 0
    ):
        command = (
            f"Rect, {x}, {y}, {height}, {width}, "
            f"{radius}, {self.color(color)}, {int(filled)},{int(rotate)}"
        )

        self.serial.send(command)
    # Format: Circle, x, y, r, color, fill;
    def Circle(self, x:int, y:int, radius:int =10, color:int = 0xfffff, filled:bool = True):
        command = (
            f"Circle, {x}, {y}, {radius}, "
            f"{self.color(color)}, {int(filled)}"
        )

        self.serial.send(command)
    # Format: Ellipse, x, y, rx, ry, color, fill;
    def Ellipse(
        self,
        x,
        y,
        radius_x,
        radius_y,
        color,
        filled
    ):
        command = (
            f"Ellipse, {x}, {y}, {radius_x}, {radius_y}, "
            f"{self.color(color)}, {int(filled)}"
        )

        self.serial.send(command)
    # Format: CircleHelper, x, y, r, corners, delta, color, fill;
    def CircleHelper(
        self,
        x,
        y,
        radius,
        corner_mask,
        delta,
        color,
        filled
    ):
        command = (
            f"CircleHelper, {x}, {y}, {radius}, "
            f"{corner_mask}, {delta}, "
            f"{self.color(color)}, {int(filled)}"
        )

        self.serial.send(command)
    # Format: Triangle, x1, y1, x2, y2, x3, y3, color, fill;
    def Triangle(
        self,
        x1,
        y1,
        x2,
        y2,
        x3,
        y3,
        color,
        filled
    ):
        command = (
            f"Triangle, {x1}, {y1}, {x2}, {y2}, "
            f"{x3}, {y3}, {self.color(color)}, {int(filled)}"
        )

        self.serial.send(command)
