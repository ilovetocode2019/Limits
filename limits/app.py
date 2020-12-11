import tkinter
import psutil
import os
import threading
import time
import json
import logging

from lock import open_window_listener

log = logging.getLogger("limits.app")

class Application(tkinter.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master.protocol("WM_DELETE_WINDOW", self.master.withdraw)

        if not os.path.exists("data"):
            os.mkdir("data")

        if os.path.isfile("data/config.json"):
            with open("data/config.json") as file:
                self.config = json.load(file)
        else:
            with open("data/config.json", "w") as file:
                self.config = {}
                json.dump(self.config, file)

        self.open_window_listener = threading.Thread(target=open_window_listener, args=(self.master,))
        self.open_window_listener.start()
