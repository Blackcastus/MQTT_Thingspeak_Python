import paho.mqtt.client as mqtt
from time import sleep
from random import randint
import threading
from queue import Queue


print("Ready MQTT")
class IOT_Device:
	def __init__(self, client_id, username, pwd, server, port):
		self.client_id = client_id
		self.username= username
		self.pwd=pwd
		self.server = server
		self.port = port
		self.client=mqtt.Client(self.client_id)
		self.client.on_connect = self.on_connect
		self.client.on_disconnect = self.on_disconnect
		self.client.on_message = self.on_message
		self.client.username_pw_set(username = self.username, password = self.pwd)
		self.client.connect(self.server, self.port, 60)
		self.client.loop_start()
		self.data = 0

	def publish(self, topic, data):
		self.client.publish(topic, data)

	def update_data(self):
		self.data = randint(0, 50)

	def auto_run(self):
		while True:
			self.update_data()
			print(self.data)
			self.publish("channels/2315139/publish", "field1=%s&field2=%s" %(self.data, self.data))
			sleep(5)

	def start(self):
		task = threading.Thread(target=self.auto_run)
		task.start()

	def on_connect(self, client, userdata, flags, rc):
		channel_ID = "2315139"
		print("Connected With Result Code {}".format(rc))
		client.subscribe("channels/%s/subscribe/fields/field3" %(channel_ID)) 

	# Chuong trinh con bao mat ket noi Server
	def on_disconnect(self, client, userdata, rc):
		print("Disconnected From Broker")

	def on_message(self, client, userdata, message):
		print("data", message.payload.decode())		# Hien thi du lieu cuoi cung duoc
		print("Topic", message.topic)			# gui vao Field_1 tren Server ThingSpeak IoT

id = "LQc6LycUNR0PJxQUMAAAFgo"
username = "LQc6LycUNR0PJxQUMAAAFgo"
password = "ZzSrq+W43sBmSTMxx6cdfc/S"


raspi_device = IOT_Device(id, username, password, 'mqtt3.thingspeak.com', 1883)
raspi_device.start()

while True:
	print("hello")
	sleep(4)