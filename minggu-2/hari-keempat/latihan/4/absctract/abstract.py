class Window :
    __toolkit = ""
    __purpose = ""

    def __init__(self, toolkit, purpose) :
        self.__toolkit = toolkit
        self.__purpose = purpose
    
    def getToolkit(self) :
        return self.__toolkit

    def getType(self) :
        return self.__purpose


class GtkToolboxWindow(Window) :
    def __init__(self) :
        Window.__init__(self, "Gtk", "ToolboxWindow")


class GtkLayerWindow(Window) :
    def __init__(self) :
        Window.__init__(self, "Gtk", "LayerWindow")


class GtkMainWindow(Window) :
    def __init__(self) :
        Window.__init__(self,"Gtk", "MainWindow")


class QtToolboxWindow(Window) :
    def __init__(self) :
        Window.__init__(self, "Qt", "ToolboxWindow")

class QtLayerWindow(Window) :
    def __init__(self) :
        Window.__init__(self, "Qt", "LayerWindow")

class QtMainWindow(Window) :
    def __init__(self) :
        Window.__init__(self, "Qt", "MainWindow")



# Abstrac factory class
class UIFactory :
    def getToolboxWindow(self) : pass
    def getLayerWindow(self) : pass
    def getMainWindow(self) : pass


class GtkUiFactory(UIFactory) :
    def getToolboxWindow(self) :
        return GtkToolboxWindow()

    def getLayerWindow(self) :
        return GtkLayerWindow()

    def getMainWindow(self) :
        return GtkMainWindow()

class QtUIFactory(UIFactory) :
    def getToolboxWindow(self) :
        return QtToolboxWindow()

    def getLayerWindow(self) :
        return QtLayerWindow()

    def getMainWindow(self) :
        return QtMainWindow()


if __name__=="__main__" :
    gnome = True
    kde = not gnome

    if gnome :
        ui = GtkUiFactory()
    elif kde :
        ui = QtUIFactory()

    toolbox = ui.getToolboxWindow()
    layers = ui.getLayerWindow()
    main = ui.getMainWindow()

    print("{} {}".format(toolbox.getToolkit(), toolbox.getType()))

    print("{} {}".format(layers.getToolkit(), layers.getType()))
    print("{} {}".format(main.getToolkit(), main.getType()))