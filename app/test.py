from pathlib import Path

# Getting the absolute path for the current file (views.py)
BASE_PATH = Path(__file__).resolve().parent

if __name__ == '__name__':
    print(BASE_PATH.joinpath('static'))