from fastapi import FastAPI
import subprocess

app = FastAPI()

def run_command(command):
    return subprocess.run(['ping', command], capture_output=True, text=True)

@app.get("/ping")
def ping(host: str):
    if not safe_ping(host):
        raise ValueError("Invalid host")
    result = run_command(host)
    return {"status": "completed", "output": result.stdout}