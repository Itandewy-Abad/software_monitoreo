import socket
import threading
import tkinter as tk

def recibir_mensajes(client_socket, text_widget):
    while True:
        try:
            mensaje = client_socket.recv(1024).decode('utf-8')
            if mensaje:
                text_widget.config(state=tk.NORMAL)
                text_widget.insert(tk.END, "El servidor te dice: " + mensaje + "\n")
                text_widget.config(state=tk.DISABLED)
            else:
                break
        except:
            break

def enviar_mensaje(client_socket, mensaje_entry, text_widget):
    mensaje = mensaje_entry.get()
    if mensaje:
        client_socket.send(mensaje.encode('utf-8'))
        text_widget.config(state=tk.NORMAL)
        text_widget.insert(tk.END, "Yo: " + mensaje + "\n")
        text_widget.config(state=tk.DISABLED)
        mensaje_entry.delete(0, tk.END)

def conectar_al_servidor(ip):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((ip, 12346))

    ventana = tk.Tk()
    ventana.title("Chat Cliente")

    text_widget = tk.Text(ventana, state=tk.DISABLED)
    text_widget.pack()

    mensaje_entry = tk.Entry(ventana)
    mensaje_entry.pack()

    enviar_boton = tk.Button(ventana, text="Enviar", command=lambda: enviar_mensaje(client_socket, mensaje_entry, text_widget))
    enviar_boton.pack()

    thread_recibir = threading.Thread(target=recibir_mensajes, args=(client_socket, text_widget))
    thread_recibir.start()

    ventana.mainloop()

if __name__ == "__main__":
    ip = input("Introduce la IP del servidor: ")
    conectar_al_servidor(ip)
