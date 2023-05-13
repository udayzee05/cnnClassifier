import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format = '[%(asctime)s]: %(message)s:')

Project_name = "cnn_classifier"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{Project_name}/__init__.py",
    f"src/{Project_name}/components/__init__.py",
    f"src/{Project_name}/utils/__init__.py",
    f"src/{Project_name}/pipeline/__init__.py",
    f"src/{Project_name}/config/__init__.py",
    f"src/{Project_name}/entity/__init__.py",
    f"src/{Project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
]

for filepath in list_of_files:
    filepath = Path(filepath)
    dir, filename = os.path.split(filepath)
    if dir != "":
        os.makedirs(dir, exist_ok=True)
        logging.info(f"Created {dir}")
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w"):
            pass
        logging.info(f"Created {filename}")
    
    else:
        logging.info(f"{filename} already exists")


