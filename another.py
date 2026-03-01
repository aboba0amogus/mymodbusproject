from pymodbus.client import ModbusSerialClient
print("start main.py")

print("пробуем на частоте 9600 разные настройки")
baudrate = 9600
parities = ['E','O','N']
stopbits = [1,2]
device_ids = [10,0]
reg_addresses = [0,1,90,0x9000,0x9000-1,0x9000+1]

for device_id in device_ids:
    for parity in parities:
        for stopbit in stopbits:
            for reg_address in reg_addresses:
                print(f"значения    baudrate:{baudrate}    parity:{parity}    stopbit:{stopbit}    id:{device_id} reg_address:{reg_address}")
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
print("команда завершена")


