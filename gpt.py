import tkinter as tk
from tkinter import ttk
from tkinter.ttk import Entry, Button, Label
from tkinter import Listbox

from typing import Optional
import json

WIN_WIDTH_PER = 3/20
WIN_HEIGHT_PER = 4/5
X_OFFSET = -30

class Application(tk.Frame):
    def __init__(self, master: Optional[tk.Tk] =None):
        super().__init__(master)
        assert master is not None

        self.master = master

        self.win_width = int(WIN_WIDTH_PER * SCREEN_WIDTH)
        self.win_height = int(WIN_HEIGHT_PER * SCREEN_HEIGHT)
        screen_x_pos =  int(SCREEN_WIDTH - self.win_width + X_OFFSET)
        screen_y_pos = int(self.win_height* (1-WIN_HEIGHT_PER)/2)

        self.master.geometry(f"{self.win_width}x{self.win_height}+{screen_x_pos}+{screen_y_pos}")
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.label: Label = tk.Label(self, text="Task List")
        self.label.pack()

        self.task_list: Listbox = tk.Listbox(self)
        self.task_list.pack()

        self.entry: Entry = ttk.Entry(self)
        self.entry.pack()

        self.add_button: Button = ttk.Button(self, text="Add Task", style="Custom.TButton", command=self.add_task)
        self.add_button.pack()

        self.done_button: Button = ttk.Button(self, text="Mark Done", style="Custom.TButton", command=self.mark_done)
        self.done_button.pack()

        self.quit_button: Button = ttk.Button(self, text="Quit", style="Custom.TButton", command=self.master.destroy)
        self.quit_button.pack()

    def add_task(self):
        task = self.entry.get()  # Get the task from the entry widget
        if not len(task) > 0:
            # Signal Empty String
            return
        self.task_list.insert(tk.END, task)  # Add the task to the list
        self.entry.delete(0, tk.END)  # Clear the entry widget


    def mark_done(self):
        # Implement the code to mark a task as done
        pass

# Initialize custom themes from styles.json
def init_themes(node: tk.Tk) -> None:
    custom_theme = ttk.Style(node)

    with open('styles.json') as file:
        styles = json.load(file)

        for style_name, style_config in styles.items():
            custom_theme.configure(style_name, **style_config["configure"])

root = tk.Tk()

SCREEN_WIDTH = root.winfo_screenwidth()
SCREEN_HEIGHT = root.winfo_screenheight()

init_themes(root)

app = Application(master=root)
app.mainloop()
