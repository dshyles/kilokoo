import time
import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn

# create the spi bus
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)

# create the cs (chip select)
cs = digitalio.DigitalInOut(board.D5)

# create the mcp object
mcp = MCP.MCP3008(spi, cs)

# create an analog input channel on pin 0
turbid = AnalogIn(mcp, MCP.P0)
temp = AnalogIn(mcp, MCP.P1)
pH = AnalogIn(mcp, MCP.P2)
pHtemp = AnalogIn(mcp, MCP.P3) #Built-in Temp on pH Probe, PH-4502C

while True:
    print("Turbidity Raw ADC Value: ", turbid.value)
    print("Turbidity ADC Voltage: " + str(turbid.voltage) + "V")
    print("Temp Raw ADC Value: ", temp.value)
    print("Temp ADC Voltage: " + str(temp.voltage) + "V") 
    print("pH Raw ADC Value: ", pH.value)
    print("pH ADC Voltage: " + str(pH.voltage) + "V") 
    print("pHtemp Raw ADC Value: ", pHtemp.value)
    print("pHtemp ADC Voltage: " + str(pHtemp.voltage) + "V") 

    time.sleep(1)
