import socket
import threading
import sys

buffer = 1024
direccion = (sys.argv[1], int(sys.argv[2]))

class Servidor(threading.Thread):
	def __init__(self, socket_servidor):
		threading.Thread.__init__(self)
		self.socket = socket_servidor
		
	def run(self):
		while True:
			try:
				datos_recibidos = self.socket.recv(buffer)
				if datos_recibidos == "salir":
					print("La conexion termino")
					break
				print (datos_recibidos.decode("utf-8"),"\n")
			except:
				print ("El servidor termino la conexion inesperadamente")
				break


socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socket_servidor.connect(direccion)

print ("Ingrese su nick: ")
nick = input()
socket_servidor.send(nick.encode("utf-8"))

hilo_mensajes = Servidor(socket_servidor)
hilo_mensajes.start()

while True:
	datos_enviar = input('>')
	if datos_enviar == ":salir":
		socket_servidor.send(datos_enviar.encode("utf-8"))
		break
	socket_servidor.send(datos_enviar.encode("utf-8"))
	
	
socket_servidor.close()

