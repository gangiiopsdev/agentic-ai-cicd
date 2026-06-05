from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    if not host.replace('.', '').isnumeric():
        raise ValueError("Invalid host")

@app.get("/ping")
def ping(host: str):
    try:
        validate_host(host)
        result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}
    except (subprocess.CalledProcessError, ValueError) as e:
        return {"status": "failed", "error": str(e)}