import motor.motor_tornado


# client = motor.motor_tornado.MotorClient()
client = motor.motor_tornado.MotorClient('mongodb://localhost:27017')
client2 = motor.motor_tornado.MotorClient('mongodb://host1,host2/?replicaSet=my-replicaset-name')


db = client.test_database
db2 = client2['test_database']

db3 = motor.motor_tornado.MotorClient().test_database

application = tornado.web.Application([
    (r'/', MainHandler)
], db=db)

application.listen(8888)
tornado.ioloop.IOLoop.current().start()


class MainHandler(tornado.web.RequestHandler) :
    def get(self) :
        db = self.settings['db']