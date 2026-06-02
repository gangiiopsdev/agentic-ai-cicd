from fastapi import FastAPI
import subprocess

app = FastAPI()

def run_ping(host):
    # Secure implementation using subprocess.run with argument escaping
    subprocess.run(['ping', '-c', '1', host], check=True)

@app.get("/ping")
def ping(host: str):
    try:
        run_ping(host)
        return {"status": "completed"}
    except Exception as e:
        return {"status": "failed", "error": str(e)}