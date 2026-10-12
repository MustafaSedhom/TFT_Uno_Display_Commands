# ============================================================
# SEDHOM COLORS
# ============================================================

class SEDHOMColors:
    # --------------------------------------------------------
    # RGB565 Color Constants
    # --------------------------------------------------------

    Black       = 0x0000
    White       = 0xFFFF
    Red         = 0xF800
    Green       = 0x07E0
    Blue        = 0x001F
    Yellow      = 0xFFE0
    Cyan        = 0x07FF
    Magenta     = 0xF81F
    Orange      = 0xFD20
    Purple      = 0x8010
    Pink        = 0xF81F
    Gray        = 0x8410
    Dark_Gray   = 0x4208
    Light_Gray  = 0xC618
    Brown       = 0xA145
    Navy        = 0x000F
    Teal        = 0x0410
    Lime        = 0x07E0
    Maroon      = 0x7800
    Olive       = 0x7BE0
    Silver      = 0xC618
    Gold        = 0xFEA0
    Sky_Blue    = 0x867D

    # --------------------------------------------------------
    # Named Color Dictionary
    # --------------------------------------------------------

    COLORS = {
        "black": Black,
        "white": White,
        "red": Red,
        "green": Green,
        "blue": Blue,
        "yellow": Yellow,
        "cyan": Cyan,
        "magenta": Magenta,
        "orange": Orange,
        "purple": Purple,
        "pink": Pink,
        "gray": Gray,
        "dark_gray": Dark_Gray,
        "light_gray": Light_Gray,
        "brown": Brown,
        "navy": Navy,
        "teal": Teal,
        "lime": Lime,
        "maroon": Maroon,
        "olive": Olive,
        "silver": Silver,
        "gold": Gold,
        "sky_blue": Sky_Blue,
    }

    # --------------------------------------------------------
    # Get Color By Name
    # --------------------------------------------------------

    @classmethod
    def get(cls, name):
        if isinstance(name, int):
            return cls.to_rgb565(name)

        key = name.strip().lower().replace(" ", "_")

        if key not in cls.COLORS:
            raise ValueError(f"Unknown color: {name}")

        return cls.COLORS[key]

    # --------------------------------------------------------
    # Convert RGB888 To RGB565
    # --------------------------------------------------------

    @staticmethod
    def rgb888_to_rgb565(red, green, blue):
        red &= 0xFF
        green &= 0xFF
        blue &= 0xFF

        return (
            ((red & 0xF8) << 8)
            | ((green & 0xFC) << 3)
            | (blue >> 3)
        )

    # --------------------------------------------------------
    # Convert RGB565 To RGB888
    # --------------------------------------------------------

    @staticmethod
    def rgb565_to_rgb888(color):
        color = SEDHOMColors.to_rgb565(color)

        red = (color >> 11) & 0x1F
        green = (color >> 5) & 0x3F
        blue = color & 0x1F

        red = (red << 3) | (red >> 2)
        green = (green << 2) | (green >> 4)
        blue = (blue << 3) | (blue >> 2)

        return red, green, blue

    # --------------------------------------------------------
    # Convert Color To RGB565 Integer
    # Accepts:
    #   Integer: 0xFFFF
    #   String:  "0xFFFF"
    #   String:  "#FF0000"
    #   Tuple:   (255, 0, 0)
    #   Name:    "red"
    # --------------------------------------------------------

    @classmethod
    def to_rgb565(cls, color):
        if isinstance(color, int):
            if not 0 <= color <= 0xFFFF:
                raise ValueError("RGB565 color must be between 0x0000 and 0xFFFF")
            return color

        if isinstance(color, (tuple, list)):
            if len(color) != 3:
                raise ValueError("RGB color must contain exactly 3 values")

            red, green, blue = color

            if not all(isinstance(v, int) and 0 <= v <= 255
                       for v in (red, green, blue)):
                raise ValueError("RGB values must be integers between 0 and 255")

            return cls.rgb888_to_rgb565(red, green, blue)

        if isinstance(color, str):
            value = color.strip()

            if value.startswith("#"):
                value = value[1:]

                if len(value) != 6:
                    raise ValueError("Hex RGB colors must contain 6 digits")

                try:
                    rgb = int(value, 16)
                except ValueError as exc:
                    raise ValueError(f"Invalid hex color: {color}") from exc

                red = (rgb >> 16) & 0xFF
                green = (rgb >> 8) & 0xFF
                blue = rgb & 0xFF

                return cls.rgb888_to_rgb565(red, green, blue)

            if value.lower().startswith("0x"):
                try:
                    return cls.to_rgb565(int(value, 16))
                except ValueError as exc:
                    raise ValueError(f"Invalid RGB565 color: {color}") from exc

            return cls.get(value)

        raise TypeError(f"Unsupported color type: {type(color).__name__}")

    # --------------------------------------------------------
    # Format Color For Serial Commands
    # --------------------------------------------------------

    @classmethod
    def format(cls, color):
        return f"0x{cls.to_rgb565(color):04X}"

    # --------------------------------------------------------
    # Get RGB Tuple
    # --------------------------------------------------------

    @classmethod
    def to_rgb(cls, color):
        return cls.rgb565_to_rgb888(cls.to_rgb565(color))

    # --------------------------------------------------------
    # Convert RGB565 To Hex RGB String
    # Example: 0xF800 -> "#FF0000"
    # --------------------------------------------------------

    @classmethod
    def to_hex_rgb(cls, color):
        red, green, blue = cls.to_rgb(color)
        return f"#{red:02X}{green:02X}{blue:02X}"