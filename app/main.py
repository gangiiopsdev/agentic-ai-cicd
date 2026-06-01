from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    escaped_host = ''.join(c if c.isalnum() or c in '_-.,' else f'\\{ord(c):03o}' for c in host)
    subprocess.run(['ping', escaped_host], check=True, capture_output=True, text=True)
    return {"status": "completed"}