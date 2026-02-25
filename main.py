from pymodbus.client import ModbusSerialClient
print("start main.py")

print ("пробуем перебрать все значения")
baudrates = [9600,19200,4800,1200,2400,38400,57600]
parityes = ['E','O','N']
stopbits = [1,1.5,2]

for device_id in range(248):
    for baudrate in baudrates:
        for parity in parityes:
            for stopbit in stopbits:
                print(f"значения    baudrate:{baudrate}    parity:{parity}    stopbit:{stopbit}    id:{device_id}")
                try:
                    client = ModbusSerialClient(
                    port="/dev/ttyUSB0",
                    baudrate=baudrate,
                    bytesize=8,
                    parity=parity,
                    stopbits=stopbit,
                    name="mymodbusproject")
                    response  = client.read_holding_registers(address=0x9000,count=1,device_id=device_id)
                    print(response)
                    print("YES!")
                except Exception as e:
                    print("NOT")
                    print(e)
                finally:
                    client.close()
print("команда закончена")
