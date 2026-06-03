from fastapi import FastAPI
import subprocess

app = FastAPI()

def run_ping(host):
    # Secure implementation using subprocess.run with argument escaping and validation
    if not host.isalnum() or len(host) > 255:
        raise ValueError('Invalid host input')
    subprocess.run(['ping', '-c', '1', host], check=True)

@app.get("/ping")
def ping(host: str):
    try:
        run_ping(host)
        return {"status": "completed"}
    except Exception as e:
        return {"status": "failed", "error": str(e)}