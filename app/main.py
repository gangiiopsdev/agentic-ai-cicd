from fastapi import FastAPI
import subprocess
import shlex
def sanitize_input(input_str):
    return ''.join(char for char in input_str if char.isalnum() or char.isdigit())

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    args = shlex.split(f"ping {sanitized_host}")
    subprocess.call(args)
    return {"status": "completed"}