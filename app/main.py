from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_host(host):
    if '.' in host and ':' in host:
        return True
    return False

@app.get("/ping")
def ping(host: str):
    if not sanitize_host(host):
        return {"status": "invalid input"}
    subprocess.run(['ping', host], check=True)
    return {"status": "completed"}