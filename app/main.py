from fastapi import FastAPI
import subprocess
import shlex
import os

app = FastAPI()

def sanitize_input(input_string):
    return [item for item in shlex.split(input_string) if not any(char in item for char in "&|<>`" and os.path.exists(item))]

@app.get("/ping")
def ping(host: str):
    command = sanitize_input(host)
    if not all(os.path.basename(p) == p for p in command):
        raise ValueError('Invalid command')
    subprocess.run(command, check=True)
    return {"status": "completed"}