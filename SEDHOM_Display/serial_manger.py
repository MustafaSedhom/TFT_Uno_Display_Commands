import time
import serial


class SEDHOMSerial:

    def __init__(
        self,
        port="COM3",
        baudrate=115200,
        buffer_size=4096,
        startup_delay=2
    ):
        self.port = port
        self.baudrate = baudrate
        self.buffer_size = buffer_size
        self.startup_delay = startup_delay

        self.connection = None
        self.buffer = bytearray()

        self.bytes_sent = 0
        self.commands_sent = 0
        self.write_count = 0

    def connect(self):
        if self.connection and self.connection.is_open:
            return

        self.connection = serial.Serial(
            self.port,
            self.baudrate,
            timeout=2,
            write_timeout=15
        )

        time.sleep(self.startup_delay)
        self.connection.reset_input_buffer()

        print(f"[Serial] Connected to {self.port}")

    def send(self, command):
        if not command.endswith(";"):
            command += ";"

        encoded = (command + " ").encode("utf-8")

        self.buffer.extend(encoded)
        self.commands_sent += 1

        if len(self.buffer) >= self.buffer_size:
            self.flush()

    def send_many(self, commands):
        for command in commands:
            self.send(command)

    def flush(self):
        if not self.buffer:
            return

        if not self.connection or not self.connection.is_open:
            raise RuntimeError("Serial connection is not open.")

        size = len(self.buffer)

        self.connection.write(self.buffer)

        self.bytes_sent += size
        self.write_count += 1

        self.buffer.clear()

    def close(self):
        if self.buffer and self.connection and self.connection.is_open:
            self.flush()

        if self.connection and self.connection.is_open:
            self.connection.flush()
            self.connection.close()

        print("[Serial] Connection closed")

    def statistics(self):
        return {
            "commands": self.commands_sent,
            "bytes": self.bytes_sent,
            "writes": self.write_count
        }
