from fastapi import FastAPI
import subprocess
def secure_ping(host: str):
    # Secure implementation
    subprocess.run(['ping', host], check=True)
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    return secure_ping(host)