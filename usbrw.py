import time
from pymodbus.client.sync import ModbusSerialClient 

client = ModbusSerialClient(method='rtu' , port='/dev/ttyUSB0' , stopbits=1, bytesize=8, parity='N' , baudrate=115200, timeout=3)

connection = client.connect()
print(connection)

if client.connect():
    rea = client.read_holding_registers(address=0, count=15, unit=1);
    wri1 = client.write_register(8192, 25, unit=1);
    #print(wri1)
    wri2 = client.write_register(8193, 25, unit=1);
    #print(wri2)
    wri3 = client.write_register(8194, 16000, unit=1);
    #print(wri3)
    wri4 = client.write_register(8196, 0, unit=1);
    #print(wri4)

    if not rea.isError():
        print(rea.registers)
    else:
        print(rea)

else:
    print("cannot connect")

