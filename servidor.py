import socket
import threading
import tkinter as tk

def recibir_mensajes(conn, text_widget):
    while True:
        try:
            mensaje = conn.recv(1024).decode('utf-8')
            if mensaje:
                text_widget.config(state=tk.NORMAL)
                text_widget.insert(tk.END, "El cliente responde: " + mensaje + "\n")
                text_widget.config(state=tk.DISABLED)
            else:
                break
        except:
            break

def enviar_mensaje(conn, mensaje_entry, text_widget):
    mensaje = mensaje_entry.get()
    if mensaje:
        conn.send(mensaje.encode('utf-8'))
        text_widget.config(state=tk.NORMAL)
        text_widget.insert(tk.END, "Yo: " + mensaje + "\n")
        text_widget.config(state=tk.DISABLED)
        mensaje_entry.delete(0, tk.END)

def iniciar_servidor():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 12346))
    server.listen(1)
    print("Esperando conexión...")
    conn, addr = server.accept()
    print(f"Conectado con {addr}")
    
    ventana = tk.Tk()
    ventana.title("Chat Servidor")

    text_widget = tk.Text(ventana, state=tk.DISABLED)
    text_widget.pack()

    mensaje_entry = tk.Entry(ventana)
    mensaje_entry.pack()

    enviar_boton = tk.Button(ventana, text="Enviar", command=lambda: enviar_mensaje(conn, mensaje_entry, text_widget))
    enviar_boton.pack()

    thread_recibir = threading.Thread(target=recibir_mensajes, args=(conn, text_widget))
    thread_recibir.start()

    ventana.mainloop()

if __name__ == "__main__":
    iniciar_servidor()
