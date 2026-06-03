from fastapi import FastAPI
import subprocess
import shlex
def validate_input(input_str):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_@'
    for char in input_str:
        if char not in allowed_chars:
            return False
    return True

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if validate_input(host):
        subprocess.run(shlex.split(f"ping {host}"), check=True, capture_output=True)
    else:
        raise ValueError("Invalid input")

    return {"status": "completed"}