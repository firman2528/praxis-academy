import motor.motor_tornado


# client = motor.motor_tornado.MotorClient()
client = motor.motor_tornado.MotorClient('mongodb://localhost:27017')
client2 = motor.motor_tornado.MotorClient('mongodb://host1,host2/?replicaSet=my-replicaset-name')


db = client.test_database
db2 = client2['test_database']