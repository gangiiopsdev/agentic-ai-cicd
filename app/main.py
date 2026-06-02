from fastapi import FastAPI
import subprocess

app = FastAPI()

def run_command(command):
    return subprocess.run(command, capture_output=True, text=True)

def safe_ping(host):
    if host.replace('.', '', 3).isdigit():
        return True
    return False

@app.get("/ping")
def ping(host: str):
    if not safe_ping(host):
        raise ValueError("Invalid host")
    command = ["ping", host]
    result = run_command(command)
    return {"status": "completed", "output": result.stdout}