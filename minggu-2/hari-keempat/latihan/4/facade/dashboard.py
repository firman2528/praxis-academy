from dashboard import _DashboardLight

class _HandBrakeLight(_DashboardLight) :
    pass

class _FogLampLight(_DashboardLight) :
    pass

class _Dashboard(object) :
    def __init__(self, ) :
        self.lights = {"handbreak " :_HandBrakeLight, "fog" :_FogLampLight}

    def show(self) :
        for light in self.lights.values() :
            light.status_check()
    