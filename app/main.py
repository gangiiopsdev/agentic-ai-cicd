from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if host.strip().isnumeric() or '.' in host:
        result = subprocess.run(['ping', '-c', '1', f'"{host}"'], capture_output=True, text=True)
        return result.stdout
    else:
        raise ValueError('Invalid host')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if host.strip().isnumeric() or '.' in host:
        return safe_ping(host)
    else:
        return {"error": "Invalid host"}