import asyncio
import websockets

connected_clients = set()

async def chat_handler(websocket, path):
    # Añadir cliente a la lista de conectados
    connected_clients.add(websocket)
    try:
        async for message in websocket:
            print(f"Mensaje recibido del cliente: {message}")
            
            # Enviar mensaje a todos los clientes conectados
            for client in connected_clients:
                if client != websocket:  # No enviar el mensaje de vuelta al mismo cliente
                    await client.send(f"Servidor: {message}")
    finally:
        # Eliminar cliente de la lista al desconectarse
        connected_clients.remove(websocket)

# Iniciar servidor WebSocket
start_server = websockets.serve(chat_handler, "localhost", 5000)

# Ejecutar el servidor
asyncio.get_event_loop().run_until_complete(start_server)
print("Servidor WebSocket corriendo en ws://localhost:5000")
asyncio.get_event_loop().run_forever()
