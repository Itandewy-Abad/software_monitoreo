import socket

# Configurar el cliente
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.12', 5000))  # Conectarse a localhost en el puerto 5000

# Enviar mensajes y recibir respuestas del servidor
while True:
    message = input("Escribe un mensaje (o 'exit' para salir): ")
    client_socket.send(message.encode('utf-8'))  # Enviar el mensaje al servidor
    
    if message.lower() == 'exit':
        print("Cerrando conexión...")
        break

    # Recibir respuesta del servidor
    response = client_socket.recv(1024).decode('utf-8')
    print(f"Respuesta del servidor: {response}")

# Cerrar la conexión
client_socket.close()
