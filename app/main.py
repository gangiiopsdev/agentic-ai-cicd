from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_host(host):
    return ''.join(c for c in host if c.isalnum() or c in ['-', '_', '.', ':', '/'])

@app.get("/ping")
def ping(host: str):
    safe_host = escape_host(host)
    try:
        subprocess.run(['ping', safe_host], check=True, timeout=5)
        return {"status": "completed"}
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}