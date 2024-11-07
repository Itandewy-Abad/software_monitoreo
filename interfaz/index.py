import tkinter as tk
from tkinter import messagebox, font, Toplevel
import ttkbootstrap as ttk  # Importar ttkbootstrap en lugar de tkinter

class MonitoringApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Software de Monitoreo")
        self.root.geometry("800x600")
        self.root.configure(bg="#f0f0f0")

        # Fuente personalizada
        self.custom_font = font.Font(family="Helvetica", size=12)

        # Sección de Monitoreo de PCs
        self.monitor_frame = ttk.LabelFrame(root, text="Monitoreo Remoto", padding=10, bootstyle="primary")
        self.monitor_frame.pack(fill="both", expand=True, padx=20, pady=10)

        self.label_pc = ttk.Label(self.monitor_frame, text="Selecciona el PC a monitorear:", font=self.custom_font)
        self.label_pc.grid(row=0, column=0, padx=5, pady=5)

        self.view_button_1 = ttk.Button(self.monitor_frame, text="Ver lo que hace otro PC remoto", 
                                        command=self.monitor_pc, bootstyle="success")
        self.view_button_1.grid(row=0, column=1, padx=5, pady=5)

        self.view_button_2 = ttk.Button(self.monitor_frame, text="Mostrar al Servidor", 
                                        command=self.monitor_pc, bootstyle="success")
        self.view_button_2.grid(row=0, column=2, padx=5, pady=5)

        # Transferencia de información
        self.transfer_frame = ttk.LabelFrame(root, text="Transferencia de Información", padding=10, bootstyle="info")
        self.transfer_frame.pack(fill="both", expand=True, padx=20, pady=10)

        self.send_button = ttk.Button(self.transfer_frame, text="Enviar datos", 
                                      command=self.send_data, bootstyle="primary")
        self.send_button.grid(row=0, column=0, padx=5, pady=5)

        self.receive_button = ttk.Button(self.transfer_frame, text="Recibir datos", 
                                         command=self.receive_data, bootstyle="primary")
        self.receive_button.grid(row=0, column=1, padx=5, pady=5)

        # Chat bidireccional
        self.chat_frame = ttk.LabelFrame(root, text="Chat", padding=10, bootstyle="info")
        self.chat_frame.pack(fill="both", expand=True, padx=20, pady=10)

        self.send_chat_button = ttk.Button(self.chat_frame, text="Comenzar a Chatear", 
                                           command=self.abrir_ventana_chat, bootstyle="primary")
        self.send_chat_button.grid(row=0, column=0, padx=5, pady=5)

        # Control de Teclado y Mouse
        self.control_frame = ttk.LabelFrame(root, text="Control de Teclado y Mouse", padding=10, bootstyle="info")
        self.control_frame.pack(fill="both", expand=True, padx=20, pady=10)

        self.block_button = ttk.Button(self.control_frame, text="Bloquear Teclado/Mouse", 
                                       command=self.block_input, bootstyle="danger")
        self.block_button.grid(row=0, column=0, padx=5, pady=5)

        self.unblock_button = ttk.Button(self.control_frame, text="Desbloquear Teclado/Mouse", 
                                         command=self.unblock_input, bootstyle="success")
        self.unblock_button.grid(row=0, column=1, padx=5, pady=5)

        # Apagar PC Remotamente
        self.shutdown_button = ttk.Button(root, text="Apagar PC Remoto", 
                                          command=self.shutdown_pc, bootstyle="danger")
        self.shutdown_button.pack(pady=10)

        # Control de Acceso Web y Ping
        self.web_control_frame = ttk.LabelFrame(root, text="Control de Acceso Web y Ping", padding=10, bootstyle="info")
        self.web_control_frame.pack(fill="both", expand=True, padx=20, pady=10)

        self.block_web_button = ttk.Button(self.web_control_frame, text="Denegar acceso a sitios web", 
                                           command=self.block_web, bootstyle="danger")
        self.block_web_button.grid(row=0, column=0, padx=5, pady=5)

        self.allow_ping_button = ttk.Button(self.web_control_frame, text="Permitir Ping", 
                                            command=self.allow_ping, bootstyle="success")
        self.allow_ping_button.grid(row=1, column=0, padx=5, pady=5)

        self.deny_ping_button = ttk.Button(self.web_control_frame, text="Denegar Ping", 
                                           command=self.deny_ping, bootstyle="danger")
        self.deny_ping_button.grid(row=1, column=1, padx=5, pady=5)

    # Métodos de la aplicación
    def monitor_pc(self):
        messagebox.showinfo("Monitoreo", "Monitoreando PC seleccionado")

    def send_data(self):
        messagebox.showinfo("Transferencia de Información", "Datos enviados.")

    def receive_data(self):
        messagebox.showinfo("Transferencia de Información", "Datos recibidos.")

    def send_message(self):
        messagebox.showinfo("Chat", "Mensaje enviado.")

    def block_input(self):
        messagebox.showinfo("Control", "Teclado y mouse bloqueados.")

    def unblock_input(self):
        messagebox.showinfo("Control", "Teclado y mouse desbloqueados.")

    def shutdown_pc(self):
        messagebox.showinfo("Apagar PC", "PC remoto apagado.")

    def block_web(self):
        messagebox.showinfo("Control Web", "Acceso a sitios web denegado.")

    def allow_ping(self):
        messagebox.showinfo("Control Ping", "Ping permitido.")

    def deny_ping(self):
        messagebox.showinfo("Control Ping", "Ping denegado.")

    # Nueva ventana de chat
    def abrir_ventana_chat(self):
        # Crear una nueva ventana para el chat
        ventana_chat = Toplevel(self.root)
        ventana_chat.title("Chat")
        ventana_chat.geometry("400x300")

        # Área de texto para el chat
        text_area = tk.Text(ventana_chat, height=10, width=50)
        text_area.pack(pady=10)

        # Entrada para escribir el mensaje
        message_entry = ttk.Entry(ventana_chat, width=40)
        message_entry.pack(pady=5)

        # Botón para enviar el mensaje
        send_button = ttk.Button(ventana_chat, text="Enviar", 
                                 command=lambda: self.send_message_chat(text_area, message_entry))
        send_button.pack(pady=5)

    def send_message_chat(self, text_area, message_entry):
        message = message_entry.get()
        if message:
            text_area.insert(tk.END, f"Tú: {message}\n")
            message_entry.delete(0, tk.END)


# Iniciar la aplicación
if __name__ == "__main__":
    root = ttk.Window(themename="flatly")  # Usar la ventana de ttkbootstrap con un tema moderno
    app = MonitoringApp(root)
    root.mainloop()
