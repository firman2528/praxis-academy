from dependency_injector import provider, singleton
class Api :
    def fetch_remote_data(self) :
        print('Api called')
        return 42


class BusinessLogic :
    def __init__(self, api : Api) :
        self.api = api

    def do_stuff(self) :
        api_result = self.api.fetch_remote_data()
        print("the api returned a result :", api_result)


class AppModule(Module) :

    @singleton
    @provider
    def provide_business_logic(self, api:Api) -> BusinessLogic :
        return BusinessLogic(api=api)

    @singleton
    @provider
    def provide_api(self) -> Api :
        configuration
        return Api()