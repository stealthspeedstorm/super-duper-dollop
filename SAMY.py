#!/usr/bin/python3
import time
import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn

# SPI bus and chip select
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
cs = digitalio.DigitalInOut(board.D22)

# Initializing MCP3008
mcp = MCP.MCP3008(spi, cs)

# Creating an analog input channel on pin 0
channel = AnalogIn(mcp, MCP.P0)

# Funct 2 remap a value from one range to another
def remap(value, in_min, in_max, out_min, out_max):
    return int((value - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

# Loop to read, remap, and print values
while True:
    raw_value = channel.value  # Raw ADC value (0-65535)
    remapped_value = remap(raw_value, 0, 65535, 0, 100)  # Map to 0-100 range
    print("Raw Value:", raw_value)
    print("Remapped Value (0-100):", remapped_value)
    time.sleep(0.5)  # Pause for half a second
