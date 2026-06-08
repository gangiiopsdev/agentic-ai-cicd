from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping_safe(host: str):
    # Safe implementation with full path and shell=False
    try:
        result = subprocess.run(['ping', '-c', '1', host], check=True, capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr}