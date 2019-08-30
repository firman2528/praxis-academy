from jeepbuilder import JeepBuilder
from director import Director

def main() :
    jipbuilder = JeepBuilder()
    direktur = Director()

    print("Building Jeep")
    direktur.setBuilder(jipbuilder)
    jeep = direktur.getCar()
    jeep.specification()
    print("")

if __name__ == "__main__" :
    main()