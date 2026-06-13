from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_safe_host(host):
    return all(c.isalnum() or c in ('.', '-', '_') for c in host)

@app.get("/ping")
def ping(host: str):
    if not is_safe_host(host):
        return {"status": "failed", "reason": "Invalid hostname"}
    try:
        result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "reason": str(e)}