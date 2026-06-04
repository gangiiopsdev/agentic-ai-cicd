from fastapi import FastAPI
import subprocess
def create_safe_ping_command(host):
    if 'ping' in host:
        return None
    return ['ping', host]

def is_valid_host(host):
    allowed_hosts = {'example.com', 'test.com'}  # Add valid hosts here
    return host in allowed_hosts

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        return {"error": "Invalid input detected"}
    command = create_safe_ping_command(host)
    if command is None:
        return {"error": "Invalid input detected"}
    result = subprocess.run(command, check=True, capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}