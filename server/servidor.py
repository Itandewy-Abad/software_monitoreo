import socket

# Configurar el servidor
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('127.0.0.12', 5000))  # Usar localhost en el puerto 5000
server_socket.listen(1)
print("Servidor escuchando en 127.0.0.12:5000...")

# Aceptar una conexión
client_socket, addr = server_socket.accept()
print(f"Conexión establecida con {addr}")

# Recibir y responder a mensajes del cliente manualmente
while True:
    # Recibir el mensaje del cliente
    message = client_socket.recv(1024).decode('utf-8')
    if not message or message.lower() == 'exit':
        print("El cliente ha cerrado la conexión.")
        break
    
    # Mostrar el mensaje recibido del cliente
    print(f"Mensaje recibido del cliente: {message}")

    # Escribir una respuesta para el cliente
    response = input("Escribe una respuesta para el cliente: ")

    # Enviar la respuesta al cliente cuando se presiona Enter
    client_socket.send(response.encode('utf-8'))

# Cerrar la conexión
client_socket.close()
server_socket.close()
