import time


from .serial_manger import SEDHOMSerial
from .shapes import SEDHOMShapes
from .text import SEDHOMText
from .image_sender import SEDHOMImageSender
from .colors import SEDHOMColors


# ============================================================
# SEDHOM DISPLAY
# ============================================================

class SEDHOM_Display:

    # --------------------------------------------------------
    # Constructor
    # --------------------------------------------------------

    def __init__(
        self,
        port:str="COM3",
        boudrate:int=115200,
        width:int=320,
        height:int=240,
        Display:str="SEDHOM Display",
        MCU:str=None,
        buffer_size:int=4096,
        image_min_line_length:int=2
    ):

        # Display Settings
        self.port = port
        self.boudrate = boudrate
        self.width = width
        self.height = height
        self.Display = Display
        self.MCU = MCU

        # Performance Settings
        self.buffer_size = buffer_size
        self.image_min_line_length = image_min_line_length

        # Connection State
        self.is_connected = False

        # Performance Tracking
        self.start_time = None

        # mode color of Display
        self.color_mode = 0x0000

        # rotation of Display
        self.rotation = 1

        # ----------------------------------------------------
        # Initialize Serial Manager
        # ----------------------------------------------------

        self.serial = SEDHOMSerial(
            port=self.port,
            baudrate=self.boudrate,
            buffer_size=self.buffer_size
        )

        # ----------------------------------------------------
        # Initialize Display Components
        # ----------------------------------------------------

        self.shape = SEDHOMShapes(self.serial)

        self.text = SEDHOMText(self.serial)

        self.image = SEDHOMImageSender(
            serial_manager=self.serial,
            width=self.width,
            height=self.height,
            start_x=0,
            start_y=0,
            min_line_length=self.image_min_line_length
        )

        # Colors are available through Display.colors.RED.
        self.colors = SEDHOMColors

    # --------------------------------------------------------
    # Begin Display
    # --------------------------------------------------------

    def begin(self,color_mode:int = 0x0000):

        if self.is_connected:
            return self

        self.start_time = time.perf_counter()

        self.serial.connect()
        self.is_connected = True

        print(f"{self.Display} initialized successfully.")
        print(f"Serial Port : {self.port}")
        print(f"Baud Rate   : {self.boudrate}")
        print(f"Resolution  : {self.width} x {self.height}")

        if self.MCU:
            print(f"Controller  : {self.MCU}")

        self.set_mode(color_mode)
        return self

    # --------------------------------------------------------
    # Clear / Flush Pending Commands
    # --------------------------------------------------------

    def flush(self):
        self._require_connection()
        self.serial.flush()

    # --------------------------------------------------------
    # Check Connection
    # --------------------------------------------------------

    def _require_connection(self):

        if not self.is_connected:
            raise RuntimeError(
                "Display is not connected. Call Display.begin() first."
            )

    # --------------------------------------------------------
    # Display Information
    # --------------------------------------------------------

    def show_info(self):

        print("\n" + "=" * 45)
        print("SEDHOM DISPLAY INFORMATION")
        print("=" * 45)

        print(f"Name        : {self.name}")
        print(f"Resolution  : {self.width} x {self.height}")
        print(f"Serial Port : {self.port}")
        print(f"Baud Rate   : {self.boudrate}")
        print(f"Arduino     : {self.arduino or 'Not specified'}")
        print(f"Connected   : {self.is_connected}")

        print("=" * 45)

    # --------------------------------------------------------
    # Performance Report
    # --------------------------------------------------------

    def show_performance(self):

        stats = self.serial.statistics()

        elapsed = (
            time.perf_counter() - self.start_time
            if self.start_time is not None
            else 0
        )

        print("\n" + "=" * 45)
        print("SEDHOM PERFORMANCE REPORT")
        print("=" * 45)

        print(f"Commands queued : {stats['commands']:,}")
        print(f"Bytes sent      : {stats['bytes']:,}")
        print(f"Serial writes   : {stats['writes']:,}")
        print(f"Elapsed time    : {elapsed:.3f} seconds")

        print("=" * 45)

    # --------------------------------------------------------
    # Close Display
    # --------------------------------------------------------

    def close(self):

        if not self.is_connected:
            return

        try:
            self.serial.flush()
        finally:
            self.serial.close()
            self.is_connected = False

        self.show_performance()

    # --------------------------------------------------------
    # Context Manager Support
    # --------------------------------------------------------

    def __enter__(self):
        return self.begin()

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()
        return False
    
    #######################################################################################
    # Screen Settings
    #######################################################################################

    def fill_screen(self, fill_color: int = 0x0000):
        self.shape.Rectangle(
            0,
            0,
            self.width,
            self.height,
            0,
            fill_color,
            True,
            0
        )
        self.flush()
        return True

    #######################################################################################
    # Color Mode
    #######################################################################################

    def set_mode(self, color_mode: int):
        self.color_mode = color_mode
        self.fill_screen(color_mode)

        return self.color_mode

    def change_mode(self):
        self.set_mode(self.get_not_mode())

    def get_mode(self) -> int:
        return self.color_mode


    def get_not_mode(self) -> int:
        if self.color_mode == self.colors.Black:
            return self.colors.White

        return self.colors.Black


    #######################################################################################
    # Display Rotation
    #######################################################################################

    def set_rotation(self, rotation: int):
        self.rotation = rotation

        return self.rotation


    def get_rotation(self) -> int:
        return self.rotation

    #######################################################################################
    # Display Rotation
    #######################################################################################

    def restart_Display():
        pass
