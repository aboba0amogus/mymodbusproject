from pymodbus.client import ModbusSerialClient
print("start main.py")

client = ModbusSerialClient(
    port="/dev/ttyUSB0",
    baudrate=9600,
    bytesize=8,
    parity='E',
    stopbits=2,
    name="mymodbusproject")

response = client.read_holding_registers(address=36864,count=1,device_id=10)
print(response)

