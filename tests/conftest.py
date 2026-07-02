import pytest
from src.arduino import Arduino

PORT = "COM6"   # CHANGE THIS


@pytest.fixture(scope="session")
def board():
    arduino = Arduino(PORT)
    arduino.connect()
    yield arduino
    arduino.disconnect()