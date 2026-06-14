from fastapi import FastAPI
import subprocess
def run_ping(host):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    if not all(c.isalnum() or c in '-.' for c in host):
        raise ValueError("Invalid hostname")
    response = run_ping(host)
    return {"status": "completed", "response": response}