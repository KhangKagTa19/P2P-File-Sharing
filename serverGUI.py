import tkinter as tk
from tkinter import ttk, scrolledtext
import threading
from server import FileServer

class ServerGUI:
    def __init__(self, host, port):
        self.server = FileServer(host, port, log_callback=self.log_message)

        self.root = tk.Tk()
        self.root.title("P2P Server GUI")

        # Style configuration
        self.style = ttk.Style()
        self.style.theme_use("clam")  # You can try other themes like 'default', 'alt', etc.

        # Customize colors
        self.root.configure(bg='#2c3e50')  # Background color

        # Frame for the main content
        content_frame = ttk.Frame(self.root, padding=(20, 20))
        content_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # ScrolledText for log messages
        self.log_text = scrolledtext.ScrolledText(content_frame, width=70, height=30, font=('Fira Code', 10), bg='#34495e', fg='#ecf0f1')
        self.log_text.grid(row=1, column=0, columnspan=3, pady=10)

        # Entry for command input
        self.command_entry = ttk.Entry(content_frame, width=40, font=('Fira Code', 10))
        self.command_entry.grid(row=2, column=0, pady=10, padx=10)

        # Button for sending commands
        self.send_command_button = ttk.Button(content_frame, text="Send Command", command=self.send_command, style="Send.TButton")
        self.send_command_button.grid(row=2, column=1, pady=10, padx=10)

        # Button for starting the server
        self.start_button = ttk.Button(content_frame, text="Start Server", command=self.start_server, style="Start.TButton")
        self.start_button.grid(row=3, column=0, pady=10, padx=10, sticky=tk.W)

        # Button for stopping the server
        self.stop_button = ttk.Button(content_frame, text="Stop Server", command=self.stop_server, style="Stop.TButton")
        self.stop_button.grid(row=3, column=1, pady=10, padx=10, sticky=tk.W)

        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

        # Configure button styles
        self.style.configure("Send.TButton", foreground='#ecf0f1', background='#3498db', font=('Fira Code', 10))
        self.style.configure("Start.TButton", foreground='#ecf0f1', background='#2ecc71', font=('Fira Code', 10))
        self.style.configure("Stop.TButton", foreground='#ecf0f1', background='#e74c3c', font=('Fira Code', 10))
        

    def start_server(self):
        threading.Thread(target=self.server.start).start()
        self.log_message("Server started.")

    def stop_server(self):
        self.log_message("Server stopped.")
        self.server.shutdown()

    def send_command(self):
        command = self.command_entry.get()
        threading.Thread(target=self.server.process_server_command, args=(command,)).start()
        self.command_entry.delete(0, tk.END)  # Clear the command entry

    def on_close(self):
        self.server.shutdown()
        self.root.destroy()

    def log_message(self, message):
        self.log_text.insert(tk.END, message + '\n')
        self.log_text.yview(tk.END)

if __name__ == "__main__":
    gui = ServerGUI("172.168.98.196", 3308)
    gui.root.mainloop()