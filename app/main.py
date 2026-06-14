from fastapi import FastAPI
import subprocess

app = FastAPI()

def secure_ping(host):
    try:
        result = subprocess.run(['ping', host], check=True, timeout=10)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}

@app.get("/ping")
def ping(host: str):
    # Secure implementation using subprocess.run with shell=False and safely passed arguments
    return secure_ping(host)