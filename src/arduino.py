import time
import serial


class Arduino:
    def __init__(self, port, baudrate=9600):
        self.port = port
        self.baudrate = baudrate
        self.serial = None

    def connect(self):
        self.serial = serial.Serial(self.port, self.baudrate, timeout=2)
        time.sleep(2)

        # wait until READY is received
        while True:
            line = self.serial.readline().decode(errors="ignore").strip()
            if line == "IDLE":
                break

    def disconnect(self):
        if self.serial and self.serial.is_open:
            self.serial.close()

    def query(self, command: str) -> str:
        # extra safety: ensure clean buffer before every command
        self.serial.reset_input_buffer()

        self.serial.write((command + "\n").encode())

        time.sleep(0.1)  # give Arduino time to respond

        response = self.serial.readline().decode(errors="ignore").strip()

        return response