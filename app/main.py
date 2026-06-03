from fastapi import FastAPI
import subprocess

app = FastAPI()

def secure_ping(host: str):
    # Sanitize input to prevent injection attacks
    if not host.isalnum():
        raise ValueError('Invalid hostname')
    subprocess.call(['ping', host])

@app.get("/ping")
def ping(host: str):
    try:
        secure_ping(host)
        return {"status": "completed"}
    except ValueError as e:
        return {"error": str(e)}, 400