from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(host):
    if 'ping' not in host or '\' in host:
        return False
    return True

@app.get("/ping")
def ping(host: str):
    if not sanitize_input(host):
        return {"status": "invalid input"}
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}