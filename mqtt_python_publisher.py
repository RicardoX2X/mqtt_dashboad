import paho.mqtt.client as mqtt

client = mqtt.Client()
client.connect("mqtt.eclipseprojects.io")
client.publish("lab/temperatura", "teste")
print("Mensagem enviada!")
client.disconnect()