import requests

from PIL import Image
from io import BytesIO


class SEDHOMImageSender:

    def __init__(
        self,
        serial_manager,
        width=100,
        height=100,
        start_x=0,
        start_y=0,
        min_line_length=2
    ):
        self.serial = serial_manager

        self.width = width
        self.height = height

        self.start_x = start_x
        self.start_y = start_y

        self.min_line_length = min_line_length

    # =========================================================
    # RGB888 TO RGB565
    # =========================================================

    @staticmethod
    def rgb888_to_rgb565(r, g, b):
        return (
            ((r >> 3) << 11)
            | ((g >> 2) << 5)
            | (b >> 3)
        )

    # =========================================================
    # LOAD AND RESIZE IMAGE
    # =========================================================

    def load_image(self, source, width, height):

        if isinstance(source, str) and source.lower().startswith(
            ("http://", "https://")
        ):
            response = requests.get(
                source,
                timeout=30,
                headers={"User-Agent": "Mozilla/5.0"}
            )

            response.raise_for_status()

            image = Image.open(
                BytesIO(response.content)
            ).convert("RGB")

        else:
            image = Image.open(source).convert("RGB")

        image = image.resize(
            (width, height),
            Image.Resampling.LANCZOS
        )

        return image

    # =========================================================
    # GENERATE DRAWING COMMANDS
    # =========================================================

    def generate_commands(
        self,
        image,
        width,
        height,
        start_x,
        start_y
    ):

        pixels = list(image.getdata())

        rgb565 = [
            self.rgb888_to_rgb565(r, g, b)
            for r, g, b in pixels
        ]

        commands = []

        for y in range(height):

            row_start = y * width

            row = rgb565[
                row_start:row_start + width
            ]

            x = 0

            while x < width:

                color = row[x]
                run_start = x

                while (
                    x + 1 < width
                    and row[x + 1] == color
                ):
                    x += 1

                run_end = x

                run_length = (
                    run_end - run_start + 1
                )

                x1 = start_x + run_start
                x2 = start_x + run_end
                y1 = start_y + y

                if run_length >= self.min_line_length:

                    command = (
                        f"Line, {x1}, {y1}, "
                        f"{x2}, {y1}, "
                        f"0x{color:04X}"
                    )

                else:

                    command = (
                        f"Pixel, {x1}, {y1}, "
                        f"0x{color:04X}"
                    )

                commands.append(command)

                x += 1

        return commands

    # =========================================================
    # DRAW IMAGE
    # =========================================================


    def draw(self, source, x, y, w, h):

        if not isinstance(w, int) or not isinstance(h, int):
            raise TypeError("Image width and height must be integers")

        if w <= 0 or h <= 0:
            raise ValueError("Image width and height must be positive")

        if not isinstance(x, int) or not isinstance(y, int):
            raise TypeError("Image x and y must be integers")

        print("[Image] Loading image...")

        image = self.load_image(source, w, h)

        print(f"[Image] Image size: {w}x{h}")
        print(f"[Image] Position: x={x}, y={y}")
        print("[Image] Generating commands...")

        commands = self.generate_commands(
            image=image,
            width=w,
            height=h,
            start_x=x,
            start_y=y
        )

        print(f"[Image] Commands: {len(commands):,}")

        self.serial.send_many(commands)

        print("[Image] Commands queued")

        return True

