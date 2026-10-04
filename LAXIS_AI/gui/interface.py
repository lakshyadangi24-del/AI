import customtkinter as ctk
import psutil
import time
import customtkinter as ctk

BG = "#050B12"
PANEL = "#0A1625"
CYAN = "#00F5FF"
BLUE = "#00AEEF"
TEXT = "#D9FFFF"

class ChatWindow:

    def __init__(self, brain=None, tts=None):

        self.brain = brain
        self.tts = tts

        ctk.set_appearance_mode("Dark")
        ctk.set_default_color_theme("dark-blue")

        self.app = ctk.CTk()
        self.app.configure(fg_color=BG)
        self.app.title("LAXIS AI v7")
        self.app.geometry("1600x900")
        self.app.minsize(1400, 800)


        # Header
        self.title = ctk.CTkLabel(
            self.app,
            text="LAXIS AI",
            text_color=CYAN,
            font=("Segoe UI", 34, "bold")
        )
        self.title.pack(pady=20)
        self.status = ctk.CTkLabel(
            self.app,
            text="🟢 AI ONLINE   |   🎤 Voice Ready   |   👁 Camera Ready",
            text_color=CYAN,
            font=("Consolas", 15)
        )

        self.status.pack(pady=5)

        # Main Content
        content = ctk.CTkFrame(
            self.app,
            fg_color=BG
        )

        content.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=10
        )
        # Left Panel
        left_panel = ctk.CTkFrame(
            content,
            width=220,
            fg_color=PANEL,
            border_color=CYAN,
            border_width=2
        )

        left_panel.pack(
            side="left",
            fill="both",
            padx=(0, 15),
            pady=20
        )
        ctk.CTkLabel(
            left_panel,
            text="SYSTEM",
            text_color=CYAN,
            font=("Segoe UI", 22, "bold")
        ).pack(pady=15)



        self.cpu_label = ctk.CTkLabel(
            left_panel,
            text="🖥 CPU : 0%",
            text_color=TEXT,
            font=("Consolas", 15)
        )

        self.cpu_label.pack(anchor="w", padx=15, pady=8)

        self.ram_label = ctk.CTkLabel(
            left_panel,
            text="⚡ RAM : 0%",
            text_color=TEXT,
            font=("Consolas", 15)
        )

        self.ram_label.pack(anchor="w", padx=15, pady=8)

        self.net_label = ctk.CTkLabel(
            left_panel,
            text="🌐 Network : 0 KB/s",
            text_color=TEXT,
            font=("Consolas", 15)
        )

        self.net_label.pack(anchor="w", padx=15, pady=8)

        self.voice_label = ctk.CTkLabel(
            left_panel,
            text="🎤 Voice : Ready",
            text_color=TEXT,
            font=("Consolas", 15)
        )

        self.voice_label.pack(anchor="w", padx=15, pady=8)

        self.camera_label = ctk.CTkLabel(
            left_panel,
            text="📷 Camera : Ready",
            text_color=TEXT,
            font=("Consolas", 15)
        )

        self.camera_label.pack(anchor="w", padx=15, pady=8)

        # Save previous network usage
        self.prev_net = psutil.net_io_counters()
        self.prev_time = time.time()

        # Chat Area
        self.chatbox = ctk.CTkTextbox(
            content,
            width=1200,
            height=550,
            fg_color=PANEL,
            border_width=2,
            border_color=CYAN,
            text_color=TEXT,
            font=("Consolas", 15)
        )

        self.chatbox.pack(padx=20, pady=20)
        self.chatbox.pack(
            side="left",
            fill="both",
            expand=True,
            padx=(0, 0),
            pady=20
        )
        self.chatbox.insert(
            "end",
            "🤖 LAXIS AI v8\n\n"
            "Welcome!\n"
            "I'm your personal AI assistant.\n"
            "Type a message below and press ENTER.\n\n"
        )

        self.chatbox.configure(state="disabled")

        # Bottom Frame
        # Bottom Frame
        bottom = ctk.CTkFrame(
            self.app,
            fg_color=BG
        )
        bottom.pack(fill="x", padx=20, pady=10)

        self.entry = ctk.CTkEntry(
            bottom,
            width=1050,
            height=45,
            fg_color=PANEL,
            border_color=CYAN,
            text_color="white",
            placeholder_text="Ask LAXIS..."
        )
        self.entry.pack(
            side="left",
            fill="x",
            expand=True,
            padx=(0,10)
        )

        self.entry.bind("<Return>", self.send_message)

        self.button = ctk.CTkButton(
            bottom,
            text="SEND",
            width=120,
            fg_color=BLUE,
            hover_color=CYAN,
            command=self.send_message
        )

        self.update_system_info()

        self.button.pack(
            side="right",
            padx=(10, 0)
        )

    def send_message(self, event=None):

        question = self.entry.get().strip()

        if not question:
            return

        self.entry.delete(0, "end")

        self.chatbox.configure(state="normal")

        self.chatbox.insert(
            "end",
            f"\n🧑 You: {question}\n"
        )

        if self.brain:
            answer = self.brain.ask(question)
        else:
            answer = "Brain not connected."

        self.chatbox.insert(
            "end",
            f"🤖 LAXIS: {answer}\n\n"
        )

        self.chatbox.configure(state="disabled")
        self.chatbox.see("end")

        if self.tts:
            self.tts.speak(answer)

    def run(self):
        self.app.mainloop()

    def update_system_info(self):

        # CPU
        cpu = psutil.cpu_percent(interval=None)

        # RAM
        ram = psutil.virtual_memory().percent

        # Network
        current = psutil.net_io_counters()

        now = time.time()

        elapsed = now - self.prev_time

        upload = (current.bytes_sent - self.prev_net.bytes_sent) / elapsed

        download = (current.bytes_recv - self.prev_net.bytes_recv) / elapsed

        self.prev_net = current

        self.prev_time = now

        self.cpu_label.configure(
            text=f"🖥 CPU : {cpu:.0f}%"
        )

        self.ram_label.configure(
            text=f"⚡ RAM : {ram:.0f}%"
        )

        self.net_label.configure(
            text=f"🌐 Net ↓ {download / 1024:.1f} KB/s ↑ {upload / 1024:.1f} KB/s"
        )

        self.app.after(1000, self.update_system_info)