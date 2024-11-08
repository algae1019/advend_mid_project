import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
NP = os.path.join(BASE_DIR, 'test.txt')

try:
    with open(NP, "r", encoding="utf-8") as file:
        notepad = file.readlines()
except FileNotFoundError:
    print(f"Error: File not found at {NP}")