from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    try:
        output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return True, output.stdout
    except subprocess.CalledProcessError as e:
        return False, e.stderr

@app.get("/ping")
def ping(host: str):
    success, result = safe_ping(host)
    if success:
        return {"status": "completed", "output": result}
    else:
        return {"status": "failed", "error": result}