from fastapi import FastAPI
import subprocess

app = FastAPI()

def run_command(command):
    return subprocess.run(command, capture_output=True, text=True)

def safe_ping(host):
    try:
        ip_parts = host.split('.')
        if len(ip_parts) != 4 or not all(part.isdigit() for part in ip_parts):
            raise ValueError
        if any(int(part) > 255 for part in ip_parts):
            raise ValueError
    except ValueError:
        return False
    return True

@app.get("/ping")
def ping(host: str):
    if not safe_ping(host):
        raise ValueError("Invalid host")
    command = ["ping", host]
    result = run_command(command)
    return {"status": "completed", "output": result.stdout}