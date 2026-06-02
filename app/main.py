from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def create_subprocess(command):
    args = shlex.split(command)
    return subprocess.Popen(args, shell=False)

def validate_input(input_str):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-:_'
    if not all(char in allowed_chars for char in input_str): raise ValueError('Invalid input')

@app.get("/ping")
def ping(host: str):
    validate_input(host)
    command = f"ping {host}"
    process = create_subprocess(command)
    process.wait()

    return {"status": "completed"}