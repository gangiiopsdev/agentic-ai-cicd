from fastapi import FastAPI
import subprocess
def sanitize_input(input_str):
    return input_str.strip()

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    command = ['ping', sanitized_host]
    if all(isinstance(arg, str) for arg in command):
        subprocess.run(command, check=True)
    return {"status": "completed"}