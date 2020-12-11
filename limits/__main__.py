import tkinter
import os
import argparse
import sys
import logging

from app import Application
from lock import is_running, open_window

log = logging.getLogger("limits")
logging.basicConfig(
    level=logging.INFO,
    format="(%(asctime)s) %(levelname)s %(message)s",
    datefmt="%m/%d/%y - %H:%M:%S %Z"
)

def main():
    parser = argparse.ArgumentParser(description="Limits: A program written in python that sets screen time limits")
    parser.add_argument("--window", action="store_true", help="Open the limits window on startup")
    args = parser.parse_args()

    if is_running():
        open_window()
        sys.exit()

    root = tkinter.Tk()
    root.title("Limits")
    root.resizable(width=True, height=True)

    if not args.window:
        root.withdraw()

    app = Application(root)
    app.mainloop()

    sys.exit()

if __name__ == "__main__":
    main()
