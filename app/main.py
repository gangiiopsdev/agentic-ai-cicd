from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    if not all(char.isalnum() or char in '.,-_' for char in host):
        return "Invalid input"
    subprocess.call(['ping', host])

@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    if isinstance(result, dict):
        return result
    else:
        return {"status": "completed", "message": result}