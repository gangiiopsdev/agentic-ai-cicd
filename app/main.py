from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_safe_host(host):
    return ''.join(e for e in host if e.isalnum() or e in ('-', '.', '_'))

@app.get("/ping")
def ping(host: str):
    safe_host = is_safe_host(host)
    subprocess.run(['ping', safe_host], check=True, text=True, capture_output=True)
    return {'status': 'completed'}