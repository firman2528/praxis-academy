from object_factory import ObjectFactory


def main() :
    ObjectFactory.initialize()

    instance = ObjectFactory.getType1value1()
    print("{} {}".format(instance.getType(), instance.getValue()))

    instance = ObjectFactory.getType1value2()
    print("{} {}".format(instance.getType(), instance.getValue()))

    instance = ObjectFactory.getType2value1()
    print("{} {}".format(instance.getType(), instance.getValue()))

    instance = ObjectFactory.getType2value2() 
    print("{} {}".format(instance.getType(), instance.getValue()))


if __name__ == "__main__" :
    main()


