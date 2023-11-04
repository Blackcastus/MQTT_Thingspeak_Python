import paho.mqtt.client as mqtt
from time import sleep
from random  import randint

def on_connect(client, userdata, flags, rc):
    channel_ID = "2315139"
    print("Connected With Result Code {}".format(rc))
    client.subscribe("channels/%s/subscribe/fields/field3" % (channel_ID)) 

# Chuong trinh con bao mat ket noi Server
def on_disconnect(client, userdata, rc):
    print("Disconnected From Broker")

# Chuong trinh con nhan du lieu tu Server
def on_message(client, userdata, message):
    print("a", message.payload.decode())		# Hien thi du lieu cuoi cung duoc
    print("b", message.topic)			# gui vao Field_1 tren Server ThingSpeak IoT
    
client = mqtt.Client('LQc6LycUNR0PJxQUMAAAFgo')
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_message = on_message
client.username_pw_set(username = "LQc6LycUNR0PJxQUMAAAFgo", password = "ZzSrq+W43sBmSTMxx6cdfc/S")
client.connect("mqtt3.thingspeak.com", 1883, 60)
client.loop_start()

def thingspeak_mqtt(data):
    channel_ID = "2315139"
    client.publish("channels/%s/publish" %(channel_ID), "field1=%s&status=MQTTPUBLISH" %(data))

while True:
    # Gui du lieu ngau nhien len Server ThingSpeak sau moi 20s
    data_random = randint(0,50)     # Tao cac gia tri du lieu ngau nhien
    # print(data_random)
    
    # thingspeak_mqtt(data_random)
    
    sleep(5)
