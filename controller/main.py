import tkinter as tk

from config.event_manager import EventManager

if __name__ == "__main__":
    root = tk.Tk()
    event_manager = EventManager(root)
    event_manager.get_element("mouse").actions["print"] = True
    root.mainloop()
