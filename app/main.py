from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation using subprocess.run with input validation and escaping
    if not host or len(host) > 255:
        raise ValueError("Invalid host")
    command = ['ping', '-c', '1', host]
    escaped_command = [arg.replace('`', '\\`).replace('$', '\\$') for arg in command]
    subprocess.run(escaped_command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {"status": "completed"}