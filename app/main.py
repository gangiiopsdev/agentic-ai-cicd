from fastapi import FastAPI
import subprocess
def validate_host(host):
    if not host or len(host) > 255:
        return False
    return True

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return {"status": "error", "error": "Invalid host input"}
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "error": str(e)}