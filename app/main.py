from fastapi import FastAPI
import subprocess
def create_safe_ping_command(host):
    if 'ping' in host:
        return None
    return ['ping', host]

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    command = create_safe_ping_command(host)
    if command is None:
        return {"error": "Invalid input detected"}
    subprocess.run(command, check=True, capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}