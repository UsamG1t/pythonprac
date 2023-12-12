import time
import atexit
from pathlib import Path

PATH = Path('date')
if PATH.exists():
    DATE = float(PATH.read_text())
else:
    DATE = time.time()

def save():
    PATH.write_text(str(DATE))

atexit.register(save)