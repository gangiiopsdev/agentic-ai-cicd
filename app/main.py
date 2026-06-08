from fastapi import FastAPI
import subprocess
def secure_ping(host: str):
    # Secure implementation
    subprocess.call(['ping', '-c', '1', host])

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    secure_ping(host)
    return {"status": "completed"}