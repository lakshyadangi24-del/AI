import tkinter as tk
import customtkinter as ctk

from gui.themes import *


class BootScreen:

    def __init__(self):

        ctk.set_appearance_mode("Dark")
        ctk.set_default_color_theme("dark-blue")

        self.window = ctk.CTk()

        # Full screen
        self.window.attributes("-fullscreen", True)

        self.window.configure(fg_color=BG)

        # Screen size
        self.width = self.window.winfo_screenwidth()
        self.height = self.window.winfo_screenheight()

        # Background Canvas
        self.canvas = tk.Canvas(
            self.window,
            width=self.width,
            height=self.height,
            bg=BG,
            highlightthickness=0
        )

        self.canvas.pack(fill="both", expand=True)

        # Grid offset (for animation later)
        self.grid_offset = 0

        # Draw the background grid
        self.draw_grid()

    def run(self):
        self.window.mainloop()

    def draw_grid(self):

        self.canvas.delete("grid")

        spacing = 40

        # Vertical lines
        for x in range(
                -spacing,
                self.width + spacing,
                spacing
        ):
            self.canvas.create_line(
                x + self.grid_offset,
                0,
                x + self.grid_offset,
                self.height,
                fill=GRID,
                width=1,
                tags="grid"
            )

        # Horizontal lines
        for y in range(
                -spacing,
                self.height + spacing,
                spacing
        ):
            self.canvas.create_line(
                0,
                y,
                self.width,
                y,
                fill=GRID,
                width=1,
                tags="grid"
            )