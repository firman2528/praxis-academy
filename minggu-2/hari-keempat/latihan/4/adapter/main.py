from socket_adapter import Socket
from adapter import Adapter
from elektrikkettel import ElectricKettle
def main() :
    #plug in
    sockets = Socket()
    adapter = Adapter(sockets)
    kettle = ElectricKettle(adapter)

    kettle.boil()
    return 0

if __name__ == "__main__" :
    main()