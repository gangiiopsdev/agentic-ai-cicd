from fastapi import FastAPI
import subprocess
def safe_subprocess(command: str, *args):
    cmd_parts = [quote(arg) for arg in command.split(' ')]
    subprocess.run(cmd_parts, check=True)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Sanitize input to prevent command injection
    safe_host = quote(host)
    if not safe_host:
        raise ValueError("Invalid input")
    safe_subprocess(f'ping {safe_host}')
    return {"status": "completed"}