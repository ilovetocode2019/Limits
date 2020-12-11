import os
import psutil
import threading
import logging
from multiprocessing import connection

log = logging.getLogger("limits.lock")

address = ("localhost", 1234)

def write():
    with open("limits.lock", "w") as file:
        file.write(str(os.getpid()))

def is_running():
    if not os.path.isfile("limits.lock"):
        write()
        return False

    with open("limits.lock", "r") as file:
        try:
            process = psutil.Process(int(file.read()))
            return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            write()
            return False

def open_window_listener(root):
    listener = connection.Listener(address, authkey=b"limits auth")
    while True:
        conn = listener.accept()

        message = conn.recv()
        if message == b"open_window":
            root.deiconify()

        conn.close()

def open_window():
    client = connection.Client(address, authkey=b"limits auth")
    client.send(b"open_window")
