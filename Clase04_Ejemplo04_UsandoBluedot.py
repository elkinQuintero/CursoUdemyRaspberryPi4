from bluedot.btcomm import BluetoothServer

def leer(data):
    print(data)

print("Iniciando servidor Bluetooth")
s = BluetoothServer(leer)