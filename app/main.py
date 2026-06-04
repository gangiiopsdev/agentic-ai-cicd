from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Sanitize input to prevent injection attacks
    sanitized_host = ''.join(e for e in host if e.isalnum() or e in '-_.')
    subprocess.call(['ping', sanitized_host])

@app.get("/ping")
def ping_route(host: str):
    return ping(host)