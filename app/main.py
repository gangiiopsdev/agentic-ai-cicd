from fastapi import FastAPI
import subprocess

app = FastAPI()

def create_safe_ping_command(host):
    if 'ping' in host:
        return None
    return ['ping', host]

@app.get("/ping")
def ping(host: str):
    command = create_safe_ping_command(host)
    if command is None:
        return {"error": "Invalid input detected"}
    subprocess.call(command)
    return {"status": "completed"}