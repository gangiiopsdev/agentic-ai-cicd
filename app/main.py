from fastapi import FastAPI
import subprocess
def safe_ping(host: str) -> str:
    allowed_hosts = ['127.0.0.1', '::1']  # Define a list of allowed hosts
    if host not in allowed_hosts:
        raise ValueError("Invalid host")
    try:
        output = subprocess.run(['ping', f'-c 4 {host}'], capture_output=True, text=True, check=True)
        return output.stdout.strip()
    except subprocess.CalledProcessError as e:
        return str(e)

app = FastAPI()
@app.get("/ping")
def ping(host: str):
    try:
        return {"status": "completed", "output": safe_ping(host)}
    except ValueError as e:
        return {"error": str(e), "status": "invalid_host"}