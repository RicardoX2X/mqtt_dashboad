import paho.mqtt.client as mqtt

client = mqtt.Client()
client.connect("mqtt.eclipseprojects.io")
client.publish("lab/temperatura", "cuca beludo")
print("Mensagem enviada!")
client.disconnect()