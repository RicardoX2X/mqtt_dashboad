import paho.mqtt.subscribe as subscribe

while(1):
    print("Esperando a mensagem!")
    msg = subscribe.simple("lab/temperatura", hostname="mqtt.eclipseprojects.io", msg_count=1)
    print("Mensagem: ")
    print(msg.payload)